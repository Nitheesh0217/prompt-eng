##
## Prompt Engineering Lab
## Platform for Education and Experimentation with Prompt Engineering in Generative Intelligent Systems
## _pipeline.py :: Simulated GenAI Pipeline 
##
#  
# Copyright (c) 2025 Dr. Fernando Koch,
# The Generative Intelligence Lab @ FAU
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# Documentation and Getting Started:
#    https://github.com/GenILab-FAU/prompt-eng
#
# Disclaimer: 
# Generative AI has been used extensively while developing this package.
#

import requests
import json
import os
import time

def load_config():
    """
    Load a configuration file from one of several possible locations.
    The file should contain lines in the format KEY=VALUE, which are
    stored as environment variables.

    Example _config file:
        # Lines starting with '#' are ignored
        URL_GENERATE=https://your-llm-service.com/generate
        API_KEY=abc123
    """
    config_locations = [
        "./_config",
        "prompt-eng/_config",
        "../_config"
    ]
    
    config_path = None
    for location in config_locations:
        if os.path.exists(location):
            config_path = location
            break
    
    if not config_path:
        raise FileNotFoundError("Configuration file not found in any of the expected locations.")
    
    # Read the _config file and set environment variables
    with open(config_path, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip comments and empty lines
            if line and not line.startswith("#"):
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()

def create_payload(model, prompt, target="ollama", **kwargs):
    """
    Create the request payload in the format required by the Model Server.

    :param model:   (str) The model name (e.g., 'Llama-3.2-3B-Instruct').
    :param prompt:  (str) The text prompt to send to the model.
    :param target:  (str) Either 'ollama' or 'open-webui' to specify server type.
    :param kwargs:  Additional arguments such as temperature, num_ctx, num_predict, etc.
    :return:        (dict) A JSON-serializable payload compatible with the chosen server.
    
    @NOTE:
      - This function currently supports only two server formats: 'ollama' and 'open-webui'.
      - Adjust or expand as needed for new endpoints.
      - For 'ollama', we place 'prompt' at the root of the payload.
      - For 'open-webui', we nest 'prompt' under 'messages' with a 'role' of 'user'.
    """
    payload = None
    if target == "ollama":
        # Ollama format
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
        }
        if kwargs:
            # Additional options can be included under 'options'
            payload["options"] = {key: value for key, value in kwargs.items()}

    elif target == "open-webui":
        # Open-WebUI format
        payload = {
            "model": model,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        # If needed, incorporate kwargs into 'payload' or a 'parameters' sub-dict

    else:
        print(f"!!ERROR!! Unknown target: {target}")
    return payload

def model_req(payload=None):
    """
    Send the request to the model server and return the response.

    :param payload: (dict) A payload dict as created by create_payload().
    :return:        (tuple) (delta_time, result_str)
                    - delta_time (float): Time taken for the request, or -1 if there's an error.
                    - result_str (str): The text response or an error message.
    """
    # Attempt to load config (URL, API_KEY, etc.)
    try:
        load_config()
    except Exception as e:
        return -1, f"!!ERROR!! Problem loading prompt-eng/_config. Exception: {e}"

    # Retrieve server URL and optional API key from environment
    url = os.getenv('URL_GENERATE', None)
    api_key = os.getenv('API_KEY', None)
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    print("Payload:", payload)

    # Make the request
    try:
        start_time = time.time()
        response = requests.post(url, data=json.dumps(payload) if payload else None, headers=headers)
        delta = time.time() - start_time
    except Exception as e:
        return -1, f"!!ERROR!! Request failed! Check config URL({url}). Exception: {e}"

    if response is None:
        return -1, "!!ERROR!! There was no response."
    
    # Handle HTTP status codes
    if response.status_code == 200:
        delta = round(delta, 3)
        response_json = response.json()

        # Distinguish response formats
        if 'response' in response_json:  # Possibly Ollama
            result = response_json['response']
        elif 'choices' in response_json: # Possibly Open-WebUI
            result = response_json['choices'][0]['message']['content']
        else:
            # Return the entire JSON if it doesn't match expected keys
            result = response_json

        return delta, result

    elif response.status_code == 401:
        return -1, f"!!ERROR!! Authentication issue. Check your API_KEY for URL({url})."

    else:
        return -1, f"!!ERROR!! HTTP Response={response.status_code}, {response.text}"

#
# DEBUG MAIN
#
if __name__ == "__main__":
    # Simple debug usage example
    MESSAGE = "1 + 1"
    PROMPT = MESSAGE
    payload = create_payload(
        target="open-webui",
        model="Llama-3.2-3B-Instruct",
        prompt=PROMPT,
        temperature=1.0,
        num_ctx=5555555,
        num_predict=1
    )

    time_taken, response_str = model_req(payload=payload)
    print(response_str)
    if time_taken != -1:
        print(f"Time taken: {time_taken}s")

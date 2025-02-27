![GenI-Banner](https://github.com/genilab-fau/genial-fau.github.io/blob/8f1a2d3523f879e1082918c7bba19553cb6e7212/images/geni-lab-banner.png?raw=true)

# Developing an Automated GitHub Markdown Report Using Notebooks

A study on optimizing automated report generation using different prompt engineering techniques and AI models, integrating it as a core functionality within the Career Study Mentor Bot for project planning and structured reporting.

- Authors: Nitheesh Donepudi
- Academic Supervisor: [Dr. Fernando Koch](http://www.fernandokoch.me/)

# Research Question

How do different automation prompt engineering techniques and AI models compare in terms of efficiency, accuracy, and reliability for generating automated GitHub markdown reports using Jupyter Notebooks, and how can this be seamlessly integrated into an AI-driven project planning and reporting system?

## Arguments

### What is already known about this topic

- AI models can generate structured text using prompt engineering techniques.
- Different prompt designs influence the accuracy and relevance of the generated content.
- Automating report generation can streamline documentation and workflow efficiency.
- AI-driven project management tools benefit from structured reporting capabilities.

### What this research is exploring

- We employ various AI models and prompt engineering techniques to generate structured reports in GitHub.
- We are building an experimental framework to evaluate different automation approaches through testing models, parameters, and temperature variations.
- We are exploring trade-offs between processing speed, content quality, and parameter optimization.
- We integrate markdown report generation into the Career Study Mentor Bot, enhancing its functionality as a project planner and structured reporting assistant.

### Implications for practice

- It will be easier to automate structured documentation processes for software projects and project planning.
- It will optimize markdown report generation for various AI-driven workflows.
- We will better understand the impact of prompt tuning and model selection on automated documentation.
- AI-assisted project planning will gain a structured reporting mechanism within the Career Study Mentor Bot.

# Research Method

We conducted a comparative study by designing controlled experiments to test different AI models and prompting strategies for GitHub markdown report generation. Evaluation criteria include response latency, content structure, and adherence to formatting requirements.

**Experimental Objectives**

- **Behavior Analysis:** Evaluate how consistently each technique follows prompt instructions.
- **Performance Metrics:** Compare response times (latency) and computational overhead.
- **Effectiveness:** Assess the accuracy, readability, and Markdown formatting of generated reports.

**Testing AI Models and Prompt Engineering Approaches**

We explored multiple prompting strategies with different AI models to determine the best automation structure for report generation and its integration into project planning tools.

- **Level-1 Automation:** A single well-structured prompt directly generates the markdown report.
- **Level-2 Automation:** A multi-step approach where the AI refines the structure before generating the final report.
- **Multi-Model Comparison:** Testing multiple AI models (e.g., GPT-4, LLaMA, Qwen) with different parameter settings to analyze performance variations.

**Observations:**

- **Latency:** Faster response times with simpler prompts; increased latency with multi-step techniques.
- **Accuracy:** Higher accuracy observed with multi-step refinement.
- **Effectiveness:** Better markdown structure and clarity using models optimized for structured output.
- **Limitations:** Higher temperature settings can introduce variability in formatting consistency.

# Experimental Setup

**Matching Models to Report Sections**

- **Project Overview:** Llama-3.2-3B-Instruct or Qwen2 for coherent summaries and structured text.
- **Data & Methodologies:** Mistral-large or Gemma2 for detailed descriptions.
- **Results & Evaluation:** Qwen2 or Microsoft/phi-4 for structured metric analysis.
- **Discussion & Future Work:** Gemma2 or Llama-3.2-11B-Vision-Instruct for expanded reasoning.
- **Project Setup & Usage:** Codestral or Tinyllama for structured documentation and instructions.
- **Appendices:** Codestral for code snippets and Qwen2 for textual expansions.

**Pipeline Workflow**

1. **Gather Inputs:** Using Jupyter notebooks to collect details.
2. **Baseline Prompting (Zero-Shot):** Rough draft generation.
3. **Refinement (Few-Shot):** Improved structuring with example prompts.
4. **Deep Reasoning:** Chain-of-thought expansions.
5. **Self-Consistency Checks:** Refinement loops to detect inconsistencies.
6. **Assembly & Formatting:** Combining sections into a final markdown report.
7. **Integration:** Embedding the report generator into the Career Study Mentor Bot.

**Evaluation Metrics**

- **Response Time:** Measured round-trip latency for each technique.
- **Content Quality:** Manually assessed for completeness, clarity, markdown compliance, and adherence to reporting guidelines.
- **Error Rate:** Documented instances of formatting issues, ambiguity, or failure to generate key sections.

# Results

Our findings indicate that:

- **Level-1 automation excels in speed** but may lack refinement in structuring markdown reports.
- **Level-2 automation provides a more structured and formatted output** but requires additional processing time.
- **AI model selection significantly impacts the final output quality**, with some models better suited for markdown-specific formatting.

| Technique | Average Latency | Accuracy (Subjective Rating) | Strengths | Limitations |
| --- | --- | --- | --- | --- |
| Level-1 | Fast (Low ms) | 7/10 | Quick response, simplicity | Formatting inconsistencies in complex reports |
| Level-2 | Moderate (Higher ms) | 9/10 | Well-structured, refined output | Increased latency, requires tuning |
| Multi-Model Comparison | Varies across models | 8-10/10 | Some models excel in markdown formatting | Requires benchmarking for best performance |

# Further Research

Future studies can focus on:

- Developing automated correction mechanisms for markdown formatting inconsistencies.
- Exploring model-specific optimization techniques for report generation.
- Evaluating performance trade-offs when integrating markdown reports into continuous integration (CI) workflows.
- Investigating reinforcement learning approaches to fine-tune prompt effectiveness over iterative AI feedback cycles.
- Integrating the markdown report automation system with the Career Study Mentor Bot to enhance its functionality as a project planner and automated report generator.
- Enhancing AI-driven project tracking by utilizing markdown-based structured reporting within the bot framework.

This research provides valuable insights into how AI-powered automation can enhance structured documentation and workflow automation in software projects, with a focus on markdown report generation for GitHub repositories and AI-driven career study mentorship systems.
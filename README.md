# AI Research and Speech Generation

This project utilizes **CrewAI** to automate research and speech generation on Generative AI. It leverages language models and tools to perform web searches and craft engaging speeches based on research findings.

## 📦 Libraries Used
- **CrewAI** - For managing AI agents and tasks
- **SerperDevTool** - For performing internet searches
- **Ollama** - As the LLM provider (model: `llama3.2`)

## 🚀 How It Works
1. A **Senior AI Researcher** agent searches for the latest AI research using `SerperDevTool`.
2. The findings are compiled into a structured summary.
3. A **Senior Speech Writer** agent crafts a keynote speech based on the research.
4. The results are stored in output files.

## 📜 Output Files
- `task1output.txt` - Research summary
- `task2output.txt` - Generated keynote speech

## 🛠️ Running the Project
Ensure you have Python 3.8 - 3.12 installed and activate the virtual environment:
```sh
source venv_agents/bin/activate  # macOS/Linux
venv_agents\Scripts\activate  # Windows
```
Install dependencies:
```sh
pip install -r requirements.txt
```
Run the script:
```sh
python app.py
```

## 📌 Notes
- Ensure `SERPER_API_KEY` is set in your environment.
- Ollama should be running locally at `http://localhost:11434`.

Enjoy exploring AI-powered research and speech writing! 🚀

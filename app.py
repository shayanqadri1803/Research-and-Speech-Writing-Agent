import os
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI

os.getenv('SERPER_API_KEY')

llm = LLM(model="ollama/llama3.2", base_url="http://localhost:11434")
function_calling_llm = LLM(model="ollama/llama3.2", base_url="http://localhost:11434")

search = SerperDevTool()

# Create the agent
researcher = Agent(
    llm=llm,
    function_calling_llm=function_calling_llm,
    role="Senior AI Researcher",
    goal="Find promising research in the field of Gen AI.",
    backstory="You are a veteran AI researcher with a background in Generative AI.",
    allow_delegation=False,
    tools=[search],
    verbose=1,
)

# Create a task
task1 = Task(
    description="Search the internet and find 5 examples of promising AI research along with use cases.",
    expected_output="A detailed bullet point summary on each of the topics. Each bullet point should cover the topic, background and why the innovation is useful.",
    output_file="task1output.txt",
    agent=researcher,
)

# Create the second agent
writer = Agent(
    llm=llm,
    role="Senior Speech Writer",
    goal="Write engaging and witty keynote speeches from provided research.",
    backstory="You are a veteran AI writer with a background in Generative AI",
    allow_delegation=False,
    verbose=1,
)

# Create a task
task2 = Task(
    description="Write an engaging keynote speech on Generative AI and its use cases.",
    expected_output="A detailed keynote speech with an intro, body and conclusion.",
    output_file="task2output.txt",
    agent=writer,
)

# Put all together with the crew
crew = Crew(agents=[researcher, writer], tasks=[task1, task2], verbose=1)
print(crew.kickoff())
# in crewai two ways we can able to create the agents and tasks
# 1).normal way Agent,Task we directly design agents
# 2).using yaml file we can create agent and task in documentation 
# they are suggesting to use this technique

# src/latest_ai_development/crew.py
import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

# The names you use in your YAML files (agents.yaml and tasks.yaml) 
# should match the method names in your Python code.

@CrewBase
class LatestAiDevelopmentCrew():
  """LatestAiDevelopment crew"""

  agents_config = "agents.yaml"
  tasks_config = "tasks.yaml"

  llm = LLM(model="groq/llama-3.3-70b-versatile", temperature=0.5)

  @agent
  def researcher(self) -> Agent:
    return Agent(
      config=self.agents_config['researcher'], # type: ignore[index]
      verbose=True,
      tools=[SerperDevTool()],
      llm=self.llm
    )

  @task
  def researcher_tasks(self) -> Task:
    return Task(
      config=self.tasks_config['researcher_tasks'] # type: ignore[index]
    )

  @crew
  def crew(self) -> Crew:
    return Crew(
      agents=[self.researcher()],
      tasks=[self.researcher_tasks()],
      verbose = True
    )
  
if __name__ == "__main__":
  crew = LatestAiDevelopmentCrew().crew()
  result = crew.kickoff(inputs={"topic": "What are the latest developments in AI?"})
  print(result)
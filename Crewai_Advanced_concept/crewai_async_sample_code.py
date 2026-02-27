import asyncio
from crewai import Crew, Agent, Task

# Agent that writes blog posts
writer_agent = Agent(
    role="Blog Writer",
    goal="Write engaging blog posts on given topics",
    backstory="You are a professional content writer with 10 years of experience."
)

# Task 1: Tech blog
tech_task = Task(
    description="Write a short blog post about: {topic}",
    agent=writer_agent,
    expected_output="A 3-paragraph blog post."
)

# Task 2: Health blog
health_task = Task(
    description="Write a short blog post about: {topic}",
    agent=writer_agent,
    expected_output="A 3-paragraph blog post."
)

tech_crew   = Crew(agents=[writer_agent], tasks=[tech_task])
health_crew = Crew(agents=[writer_agent], tasks=[health_task])

async def main():
    # Both crews run at the SAME TIME — no waiting!
    results = await asyncio.gather(
        tech_crew.akickoff(inputs={"topic": "Future of AI in 2025"}),
        health_crew.akickoff(inputs={"topic": "Benefits of Morning Exercise"})
    )

    for i, result in enumerate(results, 1):
        print(f"\n--- Blog {i} ---\n{result}")

asyncio.run(main())
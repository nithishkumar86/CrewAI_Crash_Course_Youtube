research_agent = Agent(
    role="Research Analyst",
    goal="Find and summarize information about specific topics",
    # llm= groq,gemini,openai,claude,ollama
    backstory="You are an experienced researcher with attention to detail",
    tools=[SerperDevTool(),tavily,serper], #enable tool calls
    verbose=True  # Enable logging for debugging
)

dev_agent = Agent(
    role="Senior Python Developer",
    goal="Write and debug Python code",
    backstory="Expert Python developer with 10 years of experience",
    allow_code_execution=True, 
    code_execution_mode="safe",  # Uses Docker for safety
    max_execution_time=300,  # 5-minute timeout
    max_retry_limit=3  # More retries for complex code tasks
)


analysis_agent = Agent(
    role="Data Analyst",
    goal="Perform deep analysis of large datasets",
    backstory="Specialized in big data analysis and pattern recognition",
    memory=True, #memory: Enable to maintain conversation history
    respect_context_window=True, 
    # Keep messages under context window size by summarizing. Default is True.
    max_rpm=10,  # Limit API calls
    function_calling_llm="gpt-4o-mini"  # Cheaper model for tool calls
)

reasoning_agent = Agent(
    role="Strategic Planner",
    goal="Analyze complex problems and create detailed execution plans",
    backstory="Expert strategic planner who methodically breaks down complex challenges",
    reasoning=True,  # Enable reasoning and planning
    max_reasoning_attempts=3,  # Limit reasoning attempts
    max_iter=30,  # Allow more iterations for complex planning
    verbose=True  #Enable detailed execution logs for debugging. Default is False.
)


multimodal_agent = Agent(
    role="Visual Content Analyst",
    goal="Analyze and process both text and visual content",
    backstory="Specialized in multimodal analysis combining text and image understanding",
    multimodal=True,  # Enable multimodal capabilities
    verbose=True
)

custom_agent = Agent(
    role="Customer Service Representative",
    goal="Assist customers with their inquiries",
    backstory="Experienced in customer support with a focus on satisfaction",
    system_template="""<|start_header_id|>system<|end_header_id|>
                        {{ .System }}<|eot_id|>""",
    prompt_template="""<|start_header_id|>user<|end_header_id|>
                        {{ .Prompt }}<|eot_id|>""",
    response_template="""<|start_header_id|>assistant<|end_header_id|>
                        {{ .Response }}<|eot_id|>""",
)


# Use knowledge sources instead of large prompts
knowledge_agent = Agent(
    role="Knowledge Expert",
    goal="Answer questions using curated knowledge",
    backstory="Expert at leveraging structured knowledge sources",
    knowledge_sources=[your_knowledge_sources],  # knowledge_sources: Add domain-specific knowledge bases
    respect_context_window=True,
    verbose=True
)

knowledge_source = """

Knowledge in CrewAI is a powerful system that allows AI agents to access and utilize external information sources during their tasks. Think of it as giving your agents a reference library they can consult while working.

Text Sources
Raw strings
Text files (.txt)
PDF documents
Structured Data
CSV files
Excel spreadsheets
JSON documents
"""


from crewai import Agent
from crewai_tools import SerperDevTool

# Create an agent
researcher = Agent(
    role="AI Technology Researcher",
    goal="Research the latest AI developments",
    tools=[SerperDevTool()],
    verbose=True
)

# Use kickoff() to interact directly with the agent
result = researcher.kickoff("What are the latest developments in language models?")

# Access the raw response
print(result.raw)
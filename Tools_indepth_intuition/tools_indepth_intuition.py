{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "fa4d6b32",
   "metadata": {},
   "source": [
    "# tools\n",
    "\n",
    "A tool in CrewAI is a skill or function that agents can utilize to perform various actions.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
<<<<<<< HEAD
   "execution_count": 1,
=======
   "execution_count": 17,
>>>>>>> e2d7c88740d591c92e932021da34044ceb269199
   "id": "92b23974",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
<<<<<<< HEAD
     "execution_count": 1,
=======
     "execution_count": 17,
>>>>>>> e2d7c88740d591c92e932021da34044ceb269199
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "from dotenv import load_dotenv # help us to load .env variable to the current working file\n",
    "load_dotenv()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3c7136b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "from crewai import Task,Agent,LLM,Crew\n",
    "from crewai.tools import tool #creating custom tool it is required one\n",
    "from crewai_tools import TavilySearchTool # web search extract,search\n",
    "from crewai_tools import FirecrawlScrapeWebsiteTool # extract the context from specific website"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "d988c723",
   "metadata": {},
   "outputs": [],
   "source": [
    "#llm Initialization\n",
    " \n",
    "llm = LLM(\n",
    "    model=\"groq/llama-3.3-70b-versatile\",  #llama-3.1-8b-instant\n",
    "    temperature=0.2 # for output \n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "83641186",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initialize the tool\n",
    "tavily_tool = TavilySearchTool(max_results = 4,search_depth = 'advanced')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "718b70a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create an agent with clear instructions\n",
    "researcher = Agent(\n",
    "    role='Market Researcher with Specialist in Market Trends',\n",
    "    goal='Identify the top 3 most impactful AI trends from 2026 based on industry adoption and innovation.',\n",
    "    backstory='Senior technology analyst with 10 years of experience tracking AI industry developments and emerging technologies.',\n",
    "    llm = llm,\n",
    "    tools=[tavily_tool],\n",
    "    verbose=True, # logs\n",
    "    max_tokens=500 # to restricct the token limit\n",
    ")\n",
    "\n",
    "# Create a task with specific requirements\n",
    "research_task = Task(\n",
    "    description=\"\"\"\n",
    "    Search for and identify the top 3 AI trends from 2026.\n",
    "    \n",
    "    Steps:\n",
    "    1. Use Tavily to search \"top AI trends 2026\"\n",
    "    2. Select top 3 trends based on industry impact and adoption\n",
    "    3. Summarize each trend in 2-3 sentences\n",
    "    4. Keep total response under 500 tokens\n",
    "    \"\"\",\n",
    "    expected_output='A concise report listing the top 3 AI trends from 2026, with each trend including its name, a brief description, and why it matters. Maximum 500 tokens total.',\n",
    "    agent=researcher\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "5f903722",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Form the crew and kick it off\n",
    "crew = Crew(\n",
    "    agents=[researcher],\n",
    "    tasks=[research_task],\n",
    "    verbose=True \n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3be30478",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008080; text-decoration-color: #008080\">╭─────────────────────────────────────────── 🚀 Crew Execution Started ───────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>                                                                                                                 <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #008080; text-decoration-color: #008080; font-weight: bold\">Crew Execution Started</span>                                                                                         <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Name: </span>                                                                                                         <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #008080; text-decoration-color: #008080\">crew</span>                                                                                                           <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">ID: </span>                                                                                                           <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #008080; text-decoration-color: #008080\">1ebf5d72-f650-4ce9-bbd5-fa0e040e071c</span>                                                                           <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>                                                                                                                 <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>                                                                                                                 <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[36m╭─\u001b[0m\u001b[36m──────────────────────────────────────────\u001b[0m\u001b[36m 🚀 Crew Execution Started \u001b[0m\u001b[36m──────────────────────────────────────────\u001b[0m\u001b[36m─╮\u001b[0m\n",
       "\u001b[36m│\u001b[0m                                                                                                                 \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[1;36mCrew Execution Started\u001b[0m                                                                                         \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[37mName: \u001b[0m                                                                                                         \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[36mcrew\u001b[0m                                                                                                           \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[37mID: \u001b[0m                                                                                                           \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[36m1ebf5d72-f650-4ce9-bbd5-fa0e040e071c\u001b[0m                                                                           \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m                                                                                                                 \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m                                                                                                                 \u001b[36m│\u001b[0m\n",
       "\u001b[36m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #808000; text-decoration-color: #808000\">╭──────────────────────────────────────────────── 📋 Task Started ────────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000; font-weight: bold\">Task Started</span>                                                                                                   <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Name: </span>                                                                                                         <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    Search for and identify the top 3 AI trends from 2026.</span>                                                     <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    Steps:</span>                                                                                                     <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    1. Use Tavily to search \"top AI trends 2026\"</span>                                                               <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    2. Select 3 trends based on industry impact and adoption</span>                                                   <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    3. Summarize each trend in 2-3 sentences</span>                                                                   <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    4. Keep total response under 500 tokens</span>                                                                    <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    </span>                                                                                                           <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">ID: </span><span style=\"color: #808000; text-decoration-color: #808000\">0fa02651-6b64-4926-8576-e73c82bdfc4b</span>                                                                       <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[33m╭─\u001b[0m\u001b[33m───────────────────────────────────────────────\u001b[0m\u001b[33m 📋 Task Started \u001b[0m\u001b[33m───────────────────────────────────────────────\u001b[0m\u001b[33m─╮\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[1;33mTask Started\u001b[0m                                                                                                   \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[37mName: \u001b[0m                                                                                                         \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    Search for and identify the top 3 AI trends from 2026.\u001b[0m                                                     \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    Steps:\u001b[0m                                                                                                     \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    1. Use Tavily to search \"top AI trends 2026\"\u001b[0m                                                               \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    2. Select 3 trends based on industry impact and adoption\u001b[0m                                                   \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    3. Summarize each trend in 2-3 sentences\u001b[0m                                                                   \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    4. Keep total response under 500 tokens\u001b[0m                                                                    \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    \u001b[0m                                                                                                           \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[37mID: \u001b[0m\u001b[33m0fa02651-6b64-4926-8576-e73c82bdfc4b\u001b[0m                                                                       \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #800080; text-decoration-color: #800080\">╭─────────────────────────────────────────────── 🤖 Agent Started ────────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>                                                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Agent: </span><span style=\"color: #00ff00; text-decoration-color: #00ff00; font-weight: bold\">Market Researcher with Specialist in Market Trends</span>                                                      <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>                                                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Task: </span>                                                                                                         <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    Search for and identify the top 3 AI trends from 2026.</span>                                                     <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>                                                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    Steps:</span>                                                                                                     <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    1. Use Tavily to search \"top AI trends 2026\"</span>                                                               <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    2. Select 3 trends based on industry impact and adoption</span>                                                   <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    3. Summarize each trend in 2-3 sentences</span>                                                                   <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    4. Keep total response under 500 tokens</span>                                                                    <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    </span>                                                                                                           <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>                                                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[35m╭─\u001b[0m\u001b[35m──────────────────────────────────────────────\u001b[0m\u001b[35m 🤖 Agent Started \u001b[0m\u001b[35m───────────────────────────────────────────────\u001b[0m\u001b[35m─╮\u001b[0m\n",
       "\u001b[35m│\u001b[0m                                                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[37mAgent: \u001b[0m\u001b[1;92mMarket Researcher with Specialist in Market Trends\u001b[0m                                                      \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m                                                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[37mTask: \u001b[0m                                                                                                         \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    Search for and identify the top 3 AI trends from 2026.\u001b[0m                                                     \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m                                                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    Steps:\u001b[0m                                                                                                     \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    1. Use Tavily to search \"top AI trends 2026\"\u001b[0m                                                               \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    2. Select 3 trends based on industry impact and adoption\u001b[0m                                                   \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    3. Summarize each trend in 2-3 sentences\u001b[0m                                                                   \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    4. Keep total response under 500 tokens\u001b[0m                                                                    \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    \u001b[0m                                                                                                           \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m                                                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008000; text-decoration-color: #008000\">╭───────────────────────────────────────────── ✅ Agent Final Answer ─────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Agent: </span><span style=\"color: #00ff00; text-decoration-color: #00ff00; font-weight: bold\">Market Researcher with Specialist in Market Trends</span>                                                      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Final Answer:</span>                                                                                                  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">The top 3 AI trends from 2026 are:</span>                                                                             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">1. **Foundational AI Principles**: Foundational AI principles will rewrite organizational DNA, informing AI </span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">strategies and addressing AI risks. This trend matters because it will help organizations establish a solid </span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">foundation for their AI initiatives, ensuring that they are aligned with their strategic goals and values. By</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">adopting foundational AI principles, organizations can mitigate AI risks and drive business value.</span>             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">2. **Agentic AI**: Agentic AI will increase in adoption and enable outcomes across the organization, powering</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">exponential growth and change. It will transform AI from a passive assistant into an active collaborator </span>      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">capable of meaningful problem-solving and decision-making. This trend matters because it will revolutionize </span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">the way businesses operate and make decisions, enabling them to stay ahead of the competition and drive </span>       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">innovation.</span>                                                                                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">3. **Quantum AI**: Quantum AI has the potential to solve complex problems that are currently unsolvable with </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">traditional computers, driving breakthroughs in fields such as medicine, finance, and climate modeling. This </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">trend matters because it will enable organizations to tackle some of the world's most pressing challenges, </span>    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">leading to significant advancements in various industries and improving the quality of life for people around</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">the world. By leveraging quantum AI, organizations can unlock new possibilities and create new opportunities </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">for growth and innovation.</span>                                                                                     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[32m╭─\u001b[0m\u001b[32m────────────────────────────────────────────\u001b[0m\u001b[32m ✅ Agent Final Answer \u001b[0m\u001b[32m────────────────────────────────────────────\u001b[0m\u001b[32m─╮\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mAgent: \u001b[0m\u001b[1;92mMarket Researcher with Specialist in Market Trends\u001b[0m                                                      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mFinal Answer:\u001b[0m                                                                                                  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mThe top 3 AI trends from 2026 are:\u001b[0m                                                                             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92m1. **Foundational AI Principles**: Foundational AI principles will rewrite organizational DNA, informing AI \u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mstrategies and addressing AI risks. This trend matters because it will help organizations establish a solid \u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mfoundation for their AI initiatives, ensuring that they are aligned with their strategic goals and values. By\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92madopting foundational AI principles, organizations can mitigate AI risks and drive business value.\u001b[0m             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92m2. **Agentic AI**: Agentic AI will increase in adoption and enable outcomes across the organization, powering\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mexponential growth and change. It will transform AI from a passive assistant into an active collaborator \u001b[0m      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mcapable of meaningful problem-solving and decision-making. This trend matters because it will revolutionize \u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mthe way businesses operate and make decisions, enabling them to stay ahead of the competition and drive \u001b[0m       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92minnovation.\u001b[0m                                                                                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92m3. **Quantum AI**: Quantum AI has the potential to solve complex problems that are currently unsolvable with \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mtraditional computers, driving breakthroughs in fields such as medicine, finance, and climate modeling. This \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mtrend matters because it will enable organizations to tackle some of the world's most pressing challenges, \u001b[0m    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mleading to significant advancements in various industries and improving the quality of life for people around\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mthe world. By leveraging quantum AI, organizations can unlock new possibilities and create new opportunities \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mfor growth and innovation.\u001b[0m                                                                                     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008000; text-decoration-color: #008000\">╭────────────────────────────────────────────── 📋 Task Completion ───────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000; font-weight: bold\">Task Completed</span>                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Name: </span>                                                                                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    Search for and identify the top 3 AI trends from 2026.</span>                                                     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    Steps:</span>                                                                                                     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    1. Use Tavily to search \"top AI trends 2026\"</span>                                                               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    2. Select 3 trends based on industry impact and adoption</span>                                                   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    3. Summarize each trend in 2-3 sentences</span>                                                                   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    4. Keep total response under 500 tokens</span>                                                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    </span>                                                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Agent: </span>                                                                                                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Market Researcher with Specialist in Market Trends</span>                                                             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[32m╭─\u001b[0m\u001b[32m─────────────────────────────────────────────\u001b[0m\u001b[32m 📋 Task Completion \u001b[0m\u001b[32m──────────────────────────────────────────────\u001b[0m\u001b[32m─╮\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[1;32mTask Completed\u001b[0m                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mName: \u001b[0m                                                                                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    Search for and identify the top 3 AI trends from 2026.\u001b[0m                                                     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    Steps:\u001b[0m                                                                                                     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    1. Use Tavily to search \"top AI trends 2026\"\u001b[0m                                                               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    2. Select 3 trends based on industry impact and adoption\u001b[0m                                                   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    3. Summarize each trend in 2-3 sentences\u001b[0m                                                                   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    4. Keep total response under 500 tokens\u001b[0m                                                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    \u001b[0m                                                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mAgent: \u001b[0m                                                                                                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mMarket Researcher with Specialist in Market Trends\u001b[0m                                                             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008000; text-decoration-color: #008000\">╭──────────────────────────────────────────────── Crew Completion ────────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000; font-weight: bold\">Crew Execution Completed</span>                                                                                       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Name: </span>                                                                                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">crew</span>                                                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">ID: </span>                                                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">1ebf5d72-f650-4ce9-bbd5-fa0e040e071c</span>                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Final Output: The top 3 AI trends from 2026 are:</span>                                                               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">1. **Foundational AI Principles**: Foundational AI principles will rewrite organizational DNA, informing AI </span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">strategies and addressing AI risks. This trend matters because it will help organizations establish a solid </span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">foundation for their AI initiatives, ensuring that they are aligned with their strategic goals and values. By</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">adopting foundational AI principles, organizations can mitigate AI risks and drive business value.</span>             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">2. **Agentic AI**: Agentic AI will increase in adoption and enable outcomes across the organization, powering</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">exponential growth and change. It will transform AI from a passive assistant into an active collaborator </span>      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">capable of meaningful problem-solving and decision-making. This trend matters because it will revolutionize </span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">the way businesses operate and make decisions, enabling them to stay ahead of the competition and drive </span>       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">innovation.</span>                                                                                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">3. **Quantum AI**: Quantum AI has the potential to solve complex problems that are currently unsolvable with </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">traditional computers, driving breakthroughs in fields such as medicine, finance, and climate modeling. This </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">trend matters because it will enable organizations to tackle some of the world's most pressing challenges, </span>    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">leading to significant advancements in various industries and improving the quality of life for people around</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">the world. By leveraging quantum AI, organizations can unlock new possibilities and create new opportunities </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">for growth and innovation.</span>                                                                                     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[32m╭─\u001b[0m\u001b[32m───────────────────────────────────────────────\u001b[0m\u001b[32m Crew Completion \u001b[0m\u001b[32m───────────────────────────────────────────────\u001b[0m\u001b[32m─╮\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[1;32mCrew Execution Completed\u001b[0m                                                                                       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mName: \u001b[0m                                                                                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mcrew\u001b[0m                                                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mID: \u001b[0m                                                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m1ebf5d72-f650-4ce9-bbd5-fa0e040e071c\u001b[0m                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mFinal Output: The top 3 AI trends from 2026 are:\u001b[0m                                                               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37m1. **Foundational AI Principles**: Foundational AI principles will rewrite organizational DNA, informing AI \u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mstrategies and addressing AI risks. This trend matters because it will help organizations establish a solid \u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mfoundation for their AI initiatives, ensuring that they are aligned with their strategic goals and values. By\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37madopting foundational AI principles, organizations can mitigate AI risks and drive business value.\u001b[0m             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37m2. **Agentic AI**: Agentic AI will increase in adoption and enable outcomes across the organization, powering\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mexponential growth and change. It will transform AI from a passive assistant into an active collaborator \u001b[0m      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mcapable of meaningful problem-solving and decision-making. This trend matters because it will revolutionize \u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mthe way businesses operate and make decisions, enabling them to stay ahead of the competition and drive \u001b[0m       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37minnovation.\u001b[0m                                                                                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37m3. **Quantum AI**: Quantum AI has the potential to solve complex problems that are currently unsolvable with \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mtraditional computers, driving breakthroughs in fields such as medicine, finance, and climate modeling. This \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mtrend matters because it will enable organizations to tackle some of the world's most pressing challenges, \u001b[0m    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mleading to significant advancements in various industries and improving the quality of life for people around\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mthe world. By leveraging quantum AI, organizations can unlock new possibilities and create new opportunities \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mfor growth and innovation.\u001b[0m                                                                                     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The top 3 AI trends from 2026 are:\n",
      "\n",
      "1. **Foundational AI Principles**: Foundational AI principles will rewrite organizational DNA, informing AI strategies and addressing AI risks. This trend matters because it will help organizations establish a solid foundation for their AI initiatives, ensuring that they are aligned with their strategic goals and values. By adopting foundational AI principles, organizations can mitigate AI risks and drive business value.\n",
      "\n",
      "2. **Agentic AI**: Agentic AI will increase in adoption and enable outcomes across the organization, powering exponential growth and change. It will transform AI from a passive assistant into an active collaborator capable of meaningful problem-solving and decision-making. This trend matters because it will revolutionize the way businesses operate and make decisions, enabling them to stay ahead of the competition and drive innovation.\n",
      "\n",
      "3. **Quantum AI**: Quantum AI has the potential to solve complex problems that are currently unsolvable with traditional computers, driving breakthroughs in fields such as medicine, finance, and climate modeling. This trend matters because it will enable organizations to tackle some of the world's most pressing challenges, leading to significant advancements in various industries and improving the quality of life for people around the world. By leveraging quantum AI, organizations can unlock new possibilities and create new opportunities for growth and innovation.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #000080; text-decoration-color: #000080\">╭──────────────────────────────────────────────── Tracing Status ─────────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>                                                                                                                 <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  Info: Tracing is disabled.                                                                                     <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>                                                                                                                 <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  To enable tracing, do any one of these:                                                                        <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  • Set tracing=True in your Crew/Flow code                                                                      <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  • Set CREWAI_TRACING_ENABLED=true in your project's .env file                                                  <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  • Run: crewai traces enable                                                                                    <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>                                                                                                                 <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[34m╭─\u001b[0m\u001b[34m───────────────────────────────────────────────\u001b[0m\u001b[34m Tracing Status \u001b[0m\u001b[34m────────────────────────────────────────────────\u001b[0m\u001b[34m─╮\u001b[0m\n",
       "\u001b[34m│\u001b[0m                                                                                                                 \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  Info: Tracing is disabled.                                                                                     \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m                                                                                                                 \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  To enable tracing, do any one of these:                                                                        \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  • Set tracing=True in your Crew/Flow code                                                                      \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  • Set CREWAI_TRACING_ENABLED=true in your project's .env file                                                  \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  • Run: crewai traces enable                                                                                    \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m                                                                                                                 \u001b[34m│\u001b[0m\n",
       "\u001b[34m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "\u001b[36m┌─\u001b[0m\u001b[36m────────────────────────────\u001b[0m\u001b[36m \u001b[0m\u001b[1;36mExecution Traces\u001b[0m\u001b[36m \u001b[0m\u001b[36m─────────────────────────────\u001b[0m\u001b[36m─┐\u001b[0m\n",
      "\u001b[36m│\u001b[0m                                                                             \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[1;36m🔍 \u001b[0m\u001b[1;36mDetailed execution traces are available!\u001b[0m                                \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m                                                                             \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[37mView insights including:\u001b[0m                                                   \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[94m  • Agent decision-making process\u001b[0m                                          \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[94m  • Task execution flow and timing\u001b[0m                                         \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[94m  • Tool usage details\u001b[0m                                                     \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m                                                                             \u001b[36m│\u001b[0m\n",
      "\u001b[36m└─────────────────────────────────────────────────────────────────────────────┘\u001b[0m\n",
      "Would you like to view your execution traces? [y/N] (20s timeout): \n",
      "\n",
      "\u001b[34m┌─\u001b[0m\u001b[34m────────────────────────\u001b[0m\u001b[34m Tracing Preference Saved \u001b[0m\u001b[34m─────────────────────────\u001b[0m\u001b[34m─┐\u001b[0m\n",
      "\u001b[34m│\u001b[0m                                                                             \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  Info: Tracing has been disabled.                                           \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m                                                                             \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  Your preference has been saved. Future Crew/Flow executions will not       \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  collect traces.                                                            \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m                                                                             \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  To enable tracing later, do any one of these:                              \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  • Set tracing=True in your Crew/Flow code                                  \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  • Set CREWAI_TRACING_ENABLED=true in your project's .env file              \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  • Run: crewai traces enable                                                \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m                                                                             \u001b[34m│\u001b[0m\n",
      "\u001b[34m└─────────────────────────────────────────────────────────────────────────────┘\u001b[0m\n",
      "\n"
     ]
    }
   ],
   "source": [
    "result = crew.kickoff()\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d8fc8e78",
   "metadata": {},
   "source": [
    "# second Example of Inbuilt Tools"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "a5a52408",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "from dotenv import load_dotenv\n",
    "load_dotenv()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "247670bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initialize the tool\n",
    "firecrawl_tool = FirecrawlScrapeWebsiteTool(page_options='onlyMainContent',extractor_options=\"don't extract url or https extract main content\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "09515660",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create an agent with clear instructions\n",
    "content_analyst = Agent(\n",
    "    role='Website Content Analyst',\n",
    "    goal='Extract and analyze key information from the given url including features, pricing, and use cases.',\n",
    "    backstory='Experienced web content analyst specializing in technical documentation and product analysis for developer tools.',\n",
    "    llm = llm,\n",
    "    tools=[firecrawl_tool],\n",
    "    verbose=True,\n",
    "    max_tokens=500\n",
    ")\n",
    "\n",
    "# Create a task with specific requirements\n",
    "scrape_task = Task(\n",
    "    description=\"\"\"\n",
    "    Scrape and analyze the given url\n",
    "\n",
    "    url : {url} #optinal\n",
    "    \n",
    "    Steps:\n",
    "    1. Use FirecrawlScrapeWebsiteTool to scrape the url\n",
    "    2. Extract main product features and capabilities\n",
    "    3. Identify pricing information if available\n",
    "    4. Note primary use cases or target audience\n",
    "    5. Keep total response under 500 tokens\n",
    "    \"\"\",\n",
    "    expected_output='A concise summary of the url covering: what the product does, main features, pricing (if found), and target users. Maximum 500 tokens total.',\n",
    "    agent=content_analyst\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "59e2e418",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    crew = Crew(\n",
    "        agents = [content_analyst],\n",
    "        tasks = [scrape_task],\n",
    "        verbose = True\n",
    "    )\n",
    "    result = crew.kickoff(inputs={\"url\":'https://docs.crewai.com/en/introduction'})\n",
    "    return result\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "771051a7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008080; text-decoration-color: #008080\">╭─────────────────────────────────────────── 🚀 Crew Execution Started ───────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>                                                                                                                 <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #008080; text-decoration-color: #008080; font-weight: bold\">Crew Execution Started</span>                                                                                         <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Name: </span>                                                                                                         <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #008080; text-decoration-color: #008080\">crew</span>                                                                                                           <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">ID: </span>                                                                                                           <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #008080; text-decoration-color: #008080\">404c49fd-3e45-4c56-9d66-455bc0a8b83b</span>                                                                           <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>                                                                                                                 <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>                                                                                                                 <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[36m╭─\u001b[0m\u001b[36m──────────────────────────────────────────\u001b[0m\u001b[36m 🚀 Crew Execution Started \u001b[0m\u001b[36m──────────────────────────────────────────\u001b[0m\u001b[36m─╮\u001b[0m\n",
       "\u001b[36m│\u001b[0m                                                                                                                 \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[1;36mCrew Execution Started\u001b[0m                                                                                         \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[37mName: \u001b[0m                                                                                                         \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[36mcrew\u001b[0m                                                                                                           \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[37mID: \u001b[0m                                                                                                           \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[36m404c49fd-3e45-4c56-9d66-455bc0a8b83b\u001b[0m                                                                           \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m                                                                                                                 \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m                                                                                                                 \u001b[36m│\u001b[0m\n",
       "\u001b[36m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #808000; text-decoration-color: #808000\">╭──────────────────────────────────────────────── 📋 Task Started ────────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000; font-weight: bold\">Task Started</span>                                                                                                   <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Name: </span>                                                                                                         <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    Scrape and analyze the given url</span>                                                                           <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    url : https://docs.crewai.com/en/introduction</span>                                                              <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    Steps:</span>                                                                                                     <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    1. Use FirecrawlScrapeWebsiteTool to scrape the url</span>                                                        <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    2. Extract main product features and capabilities</span>                                                          <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    3. Identify pricing information if available</span>                                                               <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    4. Note primary use cases or target audience</span>                                                               <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    5. Keep total response under 500 tokens</span>                                                                    <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    </span>                                                                                                           <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">ID: </span><span style=\"color: #808000; text-decoration-color: #808000\">37a00f6b-f3ad-409d-bbc5-50d47398702b</span>                                                                       <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[33m╭─\u001b[0m\u001b[33m───────────────────────────────────────────────\u001b[0m\u001b[33m 📋 Task Started \u001b[0m\u001b[33m───────────────────────────────────────────────\u001b[0m\u001b[33m─╮\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[1;33mTask Started\u001b[0m                                                                                                   \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[37mName: \u001b[0m                                                                                                         \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    Scrape and analyze the given url\u001b[0m                                                                           \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    url : https://docs.crewai.com/en/introduction\u001b[0m                                                              \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    Steps:\u001b[0m                                                                                                     \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    1. Use FirecrawlScrapeWebsiteTool to scrape the url\u001b[0m                                                        \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    2. Extract main product features and capabilities\u001b[0m                                                          \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    3. Identify pricing information if available\u001b[0m                                                               \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    4. Note primary use cases or target audience\u001b[0m                                                               \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    5. Keep total response under 500 tokens\u001b[0m                                                                    \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    \u001b[0m                                                                                                           \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[37mID: \u001b[0m\u001b[33m37a00f6b-f3ad-409d-bbc5-50d47398702b\u001b[0m                                                                       \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #800080; text-decoration-color: #800080\">╭─────────────────────────────────────────────── 🤖 Agent Started ────────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>                                                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Agent: </span><span style=\"color: #00ff00; text-decoration-color: #00ff00; font-weight: bold\">Website Content Analyst</span>                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>                                                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Task: </span>                                                                                                         <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    Scrape and analyze the given url</span>                                                                           <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>                                                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    url : https://docs.crewai.com/en/introduction</span>                                                              <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>                                                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    Steps:</span>                                                                                                     <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    1. Use FirecrawlScrapeWebsiteTool to scrape the url</span>                                                        <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    2. Extract main product features and capabilities</span>                                                          <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    3. Identify pricing information if available</span>                                                               <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    4. Note primary use cases or target audience</span>                                                               <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    5. Keep total response under 500 tokens</span>                                                                    <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    </span>                                                                                                           <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>                                                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[35m╭─\u001b[0m\u001b[35m──────────────────────────────────────────────\u001b[0m\u001b[35m 🤖 Agent Started \u001b[0m\u001b[35m───────────────────────────────────────────────\u001b[0m\u001b[35m─╮\u001b[0m\n",
       "\u001b[35m│\u001b[0m                                                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[37mAgent: \u001b[0m\u001b[1;92mWebsite Content Analyst\u001b[0m                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m                                                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[37mTask: \u001b[0m                                                                                                         \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    Scrape and analyze the given url\u001b[0m                                                                           \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m                                                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    url : https://docs.crewai.com/en/introduction\u001b[0m                                                              \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m                                                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    Steps:\u001b[0m                                                                                                     \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    1. Use FirecrawlScrapeWebsiteTool to scrape the url\u001b[0m                                                        \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    2. Extract main product features and capabilities\u001b[0m                                                          \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    3. Identify pricing information if available\u001b[0m                                                               \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    4. Note primary use cases or target audience\u001b[0m                                                               \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    5. Keep total response under 500 tokens\u001b[0m                                                                    \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    \u001b[0m                                                                                                           \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m                                                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #808000; text-decoration-color: #808000\">╭──────────────────────────────────────── 🔧 Tool Execution Started (#1) ─────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Tool: </span><span style=\"color: #808000; text-decoration-color: #808000; font-weight: bold\">firecrawl_web_scrape_tool</span>                                                                                <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Args: </span><span style=\"color: #808000; text-decoration-color: #808000\">{'url': 'https://docs.crewai.com/en/introduction'}</span>                                                       <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[33m╭─\u001b[0m\u001b[33m───────────────────────────────────────\u001b[0m\u001b[33m 🔧 Tool Execution Started (#1) \u001b[0m\u001b[33m────────────────────────────────────────\u001b[0m\u001b[33m─╮\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[37mTool: \u001b[0m\u001b[1;33mfirecrawl_web_scrape_tool\u001b[0m                                                                                \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[37mArgs: \u001b[0m\u001b[33m{'url': 'https://docs.crewai.com/en/introduction'}\u001b[0m                                                       \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[32mTool firecrawl_web_scrape_tool executed with result: markdown='[Skip to main content](https://docs.crewai.com/en/introduction#content-area)\\n\\n[CrewAI home page![light logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&a...\u001b[0m\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008000; text-decoration-color: #008000\">╭─────────────────────────────────────── ✅ Tool Execution Completed (#1) ────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000; font-weight: bold\">Tool Completed</span>                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Tool: </span><span style=\"color: #008000; text-decoration-color: #008000; font-weight: bold\">firecrawl_web_scrape_tool</span>                                                                                <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Output: </span><span style=\"color: #008000; text-decoration-color: #008000\">markdown='[Skip to main content](https://docs.crewai.com/en/introduction#content-area)\\n\\n[CrewAI </span>     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">home page![light </span>                                                                                              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&amp;auto=format&amp;n=5SZbe87tsCW</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">ZY09V&amp;q=85&amp;s=439ca5dc63a1768cad7196005ff5636f)![dark </span>                                                          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&amp;auto=format&amp;n=5SZbe87tsCW</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">ZY09V&amp;q=85&amp;s=439ca5dc63a1768cad7196005ff5636f)](https://docs.crewai.com/)\\n\\n![US](https://d3gk2c5xim1je2.clo</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">udfront.net/flags/US.svg)\\n\\nEnglish\\n\\nSearch...\\n\\nCtrl KAsk AI\\n\\nSearch...\\n\\nNavigation\\n\\nGet </span>           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Started\\n\\nIntroduction\\n\\n[Home](https://docs.crewai.com/) </span>                                                   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Documentation](https://docs.crewai.com/en/introduction) </span>                                                      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[AMP](https://docs.crewai.com/en/enterprise/introduction) [API </span>                                                <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Reference](https://docs.crewai.com/en/api-reference/introduction) </span>                                             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Examples](https://docs.crewai.com/en/examples/example) </span>                                                       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Changelog](https://docs.crewai.com/en/changelog)\\n\\n- [Website](https://crewai.com/)\\n- </span>                      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Forum](https://community.crewai.com/)\\n- [Blog](https://blog.crewai.com/)\\n- </span>                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[CrewGPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)\\n\\n##### Get Started\\n\\n- </span>                       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Introduction](https://docs.crewai.com/en/introduction)\\n- </span>                                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Installation](https://docs.crewai.com/en/installation)\\n- </span>                                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Quickstart](https://docs.crewai.com/en/quickstart)\\n\\n##### Guides\\n\\n- Strategy\\n\\n- Agents\\n\\n- Crews\\n\\n-</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Flows\\n\\n- Advanced\\n\\n\\n##### Core Concepts\\n\\n- [Agents](https://docs.crewai.com/en/concepts/agents)\\n- </span>     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Tasks](https://docs.crewai.com/en/concepts/tasks)\\n- [Crews](https://docs.crewai.com/en/concepts/crews)\\n- </span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Flows](https://docs.crewai.com/en/concepts/flows)\\n- [Production </span>                                             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Architecture](https://docs.crewai.com/en/concepts/production-architecture)\\n- </span>                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Knowledge](https://docs.crewai.com/en/concepts/knowledge)\\n- </span>                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[LLMs](https://docs.crewai.com/en/concepts/llms)\\n- [Files](https://docs.crewai.com/en/concepts/files)\\n- </span>     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Processes](https://docs.crewai.com/en/concepts/processes)\\n- </span>                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Collaboration](https://docs.crewai.com/en/concepts/collaboration)\\n- </span>                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Training](https://docs.crewai.com/en/concepts/training)\\n- </span>                                                   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Memory](https://docs.crewai.com/en/concepts/memory)\\n- </span>                                                       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Reasoning](https://docs.crewai.com/en/concepts/reasoning)\\n- </span>                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Planning](https://docs.crewai.com/en/concepts/planning)\\n- </span>                                                   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Testing](https://docs.crewai.com/en/concepts/testing)\\n- [CLI](https://docs.crewai.com/en/concepts/cli)\\n- </span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Tools](https://docs.crewai.com/en/concepts/tools)\\n- [Event </span>                                                  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Listeners](https://docs.crewai.com/en/concepts/event-listener)\\n\\n##### MCP Integration\\n\\n- [MCP Servers as </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Tools in CrewAI](https://docs.crewai.com/en/mcp/overview)\\n- [MCP DSL </span>                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Integration](https://docs.crewai.com/en/mcp/dsl-integration)\\n- [Stdio </span>                                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Transport](https://docs.crewai.com/en/mcp/stdio)\\n- [SSE Transport](https://docs.crewai.com/en/mcp/sse)\\n- </span>    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Streamable HTTP Transport](https://docs.crewai.com/en/mcp/streamable-http)\\n- [Connecting to Multiple MCP </span>    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Servers](https://docs.crewai.com/en/mcp/multiple-servers)\\n- [MCP Security </span>                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Considerations](https://docs.crewai.com/en/mcp/security)\\n\\n##### Tools\\n\\n- [Tools </span>                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Overview](https://docs.crewai.com/en/tools/overview)\\n- File &amp; Document\\n\\n- Web Scraping &amp; Browsing\\n\\n- </span>     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Search &amp; Research\\n\\n- Database &amp; Data\\n\\n- AI &amp; Machine Learning\\n\\n- Cloud &amp; Storage\\n\\n- Integrations\\n\\n-</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Automation\\n\\n\\n##### Observability\\n\\n- [CrewAI </span>                                                              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Tracing](https://docs.crewai.com/en/observability/tracing)\\n- </span>                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Overview](https://docs.crewai.com/en/observability/overview)\\n- [Arize </span>                                       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Phoenix](https://docs.crewai.com/en/observability/arize-phoenix)\\n- </span>                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Braintrust](https://docs.crewai.com/en/observability/braintrust)\\n- [Datadog </span>                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Integration](https://docs.crewai.com/en/observability/datadog)\\n- </span>                                             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Galileo](https://docs.crewai.com/en/observability/galileo)\\n- [LangDB </span>                                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Integration](https://docs.crewai.com/en/observability/langdb)\\n- [Langfuse </span>                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Integration](https://docs.crewai.com/en/observability/langfuse)\\n- [Langtrace </span>                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Integration](https://docs.crewai.com/en/observability/langtrace)\\n- [Maxim </span>                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Integration](https://docs.crewai.com/en/observability/maxim)\\n- [MLflow </span>                                       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Integration](https://docs.crewai.com/en/observability/mlflow)\\n- [Neatlogs </span>                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Integration](https://docs.crewai.com/en/observability/neatlogs)\\n- [OpenLIT </span>                                   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Integration](https://docs.crewai.com/en/observability/openlit)\\n- [Opik </span>                                       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Integration](https://docs.crewai.com/en/observability/opik)\\n- [Patronus AI </span>                                   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Evaluation](https://docs.crewai.com/en/observability/patronus-evaluation)\\n- [Portkey </span>                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Integration](https://docs.crewai.com/en/observability/portkey)\\n- [Weave </span>                                      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Integration](https://docs.crewai.com/en/observability/weave)\\n- [TrueFoundry </span>                                  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Integration](https://docs.crewai.com/en/observability/truefoundry)\\n\\n##### Learn\\n\\n- </span>                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Overview](https://docs.crewai.com/en/learn/overview)\\n- [Strategic LLM Selection </span>                             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Guide](https://docs.crewai.com/en/learn/llm-selection-guide)\\n- [Conditional </span>                                  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Tasks](https://docs.crewai.com/en/learn/conditional-tasks)\\n- [Coding </span>                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Agents](https://docs.crewai.com/en/learn/coding-agents)\\n- [Create Custom </span>                                     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Tools](https://docs.crewai.com/en/learn/create-custom-tools)\\n- [Custom LLM </span>                                   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Implementation](https://docs.crewai.com/en/learn/custom-llm)\\n- [Custom Manager </span>                               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Agent](https://docs.crewai.com/en/learn/custom-manager-agent)\\n- [Customize </span>                                   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Agents](https://docs.crewai.com/en/learn/customizing-agents)\\n- [Image Generation with </span>                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">DALL-E](https://docs.crewai.com/en/learn/dalle-image-generation)\\n- [Force Tool Output as </span>                     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Result](https://docs.crewai.com/en/learn/force-tool-output-as-result)\\n- [Hierarchical </span>                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Process](https://docs.crewai.com/en/learn/hierarchical-process)\\n- [Human Input on </span>                            <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Execution](https://docs.crewai.com/en/learn/human-input-on-execution)\\n- [Human-in-the-Loop (HITL) </span>            <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Workflows](https://docs.crewai.com/en/learn/human-in-the-loop)\\n- [Human Feedback in </span>                          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Flows](https://docs.crewai.com/en/learn/human-feedback-in-flows)\\n- [Kickoff Crew </span>                             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Asynchronously](https://docs.crewai.com/en/learn/kickoff-async)\\n- [Kickoff Crew for </span>                          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Each](https://docs.crewai.com/en/learn/kickoff-for-each)\\n- [Connect to any </span>                                   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">LLM](https://docs.crewai.com/en/learn/llm-connections)\\n- [Using Multimodal </span>                                   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Agents](https://docs.crewai.com/en/learn/multimodal-agents)\\n- [Replay Tasks from Latest Crew </span>                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Kickoff](https://docs.crewai.com/en/learn/replay-tasks-from-latest-crew-kickoff)\\n- [Sequential </span>               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Processes](https://docs.crewai.com/en/learn/sequential-process)\\n- [Using Annotations in </span>                      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">crew.py](https://docs.crewai.com/en/learn/using-annotations)\\n- [Execution Hooks </span>                              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Overview](https://docs.crewai.com/en/learn/execution-hooks)\\n- [LLM Call </span>                                      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Hooks](https://docs.crewai.com/en/learn/llm-hooks)\\n- [Tool Call </span>                                              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Hooks](https://docs.crewai.com/en/learn/tool-hooks)\\n\\n##### Telemetry\\n\\n- </span>                                   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[Telemetry](https://docs.crewai.com/en/telemetry)\\n\\n# </span>                                                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[\\u200b](https://docs.crewai.com/en/introduction\\\\#what-is-crewai)  What is CrewAI?\\n\\n**CrewAI is the </span>        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">leading open-source framework for orchestrating autonomous AI agents and building complex workflows.**It </span>      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">empowers developers to build production-ready multi-agent systems by combining the collaborative intelligence</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">of **Crews** with the precise control of **Flows**.\\n\\n- **[CrewAI </span>                                            <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Flows](https://docs.crewai.com/en/guides/flows/first-flow)**: The backbone of your AI application. Flows </span>      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">allow you to create structured, event-driven workflows that manage state and control execution. They provide </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">the scaffolding for your AI agents to work within.\\n- **[CrewAI </span>                                               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Crews](https://docs.crewai.com/en/guides/crews/first-crew)**: The units of work within your Flow. Crews are </span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">teams of autonomous agents that collaborate to solve specific tasks delegated to them by the Flow.\\n\\nWith </span>    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">over 100,000 developers certified through our community courses, CrewAI is the standard for enterprise-ready </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">AI automation.\\n\\n## [\\u200b](https://docs.crewai.com/en/introduction\\\\#the-crewai-architecture)  The CrewAI </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Architecture\\n\\nCrewAI’s architecture is designed to balance autonomy with control.\\n\\n### </span>                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[\\u200b](https://docs.crewai.com/en/introduction\\\\#1-flows-the-backbone)  1\\\\. Flows: The Backbone\\n\\nThink </span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">of a Flow as the “manager” or the “process definition” of your application. It defines the steps, the logic, </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">and how data moves through your system.\\n\\n![CrewAI Framework </span>                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Overview](https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?fit=max&amp;auto=format&amp;n=qVjgZHKAyEOgSSUS</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">&amp;q=85&amp;s=82ea168de2f004553dcea21410cd7d8a)\\n\\nCrewAI Framework Overview\\n\\nFlows provide:\\n\\n- **State </span>         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Management**: Persist data across steps and executions.\\n- **Event-Driven Execution**: Trigger actions based </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">on events or external inputs.\\n- **Control Flow**: Use conditional logic, loops, and branching.\\n\\n### </span>        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[\\u200b](https://docs.crewai.com/en/introduction\\\\#2-crews-the-intelligence)  2\\\\. Crews: The </span>                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Intelligence\\n\\nCrews are the “teams” that do the heavy lifting. Within a Flow, you can trigger a Crew to </span>     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">tackle a complex problem requiring creativity and collaboration.\\n\\n![CrewAI Framework </span>                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Overview](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?fit=max&amp;auto=format&amp;n=5SZbe87tsCWZY09V</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">&amp;q=85&amp;s=514fd0b06e4128e62f10728d44601975)\\n\\nCrewAI Framework Overview\\n\\nCrews provide:\\n\\n- **Role-Playing </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Agents**: Specialized agents with specific goals and tools.\\n- **Autonomous Collaboration**: Agents work </span>      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">together to solve tasks.\\n- **Task Delegation**: Tasks are assigned and executed based on agent </span>               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">capabilities.\\n\\n## [\\u200b](https://docs.crewai.com/en/introduction\\\\#how-it-all-works-together)  How It All</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Works Together\\n\\n1. **The Flow** triggers an event or starts a process.\\n2. **The Flow** manages the state </span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">and decides what to do next.\\n3. **The Flow** delegates a complex task to a **Crew**.\\n4. **The Crew**’s </span>      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">agents collaborate to complete the task.\\n5. **The Crew** returns the result to the **Flow**.\\n6. **The </span>       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Flow** continues execution based on the result.\\n\\n## </span>                                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[\\u200b](https://docs.crewai.com/en/introduction\\\\#key-features)  Key Features\\n\\n## Production-Grade </span>         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Flows\\n\\nBuild reliable, stateful workflows that can handle long-running processes and complex logic.\\n\\n## </span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Autonomous Crews\\n\\nDeploy teams of agents that can plan, execute, and collaborate to achieve high-level </span>      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">goals.\\n\\n## Flexible Tools\\n\\nConnect your agents to any API, database, or local tool.\\n\\n## Enterprise </span>      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Security\\n\\nDesigned with security and compliance in mind for enterprise deployments.\\n\\n## </span>                   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[\\u200b](https://docs.crewai.com/en/introduction\\\\#when-to-use-crews-vs-flows)  When to Use Crews vs. </span>         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Flows\\n\\n**The short answer: Use both.**For any production-ready application, **start with a Flow**.\\n\\n- </span>     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">**Use a Flow** to define the overall structure, state, and logic of your application.\\n- **Use a Crew** </span>       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">within a Flow step when you need a team of agents to perform a specific, complex task that requires </span>           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">autonomy.\\n\\n| Use Case | Architecture |\\n| --- | --- |\\n| **Simple Automation** | Single Flow with Python </span>    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">tasks |\\n| **Complex Research** | Flow managing state -&gt; Crew performing research |\\n| **Application </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Backend** | Flow handling API requests -&gt; Crew generating content -&gt; Flow saving to DB |\\n\\n## </span>                <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[\\u200b](https://docs.crewai.com/en/introduction\\\\#why-choose-crewai)  Why Choose CrewAI?\\n\\n- 🧠 </span>             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">**Autonomous Operation**: Agents make intelligent decisions based on their roles and available tools\\n- 📝 </span>    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">**Natural Interaction**: Agents communicate and collaborate like human team members\\n- 🛠️ **Extensible </span>        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Design**: Easy to add new tools, roles, and capabilities\\n- 🚀 **Production Ready**: Built for reliability </span>    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">and scalability in real-world applications\\n- 🔒 **Security-Focused**: Designed with enterprise security </span>      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">requirements in mind\\n- 💰 **Cost-Efficient**: Optimized to minimize token usage and API calls\\n\\n## </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">[\\u200b](https://docs.crewai.com/en/introduction\\\\#ready-to-start-building)  Ready to Start </span>                   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Building?\\n\\n[**Build Your First Flow** \\\\\\\\\\n\\\\\\\\\\nLearn how to create structured, event-driven workflows </span>    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">with precise control over execution.](https://docs.crewai.com/en/guides/flows/first-flow) [**Build Your First</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Crew** \\\\\\\\\\n\\\\\\\\\\nStep-by-step tutorial to create a collaborative AI team that works together to solve </span>       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">complex problems.](https://docs.crewai.com/en/guides/crews/first-crew)\\n\\n[**Install CrewAI** \\\\\\\\\\n\\\\\\\\\\nGet</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">started with CrewAI in your development environment.](https://docs.crewai.com/en/installation) [**Quick </span>       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Start** \\\\\\\\\\n\\\\\\\\\\nFollow our quickstart guide to create your first CrewAI agent and get hands-on </span>            <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">experience.](https://docs.crewai.com/en/en/quickstart) [**Join the Community** \\\\\\\\\\n\\\\\\\\\\nConnect with other</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">developers, get help, and share your CrewAI experiences.](https://community.crewai.com/)\\n\\nWas this page </span>     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">helpful?\\n\\nYesNo\\n\\n[Installation\\\\\\\\\\n\\\\\\\\\\nNext](https://docs.crewai.com/en/installation)\\n\\nCtrl+I\\n\\nAss</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">istant\\n\\nResponses are generated using AI and may contain mistakes.\\n\\n![CrewAI Framework </span>                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Overview](https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=1100&amp;fit=max&amp;auto=format&amp;n=qVjgZHKAy</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">EOgSSUS&amp;q=85&amp;s=540eb3d8d8f256d6d703aa5e6111a4cd)\\n\\n![CrewAI Framework </span>                                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Overview](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=1100&amp;fit=max&amp;auto=format&amp;n=5SZbe87ts</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">CWZY09V&amp;q=85&amp;s=1af6e6a337b70ca2ce238d8e40f49218)' html=None raw_html=None json=None summary=None </span>              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">metadata=DocumentMetadata(title='Introduction - CrewAI', description='Build AI agent teams that work together</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">to tackle complex tasks', url='https://docs.crewai.com/en/introduction', language='en', keywords='AI agents, </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">multi-agent systems, CrewAI, artificial intelligence, automation, Python framework, agent collaboration, AI </span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">workflows', robots=None, og_title='Introduction - CrewAI', og_description='Build AI agent teams that work </span>     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">together to tackle complex tasks', og_url='https://docs.crewai.com/en/introduction', </span>                          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">og_image='https://docs.crewai.com/images/crew_only_logo.png', og_audio=None, og_determiner=None, </span>              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">og_locale=None, og_locale_alternate=None, og_site_name=None, og_video=None, </span>                                   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">favicon='https://docs.crewai.com/mintlify-assets/_mintlify/favicons/crewai/fh3rA5-EcpjhGg8R/_generated/favico</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">n/favicon-16x16.png', dc_terms_created=None, dc_date_created=None, dc_date=None, dc_terms_type=None, </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">dc_type=None, dc_terms_audience=None, dc_terms_subject=None, dc_subject=None, dc_description=None, </span>            <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">dc_terms_keywords=None, modified_time=None, published_time=None, article_tag=None, article_section=None, </span>      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">source_url='https://docs.crewai.com/en/introduction', status_code=200, </span>                                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">scrape_id='019c3c92-05f6-703b-be80-60068fadd874', num_pages=None, content_type='text/html; charset=utf-8', </span>    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">proxy_used='basic', timezone=None, cache_state='hit', cached_at='2026-02-07T12:16:36.171Z', credits_used=1, </span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">concurrency_limited=False, concurrency_queue_duration_ms=None, error=None, twitter:image:width='1200', </span>        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">generator='Mintlify', </span>                                                                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">msapplication-config='/mintlify-assets/_mintlify/favicons/crewai/fh3rA5-EcpjhGg8R/_generated/favicon/browserc</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">onfig.xml', next-size-adjust='', apple-mobile-web-app-title='CrewAI', og:type='website', </span>                      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">twitter:description='Build AI agent teams that work together to tackle complex tasks', </span>                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">twitter:card='summary_large_image', og:url='https://docs.crewai.com/en/introduction', og:image:width='1200', </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">canonical='https://docs.crewai.com/en/introduction', </span>                                                          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">og:image='https://docs.crewai.com/images/crew_only_logo.png', og:description='Build AI agent teams that work </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">together to tackle complex tasks', twitter:image='https://docs.crewai.com/images/crew_only_logo.png', </span>         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">twitter:image:height='630', twitter:title='Introduction - CrewAI', charset='utf-8', og:site_name='CrewAI </span>      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Documentation', viewport='width=device-width, initial-scale=1, maximum-scale=1, viewport-fit=cover', </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">og:image:height='630', application-name='CrewAI', msapplication-TileColor='#EB6658', og:title='Introduction -</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">CrewAI') links=None images=None screenshot=None actions=None warning=None change_tracking=None branding=None</span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[32m╭─\u001b[0m\u001b[32m──────────────────────────────────────\u001b[0m\u001b[32m ✅ Tool Execution Completed (#1) \u001b[0m\u001b[32m───────────────────────────────────────\u001b[0m\u001b[32m─╮\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[1;32mTool Completed\u001b[0m                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mTool: \u001b[0m\u001b[1;32mfirecrawl_web_scrape_tool\u001b[0m                                                                                \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mOutput: \u001b[0m\u001b[32mmarkdown='[Skip to main content](https://docs.crewai.com/en/introduction#content-area)\\n\\n[CrewAI \u001b[0m     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mhome page![light \u001b[0m                                                                                              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mlogo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCW\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)![dark \u001b[0m                                                          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mlogo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCW\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)](https://docs.crewai.com/)\\n\\n![US](https://d3gk2c5xim1je2.clo\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mudfront.net/flags/US.svg)\\n\\nEnglish\\n\\nSearch...\\n\\nCtrl KAsk AI\\n\\nSearch...\\n\\nNavigation\\n\\nGet \u001b[0m           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mStarted\\n\\nIntroduction\\n\\n[Home](https://docs.crewai.com/) \u001b[0m                                                   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Documentation](https://docs.crewai.com/en/introduction) \u001b[0m                                                      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[AMP](https://docs.crewai.com/en/enterprise/introduction) [API \u001b[0m                                                \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mReference](https://docs.crewai.com/en/api-reference/introduction) \u001b[0m                                             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Examples](https://docs.crewai.com/en/examples/example) \u001b[0m                                                       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Changelog](https://docs.crewai.com/en/changelog)\\n\\n- [Website](https://crewai.com/)\\n- \u001b[0m                      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Forum](https://community.crewai.com/)\\n- [Blog](https://blog.crewai.com/)\\n- \u001b[0m                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[CrewGPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)\\n\\n##### Get Started\\n\\n- \u001b[0m                       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Introduction](https://docs.crewai.com/en/introduction)\\n- \u001b[0m                                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Installation](https://docs.crewai.com/en/installation)\\n- \u001b[0m                                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Quickstart](https://docs.crewai.com/en/quickstart)\\n\\n##### Guides\\n\\n- Strategy\\n\\n- Agents\\n\\n- Crews\\n\\n-\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mFlows\\n\\n- Advanced\\n\\n\\n##### Core Concepts\\n\\n- [Agents](https://docs.crewai.com/en/concepts/agents)\\n- \u001b[0m     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Tasks](https://docs.crewai.com/en/concepts/tasks)\\n- [Crews](https://docs.crewai.com/en/concepts/crews)\\n- \u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Flows](https://docs.crewai.com/en/concepts/flows)\\n- [Production \u001b[0m                                             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mArchitecture](https://docs.crewai.com/en/concepts/production-architecture)\\n- \u001b[0m                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Knowledge](https://docs.crewai.com/en/concepts/knowledge)\\n- \u001b[0m                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[LLMs](https://docs.crewai.com/en/concepts/llms)\\n- [Files](https://docs.crewai.com/en/concepts/files)\\n- \u001b[0m     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Processes](https://docs.crewai.com/en/concepts/processes)\\n- \u001b[0m                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Collaboration](https://docs.crewai.com/en/concepts/collaboration)\\n- \u001b[0m                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Training](https://docs.crewai.com/en/concepts/training)\\n- \u001b[0m                                                   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Memory](https://docs.crewai.com/en/concepts/memory)\\n- \u001b[0m                                                       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Reasoning](https://docs.crewai.com/en/concepts/reasoning)\\n- \u001b[0m                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Planning](https://docs.crewai.com/en/concepts/planning)\\n- \u001b[0m                                                   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Testing](https://docs.crewai.com/en/concepts/testing)\\n- [CLI](https://docs.crewai.com/en/concepts/cli)\\n- \u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Tools](https://docs.crewai.com/en/concepts/tools)\\n- [Event \u001b[0m                                                  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mListeners](https://docs.crewai.com/en/concepts/event-listener)\\n\\n##### MCP Integration\\n\\n- [MCP Servers as \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mTools in CrewAI](https://docs.crewai.com/en/mcp/overview)\\n- [MCP DSL \u001b[0m                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mIntegration](https://docs.crewai.com/en/mcp/dsl-integration)\\n- [Stdio \u001b[0m                                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mTransport](https://docs.crewai.com/en/mcp/stdio)\\n- [SSE Transport](https://docs.crewai.com/en/mcp/sse)\\n- \u001b[0m    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Streamable HTTP Transport](https://docs.crewai.com/en/mcp/streamable-http)\\n- [Connecting to Multiple MCP \u001b[0m    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mServers](https://docs.crewai.com/en/mcp/multiple-servers)\\n- [MCP Security \u001b[0m                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mConsiderations](https://docs.crewai.com/en/mcp/security)\\n\\n##### Tools\\n\\n- [Tools \u001b[0m                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mOverview](https://docs.crewai.com/en/tools/overview)\\n- File & Document\\n\\n- Web Scraping & Browsing\\n\\n- \u001b[0m     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mSearch & Research\\n\\n- Database & Data\\n\\n- AI & Machine Learning\\n\\n- Cloud & Storage\\n\\n- Integrations\\n\\n-\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mAutomation\\n\\n\\n##### Observability\\n\\n- [CrewAI \u001b[0m                                                              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mTracing](https://docs.crewai.com/en/observability/tracing)\\n- \u001b[0m                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Overview](https://docs.crewai.com/en/observability/overview)\\n- [Arize \u001b[0m                                       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mPhoenix](https://docs.crewai.com/en/observability/arize-phoenix)\\n- \u001b[0m                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Braintrust](https://docs.crewai.com/en/observability/braintrust)\\n- [Datadog \u001b[0m                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mIntegration](https://docs.crewai.com/en/observability/datadog)\\n- \u001b[0m                                             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Galileo](https://docs.crewai.com/en/observability/galileo)\\n- [LangDB \u001b[0m                                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mIntegration](https://docs.crewai.com/en/observability/langdb)\\n- [Langfuse \u001b[0m                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mIntegration](https://docs.crewai.com/en/observability/langfuse)\\n- [Langtrace \u001b[0m                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mIntegration](https://docs.crewai.com/en/observability/langtrace)\\n- [Maxim \u001b[0m                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mIntegration](https://docs.crewai.com/en/observability/maxim)\\n- [MLflow \u001b[0m                                       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mIntegration](https://docs.crewai.com/en/observability/mlflow)\\n- [Neatlogs \u001b[0m                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mIntegration](https://docs.crewai.com/en/observability/neatlogs)\\n- [OpenLIT \u001b[0m                                   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mIntegration](https://docs.crewai.com/en/observability/openlit)\\n- [Opik \u001b[0m                                       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mIntegration](https://docs.crewai.com/en/observability/opik)\\n- [Patronus AI \u001b[0m                                   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mEvaluation](https://docs.crewai.com/en/observability/patronus-evaluation)\\n- [Portkey \u001b[0m                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mIntegration](https://docs.crewai.com/en/observability/portkey)\\n- [Weave \u001b[0m                                      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mIntegration](https://docs.crewai.com/en/observability/weave)\\n- [TrueFoundry \u001b[0m                                  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mIntegration](https://docs.crewai.com/en/observability/truefoundry)\\n\\n##### Learn\\n\\n- \u001b[0m                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Overview](https://docs.crewai.com/en/learn/overview)\\n- [Strategic LLM Selection \u001b[0m                             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mGuide](https://docs.crewai.com/en/learn/llm-selection-guide)\\n- [Conditional \u001b[0m                                  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mTasks](https://docs.crewai.com/en/learn/conditional-tasks)\\n- [Coding \u001b[0m                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mAgents](https://docs.crewai.com/en/learn/coding-agents)\\n- [Create Custom \u001b[0m                                     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mTools](https://docs.crewai.com/en/learn/create-custom-tools)\\n- [Custom LLM \u001b[0m                                   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mImplementation](https://docs.crewai.com/en/learn/custom-llm)\\n- [Custom Manager \u001b[0m                               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mAgent](https://docs.crewai.com/en/learn/custom-manager-agent)\\n- [Customize \u001b[0m                                   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mAgents](https://docs.crewai.com/en/learn/customizing-agents)\\n- [Image Generation with \u001b[0m                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mDALL-E](https://docs.crewai.com/en/learn/dalle-image-generation)\\n- [Force Tool Output as \u001b[0m                     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mResult](https://docs.crewai.com/en/learn/force-tool-output-as-result)\\n- [Hierarchical \u001b[0m                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mProcess](https://docs.crewai.com/en/learn/hierarchical-process)\\n- [Human Input on \u001b[0m                            \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mExecution](https://docs.crewai.com/en/learn/human-input-on-execution)\\n- [Human-in-the-Loop (HITL) \u001b[0m            \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mWorkflows](https://docs.crewai.com/en/learn/human-in-the-loop)\\n- [Human Feedback in \u001b[0m                          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mFlows](https://docs.crewai.com/en/learn/human-feedback-in-flows)\\n- [Kickoff Crew \u001b[0m                             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mAsynchronously](https://docs.crewai.com/en/learn/kickoff-async)\\n- [Kickoff Crew for \u001b[0m                          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mEach](https://docs.crewai.com/en/learn/kickoff-for-each)\\n- [Connect to any \u001b[0m                                   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mLLM](https://docs.crewai.com/en/learn/llm-connections)\\n- [Using Multimodal \u001b[0m                                   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mAgents](https://docs.crewai.com/en/learn/multimodal-agents)\\n- [Replay Tasks from Latest Crew \u001b[0m                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mKickoff](https://docs.crewai.com/en/learn/replay-tasks-from-latest-crew-kickoff)\\n- [Sequential \u001b[0m               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mProcesses](https://docs.crewai.com/en/learn/sequential-process)\\n- [Using Annotations in \u001b[0m                      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mcrew.py](https://docs.crewai.com/en/learn/using-annotations)\\n- [Execution Hooks \u001b[0m                              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mOverview](https://docs.crewai.com/en/learn/execution-hooks)\\n- [LLM Call \u001b[0m                                      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mHooks](https://docs.crewai.com/en/learn/llm-hooks)\\n- [Tool Call \u001b[0m                                              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mHooks](https://docs.crewai.com/en/learn/tool-hooks)\\n\\n##### Telemetry\\n\\n- \u001b[0m                                   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[Telemetry](https://docs.crewai.com/en/telemetry)\\n\\n# \u001b[0m                                                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[\\u200b](https://docs.crewai.com/en/introduction\\\\#what-is-crewai)  What is CrewAI?\\n\\n**CrewAI is the \u001b[0m        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mleading open-source framework for orchestrating autonomous AI agents and building complex workflows.**It \u001b[0m      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mempowers developers to build production-ready multi-agent systems by combining the collaborative intelligence\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mof **Crews** with the precise control of **Flows**.\\n\\n- **[CrewAI \u001b[0m                                            \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mFlows](https://docs.crewai.com/en/guides/flows/first-flow)**: The backbone of your AI application. Flows \u001b[0m      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mallow you to create structured, event-driven workflows that manage state and control execution. They provide \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mthe scaffolding for your AI agents to work within.\\n- **[CrewAI \u001b[0m                                               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mCrews](https://docs.crewai.com/en/guides/crews/first-crew)**: The units of work within your Flow. Crews are \u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mteams of autonomous agents that collaborate to solve specific tasks delegated to them by the Flow.\\n\\nWith \u001b[0m    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mover 100,000 developers certified through our community courses, CrewAI is the standard for enterprise-ready \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mAI automation.\\n\\n## [\\u200b](https://docs.crewai.com/en/introduction\\\\#the-crewai-architecture)  The CrewAI \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mArchitecture\\n\\nCrewAI’s architecture is designed to balance autonomy with control.\\n\\n### \u001b[0m                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[\\u200b](https://docs.crewai.com/en/introduction\\\\#1-flows-the-backbone)  1\\\\. Flows: The Backbone\\n\\nThink \u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mof a Flow as the “manager” or the “process definition” of your application. It defines the steps, the logic, \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mand how data moves through your system.\\n\\n![CrewAI Framework \u001b[0m                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mOverview](https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m&q=85&s=82ea168de2f004553dcea21410cd7d8a)\\n\\nCrewAI Framework Overview\\n\\nFlows provide:\\n\\n- **State \u001b[0m         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mManagement**: Persist data across steps and executions.\\n- **Event-Driven Execution**: Trigger actions based \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mon events or external inputs.\\n- **Control Flow**: Use conditional logic, loops, and branching.\\n\\n### \u001b[0m        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[\\u200b](https://docs.crewai.com/en/introduction\\\\#2-crews-the-intelligence)  2\\\\. Crews: The \u001b[0m                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mIntelligence\\n\\nCrews are the “teams” that do the heavy lifting. Within a Flow, you can trigger a Crew to \u001b[0m     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mtackle a complex problem requiring creativity and collaboration.\\n\\n![CrewAI Framework \u001b[0m                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mOverview](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?fit=max&auto=format&n=5SZbe87tsCWZY09V\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m&q=85&s=514fd0b06e4128e62f10728d44601975)\\n\\nCrewAI Framework Overview\\n\\nCrews provide:\\n\\n- **Role-Playing \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mAgents**: Specialized agents with specific goals and tools.\\n- **Autonomous Collaboration**: Agents work \u001b[0m      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mtogether to solve tasks.\\n- **Task Delegation**: Tasks are assigned and executed based on agent \u001b[0m               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mcapabilities.\\n\\n## [\\u200b](https://docs.crewai.com/en/introduction\\\\#how-it-all-works-together)  How It All\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mWorks Together\\n\\n1. **The Flow** triggers an event or starts a process.\\n2. **The Flow** manages the state \u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mand decides what to do next.\\n3. **The Flow** delegates a complex task to a **Crew**.\\n4. **The Crew**’s \u001b[0m      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32magents collaborate to complete the task.\\n5. **The Crew** returns the result to the **Flow**.\\n6. **The \u001b[0m       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mFlow** continues execution based on the result.\\n\\n## \u001b[0m                                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[\\u200b](https://docs.crewai.com/en/introduction\\\\#key-features)  Key Features\\n\\n## Production-Grade \u001b[0m         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mFlows\\n\\nBuild reliable, stateful workflows that can handle long-running processes and complex logic.\\n\\n## \u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mAutonomous Crews\\n\\nDeploy teams of agents that can plan, execute, and collaborate to achieve high-level \u001b[0m      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mgoals.\\n\\n## Flexible Tools\\n\\nConnect your agents to any API, database, or local tool.\\n\\n## Enterprise \u001b[0m      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mSecurity\\n\\nDesigned with security and compliance in mind for enterprise deployments.\\n\\n## \u001b[0m                   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[\\u200b](https://docs.crewai.com/en/introduction\\\\#when-to-use-crews-vs-flows)  When to Use Crews vs. \u001b[0m         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mFlows\\n\\n**The short answer: Use both.**For any production-ready application, **start with a Flow**.\\n\\n- \u001b[0m     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m**Use a Flow** to define the overall structure, state, and logic of your application.\\n- **Use a Crew** \u001b[0m       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mwithin a Flow step when you need a team of agents to perform a specific, complex task that requires \u001b[0m           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mautonomy.\\n\\n| Use Case | Architecture |\\n| --- | --- |\\n| **Simple Automation** | Single Flow with Python \u001b[0m    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mtasks |\\n| **Complex Research** | Flow managing state -> Crew performing research |\\n| **Application \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mBackend** | Flow handling API requests -> Crew generating content -> Flow saving to DB |\\n\\n## \u001b[0m                \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[\\u200b](https://docs.crewai.com/en/introduction\\\\#why-choose-crewai)  Why Choose CrewAI?\\n\\n- 🧠 \u001b[0m             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m**Autonomous Operation**: Agents make intelligent decisions based on their roles and available tools\\n- 📝 \u001b[0m    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m**Natural Interaction**: Agents communicate and collaborate like human team members\\n- 🛠️ **Extensible \u001b[0m        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mDesign**: Easy to add new tools, roles, and capabilities\\n- 🚀 **Production Ready**: Built for reliability \u001b[0m    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mand scalability in real-world applications\\n- 🔒 **Security-Focused**: Designed with enterprise security \u001b[0m      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mrequirements in mind\\n- 💰 **Cost-Efficient**: Optimized to minimize token usage and API calls\\n\\n## \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m[\\u200b](https://docs.crewai.com/en/introduction\\\\#ready-to-start-building)  Ready to Start \u001b[0m                   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mBuilding?\\n\\n[**Build Your First Flow** \\\\\\\\\\n\\\\\\\\\\nLearn how to create structured, event-driven workflows \u001b[0m    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mwith precise control over execution.](https://docs.crewai.com/en/guides/flows/first-flow) [**Build Your First\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mCrew** \\\\\\\\\\n\\\\\\\\\\nStep-by-step tutorial to create a collaborative AI team that works together to solve \u001b[0m       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mcomplex problems.](https://docs.crewai.com/en/guides/crews/first-crew)\\n\\n[**Install CrewAI** \\\\\\\\\\n\\\\\\\\\\nGet\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mstarted with CrewAI in your development environment.](https://docs.crewai.com/en/installation) [**Quick \u001b[0m       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mStart** \\\\\\\\\\n\\\\\\\\\\nFollow our quickstart guide to create your first CrewAI agent and get hands-on \u001b[0m            \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mexperience.](https://docs.crewai.com/en/en/quickstart) [**Join the Community** \\\\\\\\\\n\\\\\\\\\\nConnect with other\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mdevelopers, get help, and share your CrewAI experiences.](https://community.crewai.com/)\\n\\nWas this page \u001b[0m     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mhelpful?\\n\\nYesNo\\n\\n[Installation\\\\\\\\\\n\\\\\\\\\\nNext](https://docs.crewai.com/en/installation)\\n\\nCtrl+I\\n\\nAss\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mistant\\n\\nResponses are generated using AI and may contain mistakes.\\n\\n![CrewAI Framework \u001b[0m                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mOverview](https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=1100&fit=max&auto=format&n=qVjgZHKAy\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mEOgSSUS&q=85&s=540eb3d8d8f256d6d703aa5e6111a4cd)\\n\\n![CrewAI Framework \u001b[0m                                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mOverview](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=1100&fit=max&auto=format&n=5SZbe87ts\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mCWZY09V&q=85&s=1af6e6a337b70ca2ce238d8e40f49218)' html=None raw_html=None json=None summary=None \u001b[0m              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mmetadata=DocumentMetadata(title='Introduction - CrewAI', description='Build AI agent teams that work together\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mto tackle complex tasks', url='https://docs.crewai.com/en/introduction', language='en', keywords='AI agents, \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mmulti-agent systems, CrewAI, artificial intelligence, automation, Python framework, agent collaboration, AI \u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mworkflows', robots=None, og_title='Introduction - CrewAI', og_description='Build AI agent teams that work \u001b[0m     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mtogether to tackle complex tasks', og_url='https://docs.crewai.com/en/introduction', \u001b[0m                          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mog_image='https://docs.crewai.com/images/crew_only_logo.png', og_audio=None, og_determiner=None, \u001b[0m              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mog_locale=None, og_locale_alternate=None, og_site_name=None, og_video=None, \u001b[0m                                   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mfavicon='https://docs.crewai.com/mintlify-assets/_mintlify/favicons/crewai/fh3rA5-EcpjhGg8R/_generated/favico\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mn/favicon-16x16.png', dc_terms_created=None, dc_date_created=None, dc_date=None, dc_terms_type=None, \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mdc_type=None, dc_terms_audience=None, dc_terms_subject=None, dc_subject=None, dc_description=None, \u001b[0m            \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mdc_terms_keywords=None, modified_time=None, published_time=None, article_tag=None, article_section=None, \u001b[0m      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32msource_url='https://docs.crewai.com/en/introduction', status_code=200, \u001b[0m                                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mscrape_id='019c3c92-05f6-703b-be80-60068fadd874', num_pages=None, content_type='text/html; charset=utf-8', \u001b[0m    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mproxy_used='basic', timezone=None, cache_state='hit', cached_at='2026-02-07T12:16:36.171Z', credits_used=1, \u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mconcurrency_limited=False, concurrency_queue_duration_ms=None, error=None, twitter:image:width='1200', \u001b[0m        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mgenerator='Mintlify', \u001b[0m                                                                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mmsapplication-config='/mintlify-assets/_mintlify/favicons/crewai/fh3rA5-EcpjhGg8R/_generated/favicon/browserc\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32monfig.xml', next-size-adjust='', apple-mobile-web-app-title='CrewAI', og:type='website', \u001b[0m                      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mtwitter:description='Build AI agent teams that work together to tackle complex tasks', \u001b[0m                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mtwitter:card='summary_large_image', og:url='https://docs.crewai.com/en/introduction', og:image:width='1200', \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mcanonical='https://docs.crewai.com/en/introduction', \u001b[0m                                                          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mog:image='https://docs.crewai.com/images/crew_only_logo.png', og:description='Build AI agent teams that work \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mtogether to tackle complex tasks', twitter:image='https://docs.crewai.com/images/crew_only_logo.png', \u001b[0m         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mtwitter:image:height='630', twitter:title='Introduction - CrewAI', charset='utf-8', og:site_name='CrewAI \u001b[0m      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mDocumentation', viewport='width=device-width, initial-scale=1, maximum-scale=1, viewport-fit=cover', \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mog:image:height='630', application-name='CrewAI', msapplication-TileColor='#EB6658', og:title='Introduction -\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mCrewAI') links=None images=None screenshot=None actions=None warning=None change_tracking=None branding=None\u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008000; text-decoration-color: #008000\">╭───────────────────────────────────────────── ✅ Agent Final Answer ─────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Agent: </span><span style=\"color: #00ff00; text-decoration-color: #00ff00; font-weight: bold\">Website Content Analyst</span>                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Final Answer:</span>                                                                                                  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">CrewAI is an open-source framework for orchestrating autonomous AI agents and building complex workflows. It </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">empowers developers to build production-ready multi-agent systems by combining the collaborative intelligence</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">of Crews with the precise control of Flows. CrewAI's architecture is designed to balance autonomy with </span>        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">control, providing features such as state management, event-driven execution, and control flow. The framework</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">includes tools for building and managing AI agent teams, including Flows, Crews, and autonomous </span>               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">collaboration. CrewAI is designed for enterprise-ready AI automation, with a focus on security, compliance, </span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">and reliability. The framework provides a range of features, including production-grade Flows, autonomous </span>     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Crews, flexible tools, and enterprise security. CrewAI is suitable for a variety of use cases, including </span>      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">simple automation, complex research, and application backends. The framework is extensible, allowing </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">developers to add new tools, roles, and capabilities as needed. CrewAI is also cost-efficient, optimized to </span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">minimize token usage and API calls. </span>                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Pricing information is not available on the provided webpage. </span>                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">The target audience for CrewAI includes developers, researchers, and enterprises looking to build and deploy </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">AI-powered applications. CrewAI provides a range of resources, including documentation, tutorials, and </span>        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">community support, to help users get started with the framework. </span>                                              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Main features of CrewAI include:</span>                                                                               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">1. Production-grade Flows: Build reliable, stateful workflows that can handle long-running processes and </span>      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">complex logic.</span>                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">2. Autonomous Crews: Deploy teams of agents that can plan, execute, and collaborate to achieve high-level </span>     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">goals.</span>                                                                                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">3. Flexible Tools: Connect your agents to any API, database, or local tool.</span>                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">4. Enterprise Security: Designed with security and compliance in mind for enterprise deployments.</span>              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Overall, CrewAI provides a powerful and flexible framework for building and deploying AI-powered </span>              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">applications, with a focus on autonomy, collaboration, and enterprise readiness.</span>                               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[32m╭─\u001b[0m\u001b[32m────────────────────────────────────────────\u001b[0m\u001b[32m ✅ Agent Final Answer \u001b[0m\u001b[32m────────────────────────────────────────────\u001b[0m\u001b[32m─╮\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mAgent: \u001b[0m\u001b[1;92mWebsite Content Analyst\u001b[0m                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mFinal Answer:\u001b[0m                                                                                                  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mCrewAI is an open-source framework for orchestrating autonomous AI agents and building complex workflows. It \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mempowers developers to build production-ready multi-agent systems by combining the collaborative intelligence\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mof Crews with the precise control of Flows. CrewAI's architecture is designed to balance autonomy with \u001b[0m        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mcontrol, providing features such as state management, event-driven execution, and control flow. The framework\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mincludes tools for building and managing AI agent teams, including Flows, Crews, and autonomous \u001b[0m               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mcollaboration. CrewAI is designed for enterprise-ready AI automation, with a focus on security, compliance, \u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mand reliability. The framework provides a range of features, including production-grade Flows, autonomous \u001b[0m     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mCrews, flexible tools, and enterprise security. CrewAI is suitable for a variety of use cases, including \u001b[0m      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92msimple automation, complex research, and application backends. The framework is extensible, allowing \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mdevelopers to add new tools, roles, and capabilities as needed. CrewAI is also cost-efficient, optimized to \u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mminimize token usage and API calls. \u001b[0m                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mPricing information is not available on the provided webpage. \u001b[0m                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mThe target audience for CrewAI includes developers, researchers, and enterprises looking to build and deploy \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mAI-powered applications. CrewAI provides a range of resources, including documentation, tutorials, and \u001b[0m        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mcommunity support, to help users get started with the framework. \u001b[0m                                              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mMain features of CrewAI include:\u001b[0m                                                                               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92m1. Production-grade Flows: Build reliable, stateful workflows that can handle long-running processes and \u001b[0m      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mcomplex logic.\u001b[0m                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92m2. Autonomous Crews: Deploy teams of agents that can plan, execute, and collaborate to achieve high-level \u001b[0m     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mgoals.\u001b[0m                                                                                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92m3. Flexible Tools: Connect your agents to any API, database, or local tool.\u001b[0m                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92m4. Enterprise Security: Designed with security and compliance in mind for enterprise deployments.\u001b[0m              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mOverall, CrewAI provides a powerful and flexible framework for building and deploying AI-powered \u001b[0m              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mapplications, with a focus on autonomy, collaboration, and enterprise readiness.\u001b[0m                               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">[</span>CrewAIEventsBus<span style=\"font-weight: bold\">]</span> Warning: Event pairing mismatch. <span style=\"color: #008000; text-decoration-color: #008000\">'agent_execution_completed'</span> closed <span style=\"color: #008000; text-decoration-color: #008000\">'llm_call_started'</span> <span style=\"font-weight: bold\">(</span>expected \n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">'agent_execution_started'</span><span style=\"font-weight: bold\">)</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1m[\u001b[0mCrewAIEventsBus\u001b[1m]\u001b[0m Warning: Event pairing mismatch. \u001b[32m'agent_execution_completed'\u001b[0m closed \u001b[32m'llm_call_started'\u001b[0m \u001b[1m(\u001b[0mexpected \n",
       "\u001b[32m'agent_execution_started'\u001b[0m\u001b[1m)\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">[</span>CrewAIEventsBus<span style=\"font-weight: bold\">]</span> Warning: Event pairing mismatch. <span style=\"color: #008000; text-decoration-color: #008000\">'task_completed'</span> closed <span style=\"color: #008000; text-decoration-color: #008000\">'agent_execution_started'</span> <span style=\"font-weight: bold\">(</span>expected \n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">'task_started'</span><span style=\"font-weight: bold\">)</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1m[\u001b[0mCrewAIEventsBus\u001b[1m]\u001b[0m Warning: Event pairing mismatch. \u001b[32m'task_completed'\u001b[0m closed \u001b[32m'agent_execution_started'\u001b[0m \u001b[1m(\u001b[0mexpected \n",
       "\u001b[32m'task_started'\u001b[0m\u001b[1m)\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008000; text-decoration-color: #008000\">╭────────────────────────────────────────────── 📋 Task Completion ───────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000; font-weight: bold\">Task Completed</span>                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Name: </span>                                                                                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    Scrape and analyze the given url</span>                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    url : https://docs.crewai.com/en/introduction</span>                                                              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    Steps:</span>                                                                                                     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    1. Use FirecrawlScrapeWebsiteTool to scrape the url</span>                                                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    2. Extract main product features and capabilities</span>                                                          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    3. Identify pricing information if available</span>                                                               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    4. Note primary use cases or target audience</span>                                                               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    5. Keep total response under 500 tokens</span>                                                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    </span>                                                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Agent: </span>                                                                                                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Website Content Analyst</span>                                                                                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[32m╭─\u001b[0m\u001b[32m─────────────────────────────────────────────\u001b[0m\u001b[32m 📋 Task Completion \u001b[0m\u001b[32m──────────────────────────────────────────────\u001b[0m\u001b[32m─╮\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[1;32mTask Completed\u001b[0m                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mName: \u001b[0m                                                                                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    Scrape and analyze the given url\u001b[0m                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    url : https://docs.crewai.com/en/introduction\u001b[0m                                                              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    Steps:\u001b[0m                                                                                                     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    1. Use FirecrawlScrapeWebsiteTool to scrape the url\u001b[0m                                                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    2. Extract main product features and capabilities\u001b[0m                                                          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    3. Identify pricing information if available\u001b[0m                                                               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    4. Note primary use cases or target audience\u001b[0m                                                               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    5. Keep total response under 500 tokens\u001b[0m                                                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    \u001b[0m                                                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mAgent: \u001b[0m                                                                                                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mWebsite Content Analyst\u001b[0m                                                                                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">[</span>CrewAIEventsBus<span style=\"font-weight: bold\">]</span> Warning: Event pairing mismatch. <span style=\"color: #008000; text-decoration-color: #008000\">'crew_kickoff_completed'</span> closed <span style=\"color: #008000; text-decoration-color: #008000\">'task_started'</span> <span style=\"font-weight: bold\">(</span>expected \n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">'crew_kickoff_started'</span><span style=\"font-weight: bold\">)</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1m[\u001b[0mCrewAIEventsBus\u001b[1m]\u001b[0m Warning: Event pairing mismatch. \u001b[32m'crew_kickoff_completed'\u001b[0m closed \u001b[32m'task_started'\u001b[0m \u001b[1m(\u001b[0mexpected \n",
       "\u001b[32m'crew_kickoff_started'\u001b[0m\u001b[1m)\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008000; text-decoration-color: #008000\">╭──────────────────────────────────────────────── Crew Completion ────────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000; font-weight: bold\">Crew Execution Completed</span>                                                                                       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Name: </span>                                                                                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">crew</span>                                                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">ID: </span>                                                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">404c49fd-3e45-4c56-9d66-455bc0a8b83b</span>                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Final Output: CrewAI is an open-source framework for orchestrating autonomous AI agents and building complex </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">workflows. It empowers developers to build production-ready multi-agent systems by combining the </span>              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">collaborative intelligence of Crews with the precise control of Flows. CrewAI's architecture is designed to </span>   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">balance autonomy with control, providing features such as state management, event-driven execution, and </span>       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">control flow. The framework includes tools for building and managing AI agent teams, including Flows, Crews, </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">and autonomous collaboration. CrewAI is designed for enterprise-ready AI automation, with a focus on </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">security, compliance, and reliability. The framework provides a range of features, including production-grade</span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Flows, autonomous Crews, flexible tools, and enterprise security. CrewAI is suitable for a variety of use </span>     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">cases, including simple automation, complex research, and application backends. The framework is extensible, </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">allowing developers to add new tools, roles, and capabilities as needed. CrewAI is also cost-efficient, </span>       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">optimized to minimize token usage and API calls. </span>                                                              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Pricing information is not available on the provided webpage. </span>                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">The target audience for CrewAI includes developers, researchers, and enterprises looking to build and deploy </span>  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">AI-powered applications. CrewAI provides a range of resources, including documentation, tutorials, and </span>        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">community support, to help users get started with the framework. </span>                                              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Main features of CrewAI include:</span>                                                                               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">1. Production-grade Flows: Build reliable, stateful workflows that can handle long-running processes and </span>      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">complex logic.</span>                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">2. Autonomous Crews: Deploy teams of agents that can plan, execute, and collaborate to achieve high-level </span>     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">goals.</span>                                                                                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">3. Flexible Tools: Connect your agents to any API, database, or local tool.</span>                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">4. Enterprise Security: Designed with security and compliance in mind for enterprise deployments.</span>              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Overall, CrewAI provides a powerful and flexible framework for building and deploying AI-powered </span>              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">applications, with a focus on autonomy, collaboration, and enterprise readiness.</span>                               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[32m╭─\u001b[0m\u001b[32m───────────────────────────────────────────────\u001b[0m\u001b[32m Crew Completion \u001b[0m\u001b[32m───────────────────────────────────────────────\u001b[0m\u001b[32m─╮\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[1;32mCrew Execution Completed\u001b[0m                                                                                       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mName: \u001b[0m                                                                                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mcrew\u001b[0m                                                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mID: \u001b[0m                                                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m404c49fd-3e45-4c56-9d66-455bc0a8b83b\u001b[0m                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mFinal Output: CrewAI is an open-source framework for orchestrating autonomous AI agents and building complex \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mworkflows. It empowers developers to build production-ready multi-agent systems by combining the \u001b[0m              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mcollaborative intelligence of Crews with the precise control of Flows. CrewAI's architecture is designed to \u001b[0m   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mbalance autonomy with control, providing features such as state management, event-driven execution, and \u001b[0m       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mcontrol flow. The framework includes tools for building and managing AI agent teams, including Flows, Crews, \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mand autonomous collaboration. CrewAI is designed for enterprise-ready AI automation, with a focus on \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37msecurity, compliance, and reliability. The framework provides a range of features, including production-grade\u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mFlows, autonomous Crews, flexible tools, and enterprise security. CrewAI is suitable for a variety of use \u001b[0m     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mcases, including simple automation, complex research, and application backends. The framework is extensible, \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mallowing developers to add new tools, roles, and capabilities as needed. CrewAI is also cost-efficient, \u001b[0m       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37moptimized to minimize token usage and API calls. \u001b[0m                                                              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mPricing information is not available on the provided webpage. \u001b[0m                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mThe target audience for CrewAI includes developers, researchers, and enterprises looking to build and deploy \u001b[0m  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mAI-powered applications. CrewAI provides a range of resources, including documentation, tutorials, and \u001b[0m        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mcommunity support, to help users get started with the framework. \u001b[0m                                              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mMain features of CrewAI include:\u001b[0m                                                                               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37m1. Production-grade Flows: Build reliable, stateful workflows that can handle long-running processes and \u001b[0m      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mcomplex logic.\u001b[0m                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37m2. Autonomous Crews: Deploy teams of agents that can plan, execute, and collaborate to achieve high-level \u001b[0m     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mgoals.\u001b[0m                                                                                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37m3. Flexible Tools: Connect your agents to any API, database, or local tool.\u001b[0m                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37m4. Enterprise Security: Designed with security and compliance in mind for enterprise deployments.\u001b[0m              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mOverall, CrewAI provides a powerful and flexible framework for building and deploying AI-powered \u001b[0m              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mapplications, with a focus on autonomy, collaboration, and enterprise readiness.\u001b[0m                               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CrewAI is an open-source framework for orchestrating autonomous AI agents and building complex workflows. It empowers developers to build production-ready multi-agent systems by combining the collaborative intelligence of Crews with the precise control of Flows. CrewAI's architecture is designed to balance autonomy with control, providing features such as state management, event-driven execution, and control flow. The framework includes tools for building and managing AI agent teams, including Flows, Crews, and autonomous collaboration. CrewAI is designed for enterprise-ready AI automation, with a focus on security, compliance, and reliability. The framework provides a range of features, including production-grade Flows, autonomous Crews, flexible tools, and enterprise security. CrewAI is suitable for a variety of use cases, including simple automation, complex research, and application backends. The framework is extensible, allowing developers to add new tools, roles, and capabilities as needed. CrewAI is also cost-efficient, optimized to minimize token usage and API calls. \n",
      "\n",
      "Pricing information is not available on the provided webpage. \n",
      "\n",
      "The target audience for CrewAI includes developers, researchers, and enterprises looking to build and deploy AI-powered applications. CrewAI provides a range of resources, including documentation, tutorials, and community support, to help users get started with the framework. \n",
      "\n",
      "Main features of CrewAI include:\n",
      "\n",
      "1. Production-grade Flows: Build reliable, stateful workflows that can handle long-running processes and complex logic.\n",
      "2. Autonomous Crews: Deploy teams of agents that can plan, execute, and collaborate to achieve high-level goals.\n",
      "3. Flexible Tools: Connect your agents to any API, database, or local tool.\n",
      "4. Enterprise Security: Designed with security and compliance in mind for enterprise deployments.\n",
      "\n",
      "Overall, CrewAI provides a powerful and flexible framework for building and deploying AI-powered applications, with a focus on autonomy, collaboration, and enterprise readiness.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #000080; text-decoration-color: #000080\">╭──────────────────────────────────────────────── Tracing Status ─────────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>                                                                                                                 <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  Info: Tracing is disabled.                                                                                     <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>                                                                                                                 <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  To enable tracing, do any one of these:                                                                        <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  • Set tracing=True in your Crew/Flow code                                                                      <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  • Set CREWAI_TRACING_ENABLED=true in your project's .env file                                                  <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  • Run: crewai traces enable                                                                                    <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>                                                                                                                 <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[34m╭─\u001b[0m\u001b[34m───────────────────────────────────────────────\u001b[0m\u001b[34m Tracing Status \u001b[0m\u001b[34m────────────────────────────────────────────────\u001b[0m\u001b[34m─╮\u001b[0m\n",
       "\u001b[34m│\u001b[0m                                                                                                                 \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  Info: Tracing is disabled.                                                                                     \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m                                                                                                                 \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  To enable tracing, do any one of these:                                                                        \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  • Set tracing=True in your Crew/Flow code                                                                      \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  • Set CREWAI_TRACING_ENABLED=true in your project's .env file                                                  \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  • Run: crewai traces enable                                                                                    \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m                                                                                                                 \u001b[34m│\u001b[0m\n",
       "\u001b[34m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "\u001b[36m┌─\u001b[0m\u001b[36m────────────────────────────\u001b[0m\u001b[36m \u001b[0m\u001b[1;36mExecution Traces\u001b[0m\u001b[36m \u001b[0m\u001b[36m─────────────────────────────\u001b[0m\u001b[36m─┐\u001b[0m\n",
      "\u001b[36m│\u001b[0m                                                                             \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[1;36m🔍 \u001b[0m\u001b[1;36mDetailed execution traces are available!\u001b[0m                                \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m                                                                             \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[37mView insights including:\u001b[0m                                                   \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[94m  • Agent decision-making process\u001b[0m                                          \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[94m  • Task execution flow and timing\u001b[0m                                         \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[94m  • Tool usage details\u001b[0m                                                     \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m                                                                             \u001b[36m│\u001b[0m\n",
      "\u001b[36m└─────────────────────────────────────────────────────────────────────────────┘\u001b[0m\n",
      "Would you like to view your execution traces? [y/N] (20s timeout): \n",
      "\n",
      "\u001b[34m┌─\u001b[0m\u001b[34m────────────────────────\u001b[0m\u001b[34m Tracing Preference Saved \u001b[0m\u001b[34m─────────────────────────\u001b[0m\u001b[34m─┐\u001b[0m\n",
      "\u001b[34m│\u001b[0m                                                                             \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  Info: Tracing has been disabled.                                           \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m                                                                             \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  Your preference has been saved. Future Crew/Flow executions will not       \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  collect traces.                                                            \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m                                                                             \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  To enable tracing later, do any one of these:                              \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  • Set tracing=True in your Crew/Flow code                                  \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  • Set CREWAI_TRACING_ENABLED=true in your project's .env file              \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  • Run: crewai traces enable                                                \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m                                                                             \u001b[34m│\u001b[0m\n",
      "\u001b[34m└─────────────────────────────────────────────────────────────────────────────┘\u001b[0m\n",
      "\n"
     ]
    }
   ],
   "source": [
    "result = main()\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b69078c6",
   "metadata": {},
   "source": [
    "# Custom Tools"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "f631a0e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "from crewai.tools import tool"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16768d94",
   "metadata": {},
   "outputs": [],
   "source": [
    "import fitz\n",
    "import re\n",
    "\n",
    "#result_as_answer=True\n",
    "\n",
    "# mandatory steps for defining custom tool\n",
    "# 1.python function\n",
    "# 2.tool docstring\n",
    "#3.define our own logic\n",
    "#4.tool decorator\n",
    "\n",
    "@tool(\"pdf extractor\")\n",
    "def pdf_extractor(path:str) -> str:\n",
    "    \"\"\"\n",
    "    Custom tool for extracting content and text from PDF or DOCX files.\n",
    "    Returns cleaned text content from the document.\n",
    "    \"\"\"\n",
    "    path = r\"D:\\Cewai\\CrewAI_Crash_Course_Youtube\\Tools_indepth_intuition\\resume.pdf\"\n",
    "    text_blocks = []\n",
    "    with fitz.open(path) as doc:\n",
    "        for page in doc:\n",
    "            text = page.get_text(\"text\").strip()\n",
    "            if text:\n",
    "                text_blocks.append(text)\n",
    "\n",
    "    paragraphs = []\n",
    "    for page_text in text_blocks:\n",
    "        chunks = re.split(r'\\n\\s*\\n', page_text)\n",
    "        for chunk in chunks:\n",
    "            clean = chunk.strip()\n",
    "            paragraphs.append(clean)\n",
    "    \n",
    "    result = \"\\n\\n\".join(paragraphs)\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "878874a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "resume_parser_agent = Agent(\n",
    "    role=\"Resume Parser\",\n",
    "    goal=\"Extract text content from resume documents using the pdf_extractor tool. \"\n",
    "         \"Read the document and return its contents accurately without modification.\"\n",
    "         \"strictly don't add any other unnescessary content\",\n",
    "    backstory=\"You are a document processing specialist. Your sole responsibility is to use \"\n",
    "              \"the pdf_extractor tool to read documents and extract their text content. \"\n",
    "              \"You do not add,modify, summarize, or interpret the content.\",\n",
    "    llm=llm,\n",
    "    max_iter=3,\n",
    "    verbose=True,\n",
    "    tools=[pdf_extractor],\n",
    "    allow_delegation=False\n",
    ")\n",
    "\n",
    "task1_parse_resume = Task(\n",
    "    description=\"\"\"\n",
    "    Use the pdf_extractor tool to load and extract all text content from the resume document.\n",
    "    \n",
    "    Instructions:\n",
    "    - Call the pdf_extractor tool to read the document\n",
    "    - striclty Extract all text content without any modification\n",
    "    - Return the complete raw resume text as extracted\n",
    "    - Don't add unnecessary content to the raw text keep in mind\n",
    "    Do NOT summarize, interpret, modify or add the extra content by youself to the text.\n",
    "    keep in your mind, your task is to parse the content not modifiying or adding extra content\",\n",
    "    \"\"\",\n",
    "    expected_output=\"Complete extracted resume text\",\n",
    "    agent=resume_parser_agent\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "1040efc3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main1():\n",
    "    crew = Crew(\n",
    "        agents = [resume_parser_agent],\n",
    "        tasks = [task1_parse_resume],\n",
    "        verbose = True\n",
    "    )\n",
    "    result = crew.kickoff()\n",
    "    return result\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5330fc9a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008080; text-decoration-color: #008080\">╭─────────────────────────────────────────── 🚀 Crew Execution Started ───────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>                                                                                                                 <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #008080; text-decoration-color: #008080; font-weight: bold\">Crew Execution Started</span>                                                                                         <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Name: </span>                                                                                                         <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #008080; text-decoration-color: #008080\">crew</span>                                                                                                           <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">ID: </span>                                                                                                           <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #008080; text-decoration-color: #008080\">a09a5605-3238-4261-8f1b-44cf15e2a595</span>                                                                           <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>                                                                                                                 <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>                                                                                                                 <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[36m╭─\u001b[0m\u001b[36m──────────────────────────────────────────\u001b[0m\u001b[36m 🚀 Crew Execution Started \u001b[0m\u001b[36m──────────────────────────────────────────\u001b[0m\u001b[36m─╮\u001b[0m\n",
       "\u001b[36m│\u001b[0m                                                                                                                 \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[1;36mCrew Execution Started\u001b[0m                                                                                         \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[37mName: \u001b[0m                                                                                                         \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[36mcrew\u001b[0m                                                                                                           \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[37mID: \u001b[0m                                                                                                           \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[36ma09a5605-3238-4261-8f1b-44cf15e2a595\u001b[0m                                                                           \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m                                                                                                                 \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m                                                                                                                 \u001b[36m│\u001b[0m\n",
       "\u001b[36m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #808000; text-decoration-color: #808000\">╭──────────────────────────────────────────────── 📋 Task Started ────────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000; font-weight: bold\">Task Started</span>                                                                                                   <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Name: </span>                                                                                                         <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    Use the pdf_extractor tool to load and extract all text content from the resume document.</span>                  <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    Instructions:</span>                                                                                              <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    - Call the pdf_extractor tool to read the document</span>                                                         <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    - striclty Extract all text content without any modification</span>                                               <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    - Return the complete raw resume text as extracted</span>                                                         <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    - Don't add unnecessary content to the raw text keep in mind</span>                                               <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    Do NOT summarize, interpret, modify or add the extra content by youself to the text.</span>                       <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    keep in your mind, your task is to parse the content not modifiying or adding extra content\",</span>              <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    </span>                                                                                                           <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">ID: </span><span style=\"color: #808000; text-decoration-color: #808000\">709190a0-2f75-41c9-9a2e-7513530bf230</span>                                                                       <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[33m╭─\u001b[0m\u001b[33m───────────────────────────────────────────────\u001b[0m\u001b[33m 📋 Task Started \u001b[0m\u001b[33m───────────────────────────────────────────────\u001b[0m\u001b[33m─╮\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[1;33mTask Started\u001b[0m                                                                                                   \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[37mName: \u001b[0m                                                                                                         \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    Use the pdf_extractor tool to load and extract all text content from the resume document.\u001b[0m                  \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    Instructions:\u001b[0m                                                                                              \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    - Call the pdf_extractor tool to read the document\u001b[0m                                                         \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    - striclty Extract all text content without any modification\u001b[0m                                               \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    - Return the complete raw resume text as extracted\u001b[0m                                                         \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    - Don't add unnecessary content to the raw text keep in mind\u001b[0m                                               \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    Do NOT summarize, interpret, modify or add the extra content by youself to the text.\u001b[0m                       \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    keep in your mind, your task is to parse the content not modifiying or adding extra content\",\u001b[0m              \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    \u001b[0m                                                                                                           \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[37mID: \u001b[0m\u001b[33m709190a0-2f75-41c9-9a2e-7513530bf230\u001b[0m                                                                       \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #800080; text-decoration-color: #800080\">╭─────────────────────────────────────────────── 🤖 Agent Started ────────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>                                                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Agent: </span><span style=\"color: #00ff00; text-decoration-color: #00ff00; font-weight: bold\">Resume Parser</span>                                                                                           <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>                                                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Task: </span>                                                                                                         <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    Use the pdf_extractor tool to load and extract all text content from the resume document.</span>                  <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>                                                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    Instructions:</span>                                                                                              <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    - Call the pdf_extractor tool to read the document</span>                                                         <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    - striclty Extract all text content without any modification</span>                                               <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    - Return the complete raw resume text as extracted</span>                                                         <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    - Don't add unnecessary content to the raw text keep in mind</span>                                               <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    Do NOT summarize, interpret, modify or add the extra content by youself to the text.</span>                       <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    keep in your mind, your task is to parse the content not modifiying or adding extra content\",</span>              <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    </span>                                                                                                           <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>                                                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[35m╭─\u001b[0m\u001b[35m──────────────────────────────────────────────\u001b[0m\u001b[35m 🤖 Agent Started \u001b[0m\u001b[35m───────────────────────────────────────────────\u001b[0m\u001b[35m─╮\u001b[0m\n",
       "\u001b[35m│\u001b[0m                                                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[37mAgent: \u001b[0m\u001b[1;92mResume Parser\u001b[0m                                                                                           \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m                                                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[37mTask: \u001b[0m                                                                                                         \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    Use the pdf_extractor tool to load and extract all text content from the resume document.\u001b[0m                  \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m                                                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    Instructions:\u001b[0m                                                                                              \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    - Call the pdf_extractor tool to read the document\u001b[0m                                                         \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    - striclty Extract all text content without any modification\u001b[0m                                               \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    - Return the complete raw resume text as extracted\u001b[0m                                                         \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    - Don't add unnecessary content to the raw text keep in mind\u001b[0m                                               \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    Do NOT summarize, interpret, modify or add the extra content by youself to the text.\u001b[0m                       \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    keep in your mind, your task is to parse the content not modifiying or adding extra content\",\u001b[0m              \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    \u001b[0m                                                                                                           \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m                                                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #808000; text-decoration-color: #808000\">╭──────────────────────────────────────── 🔧 Tool Execution Started (#4) ─────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Tool: </span><span style=\"color: #808000; text-decoration-color: #808000; font-weight: bold\">pdf_extractor</span>                                                                                            <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Args: </span><span style=\"color: #808000; text-decoration-color: #808000\">{'path': 'resume_document.pdf'}</span>                                                                          <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[33m╭─\u001b[0m\u001b[33m───────────────────────────────────────\u001b[0m\u001b[33m 🔧 Tool Execution Started (#4) \u001b[0m\u001b[33m────────────────────────────────────────\u001b[0m\u001b[33m─╮\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[37mTool: \u001b[0m\u001b[1;33mpdf_extractor\u001b[0m                                                                                            \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[37mArgs: \u001b[0m\u001b[33m{'path': 'resume_document.pdf'}\u001b[0m                                                                          \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[32mTool pdf_extractor executed with result: NITHISHKUMAR \n",
      "          +91 8610198658 | nkumar861019@gmail.com |github.com/nithishkumar86 \n",
      "TECHNICAL SKILLS \n",
      "Progamming Languages  :  Python, Java,C \n",
      "Web Frameworks & Libraries:  Fastapi, Flask, Html...\u001b[0m"
     ]
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008000; text-decoration-color: #008000\">╭─────────────────────────────────────── ✅ Tool Execution Completed (#4) ────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000; font-weight: bold\">Tool Completed</span>                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Tool: </span><span style=\"color: #008000; text-decoration-color: #008000; font-weight: bold\">pdf_extractor</span>                                                                                            <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Output: </span><span style=\"color: #008000; text-decoration-color: #008000\">NITHISHKUMAR </span>                                                                                          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">          +91 8610198658 | nkumar861019@gmail.com |github.com/nithishkumar86 </span>                                  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">TECHNICAL SKILLS </span>                                                                                              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Progamming Languages  :  Python, Java,C </span>                                                                       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Web Frameworks &amp; Libraries:  Fastapi, Flask, Html, CSS, Streamlit </span>                                             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Python Libraries: Pandas,Numpy,Seaborn,Matplotlib </span>                                                             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Traditional Databases: Mysql, Sqlite, Postgresql,Mongodb </span>                                                      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Machine Learning &amp; Deep Learning FrameWorks:  Scikit-Learn (Supervised &amp; Unsupervised), Tensorflow, </span>           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Pytorch, NLP, ANN, CNN,Opencv </span>                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Generative &amp; Agentic AI Frameworks: Langchain, Langsmith, Llama Index,Finetuning, Langgraph, Crewai, </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Agno, Langflow, Autogen,n8n, google adk, Langgraph, Crewai,Agno, Langflow, Autogen,n8n, google adk </span>            <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Generative AI Vectordatabases: FAISS, Chroma, Pinecone, Astradb </span>                                               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">AWS &amp; Deployments Tools :  Docker, Git, Jenkins, Sonarqube, Aws Lambda, S3 Bucket, AWS ECR,AWS Runer,  </span>        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">,Amazon Bedrocks, Amazon Sagemaker. </span>                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">EDUCATION </span>                                                                                                     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">University College Of Engineering, Tiruchirappalli</span>                                                             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Nov 2022 - Apr  2026 </span>                                                                                          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">B.Tech Information Technology  -  CGPA:  7.09 </span>                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">PROJECTS </span>                                                                                                      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">1.Insurance Premium Prediction System : Predicted insurance premium categories using </span>                          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">features like age, BMI, lifestyle, income, and occupation. Built data validation &amp; computed features </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">with Pydantic, trained models with scikit-learn, and exposed via FastAPI + Streamlit. Containerized </span>           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">with Docker and deployed on AWS ECR. </span>                                                                          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">2. Medical Chatbot (GenAI + AWS Deployed): AI-powered chatbot to solve medical-</span>                                <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">related queries in real-time. Built with Groq API, Pinecone, Flask, HTML/CSS, version-controlled using </span>        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Git, CI/CD automated with Jenkins, and Build scan with AquaTrivy. Deployed on AWS (Docker + ECR </span>               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">+ Runner) for scalable, production-ready use. Provides real-time medical guidance and symptom </span>                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">triage for users, suitable for telemedicine platforms. </span>                                                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">3. Bus Booking System with Agents (Agentic AI + AWS Deployed): Developed a </span>                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">CRUD-based bus booking platform with agent workflows for easy reservation. Built using FastAPI, </span>               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Streamlit, PostgreSQL, with Pydantic for data validation, version-controlled with Git, and CI/CD </span>              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">automated via Jenkins with SonarQube integration. Enables users to manage bookings efficiently, </span>               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">ideal for transport platforms or travel apps. Deployed on AWS (Docker + ECR + Fargate) for scalable, </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">production-ready use. </span>                                                                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">4. Data Analyst &amp; Report Generator (CrewAI + GenAI): Built an AI-powered tool to analyze </span>                      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">datasets and generate executive reports automatically. Implemented using CrewAI, OpenRouter API </span>               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">LangSmith, ElevenLabs (voice-over), for multi-modal outputs. Streamlit used for interactive frontend </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">UI, visualizations created with pandas, matplotlib, seaborn, version-controlled with Git. </span>                     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">CERTIFICATION </span>                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Complete  Generative AI Course With LangChain and HuggingFace – Udemy </span>                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Building Agentic RAG For VectorDB -KrishAI Technologies</span>                                                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[32m╭─\u001b[0m\u001b[32m──────────────────────────────────────\u001b[0m\u001b[32m ✅ Tool Execution Completed (#4) \u001b[0m\u001b[32m───────────────────────────────────────\u001b[0m\u001b[32m─╮\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[1;32mTool Completed\u001b[0m                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mTool: \u001b[0m\u001b[1;32mpdf_extractor\u001b[0m                                                                                            \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mOutput: \u001b[0m\u001b[32mNITHISHKUMAR \u001b[0m                                                                                          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m          +91 8610198658 | nkumar861019@gmail.com |github.com/nithishkumar86 \u001b[0m                                  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mTECHNICAL SKILLS \u001b[0m                                                                                              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mProgamming Languages  :  Python, Java,C \u001b[0m                                                                       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mWeb Frameworks & Libraries:  Fastapi, Flask, Html, CSS, Streamlit \u001b[0m                                             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mPython Libraries: Pandas,Numpy,Seaborn,Matplotlib \u001b[0m                                                             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mTraditional Databases: Mysql, Sqlite, Postgresql,Mongodb \u001b[0m                                                      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mMachine Learning & Deep Learning FrameWorks:  Scikit-Learn (Supervised & Unsupervised), Tensorflow, \u001b[0m           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mPytorch, NLP, ANN, CNN,Opencv \u001b[0m                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mGenerative & Agentic AI Frameworks: Langchain, Langsmith, Llama Index,Finetuning, Langgraph, Crewai, \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mAgno, Langflow, Autogen,n8n, google adk, Langgraph, Crewai,Agno, Langflow, Autogen,n8n, google adk \u001b[0m            \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mGenerative AI Vectordatabases: FAISS, Chroma, Pinecone, Astradb \u001b[0m                                               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mAWS & Deployments Tools :  Docker, Git, Jenkins, Sonarqube, Aws Lambda, S3 Bucket, AWS ECR,AWS Runer,  \u001b[0m        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m,Amazon Bedrocks, Amazon Sagemaker. \u001b[0m                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mEDUCATION \u001b[0m                                                                                                     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mUniversity College Of Engineering, Tiruchirappalli\u001b[0m                                                             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mNov 2022 - Apr  2026 \u001b[0m                                                                                          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mB.Tech Information Technology  -  CGPA:  7.09 \u001b[0m                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mPROJECTS \u001b[0m                                                                                                      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m1.Insurance Premium Prediction System : Predicted insurance premium categories using \u001b[0m                          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mfeatures like age, BMI, lifestyle, income, and occupation. Built data validation & computed features \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mwith Pydantic, trained models with scikit-learn, and exposed via FastAPI + Streamlit. Containerized \u001b[0m           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mwith Docker and deployed on AWS ECR. \u001b[0m                                                                          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m2. Medical Chatbot (GenAI + AWS Deployed): AI-powered chatbot to solve medical-\u001b[0m                                \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mrelated queries in real-time. Built with Groq API, Pinecone, Flask, HTML/CSS, version-controlled using \u001b[0m        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mGit, CI/CD automated with Jenkins, and Build scan with AquaTrivy. Deployed on AWS (Docker + ECR \u001b[0m               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m+ Runner) for scalable, production-ready use. Provides real-time medical guidance and symptom \u001b[0m                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mtriage for users, suitable for telemedicine platforms. \u001b[0m                                                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m3. Bus Booking System with Agents (Agentic AI + AWS Deployed): Developed a \u001b[0m                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mCRUD-based bus booking platform with agent workflows for easy reservation. Built using FastAPI, \u001b[0m               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mStreamlit, PostgreSQL, with Pydantic for data validation, version-controlled with Git, and CI/CD \u001b[0m              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mautomated via Jenkins with SonarQube integration. Enables users to manage bookings efficiently, \u001b[0m               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mideal for transport platforms or travel apps. Deployed on AWS (Docker + ECR + Fargate) for scalable, \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mproduction-ready use. \u001b[0m                                                                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m4. Data Analyst & Report Generator (CrewAI + GenAI): Built an AI-powered tool to analyze \u001b[0m                      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mdatasets and generate executive reports automatically. Implemented using CrewAI, OpenRouter API \u001b[0m               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mLangSmith, ElevenLabs (voice-over), for multi-modal outputs. Streamlit used for interactive frontend \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mUI, visualizations created with pandas, matplotlib, seaborn, version-controlled with Git. \u001b[0m                     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mCERTIFICATION \u001b[0m                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mComplete  Generative AI Course With LangChain and HuggingFace – Udemy \u001b[0m                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mBuilding Agentic RAG For VectorDB -KrishAI Technologies\u001b[0m                                                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008000; text-decoration-color: #008000\">╭───────────────────────────────────────────── ✅ Agent Final Answer ─────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Agent: </span><span style=\"color: #00ff00; text-decoration-color: #00ff00; font-weight: bold\">Resume Parser</span>                                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Final Answer:</span>                                                                                                  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">NITHISHKUMAR </span>                                                                                                  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">          +91 8610198658 | nkumar861019@gmail.com |github.com/nithishkumar86 </span>                                  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">TECHNICAL SKILLS </span>                                                                                              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Progamming Languages  :  Python, Java,C </span>                                                                       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Web Frameworks &amp; Libraries:  Fastapi, Flask, Html, CSS, Streamlit </span>                                             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Python Libraries: Pandas,Numpy,Seaborn,Matplotlib </span>                                                             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Traditional Databases: Mysql, Sqlite, Postgresql,Mongodb </span>                                                      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Machine Learning &amp; Deep Learning FrameWorks:  Scikit-Learn (Supervised &amp; Unsupervised), Tensorflow, </span>           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Pytorch, NLP, ANN, CNN,Opencv </span>                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Generative &amp; Agentic AI Frameworks: Langchain, Langsmith, Llama Index,Finetuning, Langgraph, Crewai, </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Agno, Langflow, Autogen,n8n, google adk, Langgraph, Crewai,Agno, Langflow, Autogen,n8n, google adk </span>            <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Generative AI Vectordatabases: FAISS, Chroma, Pinecone, Astradb </span>                                               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">AWS &amp; Deployments Tools :  Docker, Git, Jenkins, Sonarqube, Aws Lambda, S3 Bucket, AWS ECR,AWS Runer,  </span>        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">,Amazon Bedrocks, Amazon Sagemaker. </span>                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">EDUCATION </span>                                                                                                     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">University College Of Engineering, Tiruchirappalli</span>                                                             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Nov 2022 - Apr  2026 </span>                                                                                          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">B.Tech Information Technology  -  CGPA:  7.09 </span>                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">PROJECTS </span>                                                                                                      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">1.Insurance Premium Prediction System : Predicted insurance premium categories using </span>                          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">features like age, BMI, lifestyle, income, and occupation. Built data validation &amp; computed features </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">with Pydantic, trained models with scikit-learn, and exposed via FastAPI + Streamlit. Containerized </span>           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">with Docker and deployed on AWS ECR. </span>                                                                          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">2. Medical Chatbot (GenAI + AWS Deployed): AI-powered chatbot to solve medical-</span>                                <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">related queries in real-time. Built with Groq API, Pinecone, Flask, HTML/CSS, version-controlled using </span>        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Git, CI/CD automated with Jenkins, and Build scan with AquaTrivy. Deployed on AWS (Docker + ECR </span>               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">+ Runner) for scalable, production-ready use. Provides real-time medical guidance and symptom </span>                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">triage for users, suitable for telemedicine platforms. </span>                                                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">3. Bus Booking System with Agents (Agentic AI + AWS Deployed): Developed a </span>                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">CRUD-based bus booking platform with agent workflows for easy reservation. Built using FastAPI, </span>               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Streamlit, PostgreSQL, with Pydantic for data validation, version-controlled with Git, and CI/CD </span>              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">automated via Jenkins with SonarQube integration. Enables users to manage bookings efficiently, </span>               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">ideal for transport platforms or travel apps. Deployed on AWS (Docker + ECR + Fargate) for scalable, </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">production-ready use. </span>                                                                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">4. Data Analyst &amp; Report Generator (CrewAI + GenAI): Built an AI-powered tool to analyze </span>                      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">datasets and generate executive reports automatically. Implemented using CrewAI, OpenRouter API </span>               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">LangSmith, ElevenLabs (voice-over), for multi-modal outputs. Streamlit used for interactive frontend </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">UI, visualizations created with pandas, matplotlib, seaborn, version-controlled with Git. </span>                     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">CERTIFICATION </span>                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Complete  Generative AI Course With LangChain and HuggingFace – Udemy </span>                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">Building Agentic RAG For VectorDB -KrishAI Technologies</span>                                                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[32m╭─\u001b[0m\u001b[32m────────────────────────────────────────────\u001b[0m\u001b[32m ✅ Agent Final Answer \u001b[0m\u001b[32m────────────────────────────────────────────\u001b[0m\u001b[32m─╮\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mAgent: \u001b[0m\u001b[1;92mResume Parser\u001b[0m                                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mFinal Answer:\u001b[0m                                                                                                  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mNITHISHKUMAR \u001b[0m                                                                                                  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92m          +91 8610198658 | nkumar861019@gmail.com |github.com/nithishkumar86 \u001b[0m                                  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mTECHNICAL SKILLS \u001b[0m                                                                                              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mProgamming Languages  :  Python, Java,C \u001b[0m                                                                       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mWeb Frameworks & Libraries:  Fastapi, Flask, Html, CSS, Streamlit \u001b[0m                                             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mPython Libraries: Pandas,Numpy,Seaborn,Matplotlib \u001b[0m                                                             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mTraditional Databases: Mysql, Sqlite, Postgresql,Mongodb \u001b[0m                                                      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mMachine Learning & Deep Learning FrameWorks:  Scikit-Learn (Supervised & Unsupervised), Tensorflow, \u001b[0m           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mPytorch, NLP, ANN, CNN,Opencv \u001b[0m                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mGenerative & Agentic AI Frameworks: Langchain, Langsmith, Llama Index,Finetuning, Langgraph, Crewai, \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mAgno, Langflow, Autogen,n8n, google adk, Langgraph, Crewai,Agno, Langflow, Autogen,n8n, google adk \u001b[0m            \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mGenerative AI Vectordatabases: FAISS, Chroma, Pinecone, Astradb \u001b[0m                                               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mAWS & Deployments Tools :  Docker, Git, Jenkins, Sonarqube, Aws Lambda, S3 Bucket, AWS ECR,AWS Runer,  \u001b[0m        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92m,Amazon Bedrocks, Amazon Sagemaker. \u001b[0m                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mEDUCATION \u001b[0m                                                                                                     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mUniversity College Of Engineering, Tiruchirappalli\u001b[0m                                                             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mNov 2022 - Apr  2026 \u001b[0m                                                                                          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mB.Tech Information Technology  -  CGPA:  7.09 \u001b[0m                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mPROJECTS \u001b[0m                                                                                                      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92m1.Insurance Premium Prediction System : Predicted insurance premium categories using \u001b[0m                          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mfeatures like age, BMI, lifestyle, income, and occupation. Built data validation & computed features \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mwith Pydantic, trained models with scikit-learn, and exposed via FastAPI + Streamlit. Containerized \u001b[0m           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mwith Docker and deployed on AWS ECR. \u001b[0m                                                                          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92m2. Medical Chatbot (GenAI + AWS Deployed): AI-powered chatbot to solve medical-\u001b[0m                                \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mrelated queries in real-time. Built with Groq API, Pinecone, Flask, HTML/CSS, version-controlled using \u001b[0m        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mGit, CI/CD automated with Jenkins, and Build scan with AquaTrivy. Deployed on AWS (Docker + ECR \u001b[0m               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92m+ Runner) for scalable, production-ready use. Provides real-time medical guidance and symptom \u001b[0m                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mtriage for users, suitable for telemedicine platforms. \u001b[0m                                                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92m3. Bus Booking System with Agents (Agentic AI + AWS Deployed): Developed a \u001b[0m                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mCRUD-based bus booking platform with agent workflows for easy reservation. Built using FastAPI, \u001b[0m               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mStreamlit, PostgreSQL, with Pydantic for data validation, version-controlled with Git, and CI/CD \u001b[0m              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mautomated via Jenkins with SonarQube integration. Enables users to manage bookings efficiently, \u001b[0m               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mideal for transport platforms or travel apps. Deployed on AWS (Docker + ECR + Fargate) for scalable, \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mproduction-ready use. \u001b[0m                                                                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92m4. Data Analyst & Report Generator (CrewAI + GenAI): Built an AI-powered tool to analyze \u001b[0m                      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mdatasets and generate executive reports automatically. Implemented using CrewAI, OpenRouter API \u001b[0m               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mLangSmith, ElevenLabs (voice-over), for multi-modal outputs. Streamlit used for interactive frontend \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mUI, visualizations created with pandas, matplotlib, seaborn, version-controlled with Git. \u001b[0m                     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mCERTIFICATION \u001b[0m                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mComplete  Generative AI Course With LangChain and HuggingFace – Udemy \u001b[0m                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[92mBuilding Agentic RAG For VectorDB -KrishAI Technologies\u001b[0m                                                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">[</span>CrewAIEventsBus<span style=\"font-weight: bold\">]</span> Warning: Event pairing mismatch. <span style=\"color: #008000; text-decoration-color: #008000\">'agent_execution_completed'</span> closed <span style=\"color: #008000; text-decoration-color: #008000\">'llm_call_started'</span> <span style=\"font-weight: bold\">(</span>expected \n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">'agent_execution_started'</span><span style=\"font-weight: bold\">)</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1m[\u001b[0mCrewAIEventsBus\u001b[1m]\u001b[0m Warning: Event pairing mismatch. \u001b[32m'agent_execution_completed'\u001b[0m closed \u001b[32m'llm_call_started'\u001b[0m \u001b[1m(\u001b[0mexpected \n",
       "\u001b[32m'agent_execution_started'\u001b[0m\u001b[1m)\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">[</span>CrewAIEventsBus<span style=\"font-weight: bold\">]</span> Warning: Event pairing mismatch. <span style=\"color: #008000; text-decoration-color: #008000\">'task_completed'</span> closed <span style=\"color: #008000; text-decoration-color: #008000\">'agent_execution_started'</span> <span style=\"font-weight: bold\">(</span>expected \n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">'task_started'</span><span style=\"font-weight: bold\">)</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1m[\u001b[0mCrewAIEventsBus\u001b[1m]\u001b[0m Warning: Event pairing mismatch. \u001b[32m'task_completed'\u001b[0m closed \u001b[32m'agent_execution_started'\u001b[0m \u001b[1m(\u001b[0mexpected \n",
       "\u001b[32m'task_started'\u001b[0m\u001b[1m)\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008000; text-decoration-color: #008000\">╭────────────────────────────────────────────── 📋 Task Completion ───────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000; font-weight: bold\">Task Completed</span>                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Name: </span>                                                                                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    Use the pdf_extractor tool to load and extract all text content from the resume document.</span>                  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    Instructions:</span>                                                                                              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    - Call the pdf_extractor tool to read the document</span>                                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    - striclty Extract all text content without any modification</span>                                               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    - Return the complete raw resume text as extracted</span>                                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    - Don't add unnecessary content to the raw text keep in mind</span>                                               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    Do NOT summarize, interpret, modify or add the extra content by youself to the text.</span>                       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    keep in your mind, your task is to parse the content not modifiying or adding extra content\",</span>              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    </span>                                                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Agent: </span>                                                                                                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Resume Parser</span>                                                                                                  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[32m╭─\u001b[0m\u001b[32m─────────────────────────────────────────────\u001b[0m\u001b[32m 📋 Task Completion \u001b[0m\u001b[32m──────────────────────────────────────────────\u001b[0m\u001b[32m─╮\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[1;32mTask Completed\u001b[0m                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mName: \u001b[0m                                                                                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    Use the pdf_extractor tool to load and extract all text content from the resume document.\u001b[0m                  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    Instructions:\u001b[0m                                                                                              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    - Call the pdf_extractor tool to read the document\u001b[0m                                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    - striclty Extract all text content without any modification\u001b[0m                                               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    - Return the complete raw resume text as extracted\u001b[0m                                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    - Don't add unnecessary content to the raw text keep in mind\u001b[0m                                               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    Do NOT summarize, interpret, modify or add the extra content by youself to the text.\u001b[0m                       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    keep in your mind, your task is to parse the content not modifiying or adding extra content\",\u001b[0m              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    \u001b[0m                                                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mAgent: \u001b[0m                                                                                                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mResume Parser\u001b[0m                                                                                                  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">[</span>CrewAIEventsBus<span style=\"font-weight: bold\">]</span> Warning: Event pairing mismatch. <span style=\"color: #008000; text-decoration-color: #008000\">'crew_kickoff_completed'</span> closed <span style=\"color: #008000; text-decoration-color: #008000\">'task_started'</span> <span style=\"font-weight: bold\">(</span>expected \n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">'crew_kickoff_started'</span><span style=\"font-weight: bold\">)</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1m[\u001b[0mCrewAIEventsBus\u001b[1m]\u001b[0m Warning: Event pairing mismatch. \u001b[32m'crew_kickoff_completed'\u001b[0m closed \u001b[32m'task_started'\u001b[0m \u001b[1m(\u001b[0mexpected \n",
       "\u001b[32m'crew_kickoff_started'\u001b[0m\u001b[1m)\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008000; text-decoration-color: #008000\">╭──────────────────────────────────────────────── Crew Completion ────────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000; font-weight: bold\">Crew Execution Completed</span>                                                                                       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Name: </span>                                                                                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">crew</span>                                                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">ID: </span>                                                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">a09a5605-3238-4261-8f1b-44cf15e2a595</span>                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Final Output: NITHISHKUMAR </span>                                                                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">          +91 8610198658 | nkumar861019@gmail.com |github.com/nithishkumar86 </span>                                  <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">TECHNICAL SKILLS </span>                                                                                              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Progamming Languages  :  Python, Java,C </span>                                                                       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Web Frameworks &amp; Libraries:  Fastapi, Flask, Html, CSS, Streamlit </span>                                             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Python Libraries: Pandas,Numpy,Seaborn,Matplotlib </span>                                                             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Traditional Databases: Mysql, Sqlite, Postgresql,Mongodb </span>                                                      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Machine Learning &amp; Deep Learning FrameWorks:  Scikit-Learn (Supervised &amp; Unsupervised), Tensorflow, </span>           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Pytorch, NLP, ANN, CNN,Opencv </span>                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Generative &amp; Agentic AI Frameworks: Langchain, Langsmith, Llama Index,Finetuning, Langgraph, Crewai, </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Agno, Langflow, Autogen,n8n, google adk, Langgraph, Crewai,Agno, Langflow, Autogen,n8n, google adk </span>            <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Generative AI Vectordatabases: FAISS, Chroma, Pinecone, Astradb </span>                                               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">AWS &amp; Deployments Tools :  Docker, Git, Jenkins, Sonarqube, Aws Lambda, S3 Bucket, AWS ECR,AWS Runer,  </span>        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">,Amazon Bedrocks, Amazon Sagemaker. </span>                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">EDUCATION </span>                                                                                                     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">University College Of Engineering, Tiruchirappalli</span>                                                             <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Nov 2022 - Apr  2026 </span>                                                                                          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">B.Tech Information Technology  -  CGPA:  7.09 </span>                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">PROJECTS </span>                                                                                                      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">1.Insurance Premium Prediction System : Predicted insurance premium categories using </span>                          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">features like age, BMI, lifestyle, income, and occupation. Built data validation &amp; computed features </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">with Pydantic, trained models with scikit-learn, and exposed via FastAPI + Streamlit. Containerized </span>           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">with Docker and deployed on AWS ECR. </span>                                                                          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">2. Medical Chatbot (GenAI + AWS Deployed): AI-powered chatbot to solve medical-</span>                                <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">related queries in real-time. Built with Groq API, Pinecone, Flask, HTML/CSS, version-controlled using </span>        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Git, CI/CD automated with Jenkins, and Build scan with AquaTrivy. Deployed on AWS (Docker + ECR </span>               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">+ Runner) for scalable, production-ready use. Provides real-time medical guidance and symptom </span>                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">triage for users, suitable for telemedicine platforms. </span>                                                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">3. Bus Booking System with Agents (Agentic AI + AWS Deployed): Developed a </span>                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">CRUD-based bus booking platform with agent workflows for easy reservation. Built using FastAPI, </span>               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Streamlit, PostgreSQL, with Pydantic for data validation, version-controlled with Git, and CI/CD </span>              <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">automated via Jenkins with SonarQube integration. Enables users to manage bookings efficiently, </span>               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">ideal for transport platforms or travel apps. Deployed on AWS (Docker + ECR + Fargate) for scalable, </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">production-ready use. </span>                                                                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">4. Data Analyst &amp; Report Generator (CrewAI + GenAI): Built an AI-powered tool to analyze </span>                      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">datasets and generate executive reports automatically. Implemented using CrewAI, OpenRouter API </span>               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">LangSmith, ElevenLabs (voice-over), for multi-modal outputs. Streamlit used for interactive frontend </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">UI, visualizations created with pandas, matplotlib, seaborn, version-controlled with Git. </span>                     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">CERTIFICATION </span>                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Complete  Generative AI Course With LangChain and HuggingFace – Udemy </span>                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Building Agentic RAG For VectorDB -KrishAI Technologies</span>                                                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[32m╭─\u001b[0m\u001b[32m───────────────────────────────────────────────\u001b[0m\u001b[32m Crew Completion \u001b[0m\u001b[32m───────────────────────────────────────────────\u001b[0m\u001b[32m─╮\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[1;32mCrew Execution Completed\u001b[0m                                                                                       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mName: \u001b[0m                                                                                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mcrew\u001b[0m                                                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mID: \u001b[0m                                                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32ma09a5605-3238-4261-8f1b-44cf15e2a595\u001b[0m                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mFinal Output: NITHISHKUMAR \u001b[0m                                                                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37m          +91 8610198658 | nkumar861019@gmail.com |github.com/nithishkumar86 \u001b[0m                                  \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mTECHNICAL SKILLS \u001b[0m                                                                                              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mProgamming Languages  :  Python, Java,C \u001b[0m                                                                       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mWeb Frameworks & Libraries:  Fastapi, Flask, Html, CSS, Streamlit \u001b[0m                                             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mPython Libraries: Pandas,Numpy,Seaborn,Matplotlib \u001b[0m                                                             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mTraditional Databases: Mysql, Sqlite, Postgresql,Mongodb \u001b[0m                                                      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mMachine Learning & Deep Learning FrameWorks:  Scikit-Learn (Supervised & Unsupervised), Tensorflow, \u001b[0m           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mPytorch, NLP, ANN, CNN,Opencv \u001b[0m                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mGenerative & Agentic AI Frameworks: Langchain, Langsmith, Llama Index,Finetuning, Langgraph, Crewai, \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mAgno, Langflow, Autogen,n8n, google adk, Langgraph, Crewai,Agno, Langflow, Autogen,n8n, google adk \u001b[0m            \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mGenerative AI Vectordatabases: FAISS, Chroma, Pinecone, Astradb \u001b[0m                                               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mAWS & Deployments Tools :  Docker, Git, Jenkins, Sonarqube, Aws Lambda, S3 Bucket, AWS ECR,AWS Runer,  \u001b[0m        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37m,Amazon Bedrocks, Amazon Sagemaker. \u001b[0m                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mEDUCATION \u001b[0m                                                                                                     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mUniversity College Of Engineering, Tiruchirappalli\u001b[0m                                                             \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mNov 2022 - Apr  2026 \u001b[0m                                                                                          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mB.Tech Information Technology  -  CGPA:  7.09 \u001b[0m                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mPROJECTS \u001b[0m                                                                                                      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37m1.Insurance Premium Prediction System : Predicted insurance premium categories using \u001b[0m                          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mfeatures like age, BMI, lifestyle, income, and occupation. Built data validation & computed features \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mwith Pydantic, trained models with scikit-learn, and exposed via FastAPI + Streamlit. Containerized \u001b[0m           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mwith Docker and deployed on AWS ECR. \u001b[0m                                                                          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37m2. Medical Chatbot (GenAI + AWS Deployed): AI-powered chatbot to solve medical-\u001b[0m                                \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mrelated queries in real-time. Built with Groq API, Pinecone, Flask, HTML/CSS, version-controlled using \u001b[0m        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mGit, CI/CD automated with Jenkins, and Build scan with AquaTrivy. Deployed on AWS (Docker + ECR \u001b[0m               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37m+ Runner) for scalable, production-ready use. Provides real-time medical guidance and symptom \u001b[0m                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mtriage for users, suitable for telemedicine platforms. \u001b[0m                                                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37m3. Bus Booking System with Agents (Agentic AI + AWS Deployed): Developed a \u001b[0m                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mCRUD-based bus booking platform with agent workflows for easy reservation. Built using FastAPI, \u001b[0m               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mStreamlit, PostgreSQL, with Pydantic for data validation, version-controlled with Git, and CI/CD \u001b[0m              \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mautomated via Jenkins with SonarQube integration. Enables users to manage bookings efficiently, \u001b[0m               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mideal for transport platforms or travel apps. Deployed on AWS (Docker + ECR + Fargate) for scalable, \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mproduction-ready use. \u001b[0m                                                                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37m4. Data Analyst & Report Generator (CrewAI + GenAI): Built an AI-powered tool to analyze \u001b[0m                      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mdatasets and generate executive reports automatically. Implemented using CrewAI, OpenRouter API \u001b[0m               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mLangSmith, ElevenLabs (voice-over), for multi-modal outputs. Streamlit used for interactive frontend \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mUI, visualizations created with pandas, matplotlib, seaborn, version-controlled with Git. \u001b[0m                     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mCERTIFICATION \u001b[0m                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mComplete  Generative AI Course With LangChain and HuggingFace – Udemy \u001b[0m                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mBuilding Agentic RAG For VectorDB -KrishAI Technologies\u001b[0m                                                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NITHISHKUMAR \n",
      "          +91 8610198658 | nkumar861019@gmail.com |github.com/nithishkumar86 \n",
      "TECHNICAL SKILLS \n",
      "Progamming Languages  :  Python, Java,C \n",
      "Web Frameworks & Libraries:  Fastapi, Flask, Html, CSS, Streamlit \n",
      "Python Libraries: Pandas,Numpy,Seaborn,Matplotlib \n",
      "Traditional Databases: Mysql, Sqlite, Postgresql,Mongodb \n",
      "Machine Learning & Deep Learning FrameWorks:  Scikit-Learn (Supervised & Unsupervised), Tensorflow, \n",
      "Pytorch, NLP, ANN, CNN,Opencv \n",
      "Generative & Agentic AI Frameworks: Langchain, Langsmith, Llama Index,Finetuning, Langgraph, Crewai, \n",
      "Agno, Langflow, Autogen,n8n, google adk, Langgraph, Crewai,Agno, Langflow, Autogen,n8n, google adk \n",
      "Generative AI Vectordatabases: FAISS, Chroma, Pinecone, Astradb \n",
      "AWS & Deployments Tools :  Docker, Git, Jenkins, Sonarqube, Aws Lambda, S3 Bucket, AWS ECR,AWS Runer,  \n",
      ",Amazon Bedrocks, Amazon Sagemaker. \n",
      "EDUCATION \n",
      "University College Of Engineering, Tiruchirappalli\n",
      "\n",
      "Nov 2022 - Apr  2026 \n",
      "B.Tech Information Technology  -  CGPA:  7.09 \n",
      "PROJECTS \n",
      "1.Insurance Premium Prediction System : Predicted insurance premium categories using \n",
      "features like age, BMI, lifestyle, income, and occupation. Built data validation & computed features \n",
      "with Pydantic, trained models with scikit-learn, and exposed via FastAPI + Streamlit. Containerized \n",
      "with Docker and deployed on AWS ECR. \n",
      "2. Medical Chatbot (GenAI + AWS Deployed): AI-powered chatbot to solve medical-\n",
      "related queries in real-time. Built with Groq API, Pinecone, Flask, HTML/CSS, version-controlled using \n",
      "Git, CI/CD automated with Jenkins, and Build scan with AquaTrivy. Deployed on AWS (Docker + ECR \n",
      "+ Runner) for scalable, production-ready use. Provides real-time medical guidance and symptom \n",
      "triage for users, suitable for telemedicine platforms. \n",
      "3. Bus Booking System with Agents (Agentic AI + AWS Deployed): Developed a \n",
      "CRUD-based bus booking platform with agent workflows for easy reservation. Built using FastAPI, \n",
      "Streamlit, PostgreSQL, with Pydantic for data validation, version-controlled with Git, and CI/CD \n",
      "automated via Jenkins with SonarQube integration. Enables users to manage bookings efficiently, \n",
      "ideal for transport platforms or travel apps. Deployed on AWS (Docker + ECR + Fargate) for scalable, \n",
      "production-ready use. \n",
      "4. Data Analyst & Report Generator (CrewAI + GenAI): Built an AI-powered tool to analyze \n",
      "datasets and generate executive reports automatically. Implemented using CrewAI, OpenRouter API \n",
      "LangSmith, ElevenLabs (voice-over), for multi-modal outputs. Streamlit used for interactive frontend \n",
      "UI, visualizations created with pandas, matplotlib, seaborn, version-controlled with Git. \n",
      "CERTIFICATION \n",
      "Complete  Generative AI Course With LangChain and HuggingFace – Udemy \n",
      "Building Agentic RAG For VectorDB -KrishAI Technologies\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #000080; text-decoration-color: #000080\">╭──────────────────────────────────────────────── Tracing Status ─────────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>                                                                                                                 <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  Info: Tracing is disabled.                                                                                     <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>                                                                                                                 <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  To enable tracing, do any one of these:                                                                        <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  • Set tracing=True in your Crew/Flow code                                                                      <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  • Set CREWAI_TRACING_ENABLED=true in your project's .env file                                                  <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  • Run: crewai traces enable                                                                                    <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>                                                                                                                 <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[34m╭─\u001b[0m\u001b[34m───────────────────────────────────────────────\u001b[0m\u001b[34m Tracing Status \u001b[0m\u001b[34m────────────────────────────────────────────────\u001b[0m\u001b[34m─╮\u001b[0m\n",
       "\u001b[34m│\u001b[0m                                                                                                                 \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  Info: Tracing is disabled.                                                                                     \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m                                                                                                                 \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  To enable tracing, do any one of these:                                                                        \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  • Set tracing=True in your Crew/Flow code                                                                      \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  • Set CREWAI_TRACING_ENABLED=true in your project's .env file                                                  \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  • Run: crewai traces enable                                                                                    \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m                                                                                                                 \u001b[34m│\u001b[0m\n",
       "\u001b[34m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "\u001b[36m┌─\u001b[0m\u001b[36m────────────────────────────\u001b[0m\u001b[36m \u001b[0m\u001b[1;36mExecution Traces\u001b[0m\u001b[36m \u001b[0m\u001b[36m─────────────────────────────\u001b[0m\u001b[36m─┐\u001b[0m\n",
      "\u001b[36m│\u001b[0m                                                                             \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[1;36m🔍 \u001b[0m\u001b[1;36mDetailed execution traces are available!\u001b[0m                                \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m                                                                             \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[37mView insights including:\u001b[0m                                                   \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[94m  • Agent decision-making process\u001b[0m                                          \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[94m  • Task execution flow and timing\u001b[0m                                         \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[94m  • Tool usage details\u001b[0m                                                     \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m                                                                             \u001b[36m│\u001b[0m\n",
      "\u001b[36m└─────────────────────────────────────────────────────────────────────────────┘\u001b[0m\n",
      "Would you like to view your execution traces? [y/N] (20s timeout): \n",
      "\n",
      "\u001b[34m┌─\u001b[0m\u001b[34m────────────────────────\u001b[0m\u001b[34m Tracing Preference Saved \u001b[0m\u001b[34m─────────────────────────\u001b[0m\u001b[34m─┐\u001b[0m\n",
      "\u001b[34m│\u001b[0m                                                                             \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  Info: Tracing has been disabled.                                           \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m                                                                             \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  Your preference has been saved. Future Crew/Flow executions will not       \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  collect traces.                                                            \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m                                                                             \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  To enable tracing later, do any one of these:                              \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  • Set tracing=True in your Crew/Flow code                                  \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  • Set CREWAI_TRACING_ENABLED=true in your project's .env file              \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  • Run: crewai traces enable                                                \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m                                                                             \u001b[34m│\u001b[0m\n",
      "\u001b[34m└─────────────────────────────────────────────────────────────────────────────┘\u001b[0m\n",
      "\n"
     ]
    }
   ],
   "source": [
    "result  = main1()\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "90b86098",
   "metadata": {},
   "source": [
    "# Third Party Tools"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "967a4839",
   "metadata": {},
   "outputs": [],
   "source": [
    "from crewai import Agent, Task\n",
    "from langchain_community.tools.pubmed.tool import PubmedQueryRun #epecifically for medical related\n",
    "from crewai.tools import tool"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "47fa7b60",
   "metadata": {},
   "outputs": [],
   "source": [
    "# CrewAI-native tools (decorated with @tool)\n",
    "\n",
    "# mandatory steps for defining custom tool\n",
    "# 1.python function\n",
    "# 2.tool docstring\n",
    "# 3.initialize the the third party tool\n",
    "#tool decorator\n",
    "\n",
    "@tool(result_as_answer=True)\n",
    "def pubmed_search(query: str) -> str:\n",
    "    \"\"\"Search PubMed database for medical research articles.\"\"\"\n",
    "    pubmed = PubmedQueryRun()\n",
    "    return pubmed.run(query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "68bc62c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create an agent with clear instructions\n",
    "medical_researcher = Agent(\n",
    "    role='Medical Research Analyst',\n",
    "    goal='Search PubMed database for the latest peer-reviewed research on specific diseases, treatments, and medical conditions.',\n",
    "    backstory='Clinical research specialist with 8 years of experience analyzing medical literature and synthesizing findings from peer-reviewed journals.',\n",
    "    llm=llm,\n",
    "    tools=[pubmed_search],\n",
    "    verbose=True,\n",
    "    max_tokens=500\n",
    ")\n",
    "\n",
    "# Create a task with specific requirements\n",
    "research_task = Task(\n",
    "    description=\"\"\"\n",
    "    User Question :\n",
    "    {disease}\n",
    "    \n",
    "    Steps:\n",
    "    1. Use the PubMed tool to search for user given disease\"\n",
    "    2. Focus on recent publications and clinical findings\n",
    "    3. Identify key findings on causes, symptoms, or treatments\n",
    "    4. Summarize the most relevant research findings\n",
    "    5. Keep total response under 500 tokens\n",
    "    \"\"\",\n",
    "    expected_output='A concise medical research summary including: disease overview, recent findings, current treatment approaches, and key takeaways from peer-reviewed sources. Maximum 500 tokens total.',\n",
    "    agent=medical_researcher\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "5082f8fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main2():\n",
    "    crew = Crew(\n",
    "        agents = [medical_researcher],\n",
    "        tasks = [research_task],\n",
    "        verbose = True\n",
    "    )\n",
    "    result = crew.kickoff(inputs={\"disease\":\"severe fever\"})\n",
    "    return result\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "47ab4c22",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008080; text-decoration-color: #008080\">╭─────────────────────────────────────────── 🚀 Crew Execution Started ───────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>                                                                                                                 <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #008080; text-decoration-color: #008080; font-weight: bold\">Crew Execution Started</span>                                                                                         <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Name: </span>                                                                                                         <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #008080; text-decoration-color: #008080\">crew</span>                                                                                                           <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">ID: </span>                                                                                                           <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>  <span style=\"color: #008080; text-decoration-color: #008080\">002d1c23-17bc-4515-8980-bc967b1d38e1</span>                                                                           <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>                                                                                                                 <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">│</span>                                                                                                                 <span style=\"color: #008080; text-decoration-color: #008080\">│</span>\n",
       "<span style=\"color: #008080; text-decoration-color: #008080\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[36m╭─\u001b[0m\u001b[36m──────────────────────────────────────────\u001b[0m\u001b[36m 🚀 Crew Execution Started \u001b[0m\u001b[36m──────────────────────────────────────────\u001b[0m\u001b[36m─╮\u001b[0m\n",
       "\u001b[36m│\u001b[0m                                                                                                                 \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[1;36mCrew Execution Started\u001b[0m                                                                                         \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[37mName: \u001b[0m                                                                                                         \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[36mcrew\u001b[0m                                                                                                           \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[37mID: \u001b[0m                                                                                                           \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m  \u001b[36m002d1c23-17bc-4515-8980-bc967b1d38e1\u001b[0m                                                                           \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m                                                                                                                 \u001b[36m│\u001b[0m\n",
       "\u001b[36m│\u001b[0m                                                                                                                 \u001b[36m│\u001b[0m\n",
       "\u001b[36m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #808000; text-decoration-color: #808000\">╭──────────────────────────────────────────────── 📋 Task Started ────────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000; font-weight: bold\">Task Started</span>                                                                                                   <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Name: </span>                                                                                                         <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    User Question :</span>                                                                                            <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    severe fever</span>                                                                                               <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    Steps:</span>                                                                                                     <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    1. Use the PubMed tool to search for user given disease\"</span>                                                   <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    2. Focus on recent publications and clinical findings</span>                                                      <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    3. Identify key findings on causes, symptoms, or treatments</span>                                                <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    4. Summarize the most relevant research findings</span>                                                           <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    5. Keep total response under 500 tokens</span>                                                                    <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #808000; text-decoration-color: #808000\">    </span>                                                                                                           <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">ID: </span><span style=\"color: #808000; text-decoration-color: #808000\">3894a4b0-f863-4f27-96ee-768af7fb1a51</span>                                                                       <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[33m╭─\u001b[0m\u001b[33m───────────────────────────────────────────────\u001b[0m\u001b[33m 📋 Task Started \u001b[0m\u001b[33m───────────────────────────────────────────────\u001b[0m\u001b[33m─╮\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[1;33mTask Started\u001b[0m                                                                                                   \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[37mName: \u001b[0m                                                                                                         \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    User Question :\u001b[0m                                                                                            \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    severe fever\u001b[0m                                                                                               \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    Steps:\u001b[0m                                                                                                     \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    1. Use the PubMed tool to search for user given disease\"\u001b[0m                                                   \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    2. Focus on recent publications and clinical findings\u001b[0m                                                      \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    3. Identify key findings on causes, symptoms, or treatments\u001b[0m                                                \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    4. Summarize the most relevant research findings\u001b[0m                                                           \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    5. Keep total response under 500 tokens\u001b[0m                                                                    \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[33m    \u001b[0m                                                                                                           \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[37mID: \u001b[0m\u001b[33m3894a4b0-f863-4f27-96ee-768af7fb1a51\u001b[0m                                                                       \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #800080; text-decoration-color: #800080\">╭─────────────────────────────────────────────── 🤖 Agent Started ────────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>                                                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Agent: </span><span style=\"color: #00ff00; text-decoration-color: #00ff00; font-weight: bold\">Medical Research Analyst</span>                                                                                <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>                                                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Task: </span>                                                                                                         <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    User Question :</span>                                                                                            <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    severe fever</span>                                                                                               <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>                                                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    Steps:</span>                                                                                                     <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    1. Use the PubMed tool to search for user given disease\"</span>                                                   <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    2. Focus on recent publications and clinical findings</span>                                                      <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    3. Identify key findings on causes, symptoms, or treatments</span>                                                <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    4. Summarize the most relevant research findings</span>                                                           <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    5. Keep total response under 500 tokens</span>                                                                    <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>  <span style=\"color: #00ff00; text-decoration-color: #00ff00\">    </span>                                                                                                           <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">│</span>                                                                                                                 <span style=\"color: #800080; text-decoration-color: #800080\">│</span>\n",
       "<span style=\"color: #800080; text-decoration-color: #800080\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[35m╭─\u001b[0m\u001b[35m──────────────────────────────────────────────\u001b[0m\u001b[35m 🤖 Agent Started \u001b[0m\u001b[35m───────────────────────────────────────────────\u001b[0m\u001b[35m─╮\u001b[0m\n",
       "\u001b[35m│\u001b[0m                                                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[37mAgent: \u001b[0m\u001b[1;92mMedical Research Analyst\u001b[0m                                                                                \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m                                                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[37mTask: \u001b[0m                                                                                                         \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    User Question :\u001b[0m                                                                                            \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    severe fever\u001b[0m                                                                                               \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m                                                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    Steps:\u001b[0m                                                                                                     \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    1. Use the PubMed tool to search for user given disease\"\u001b[0m                                                   \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    2. Focus on recent publications and clinical findings\u001b[0m                                                      \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    3. Identify key findings on causes, symptoms, or treatments\u001b[0m                                                \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    4. Summarize the most relevant research findings\u001b[0m                                                           \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    5. Keep total response under 500 tokens\u001b[0m                                                                    \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m  \u001b[92m    \u001b[0m                                                                                                           \u001b[35m│\u001b[0m\n",
       "\u001b[35m│\u001b[0m                                                                                                                 \u001b[35m│\u001b[0m\n",
       "\u001b[35m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #808000; text-decoration-color: #808000\">╭──────────────────────────────────────── 🔧 Tool Execution Started (#2) ─────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Tool: </span><span style=\"color: #808000; text-decoration-color: #808000; font-weight: bold\">pubmed_search</span>                                                                                            <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Args: </span><span style=\"color: #808000; text-decoration-color: #808000\">{'query': 'severe fever'}</span>                                                                                <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">│</span>                                                                                                                 <span style=\"color: #808000; text-decoration-color: #808000\">│</span>\n",
       "<span style=\"color: #808000; text-decoration-color: #808000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[33m╭─\u001b[0m\u001b[33m───────────────────────────────────────\u001b[0m\u001b[33m 🔧 Tool Execution Started (#2) \u001b[0m\u001b[33m────────────────────────────────────────\u001b[0m\u001b[33m─╮\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[37mTool: \u001b[0m\u001b[1;33mpubmed_search\u001b[0m                                                                                            \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m  \u001b[37mArgs: \u001b[0m\u001b[33m{'query': 'severe fever'}\u001b[0m                                                                                \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m│\u001b[0m                                                                                                                 \u001b[33m│\u001b[0m\n",
       "\u001b[33m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[32mTool pubmed_search executed with result: PubMed exception: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1010)>...\u001b[0m\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008000; text-decoration-color: #008000\">╭─────────────────────────────────────── ✅ Tool Execution Completed (#2) ────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000; font-weight: bold\">Tool Completed</span>                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Tool: </span><span style=\"color: #008000; text-decoration-color: #008000; font-weight: bold\">pubmed_search</span>                                                                                            <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Output: </span><span style=\"color: #008000; text-decoration-color: #008000\">PubMed exception: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: </span>          <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">self-signed certificate in certificate chain (_ssl.c:1010)&gt;</span>                                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[32m╭─\u001b[0m\u001b[32m──────────────────────────────────────\u001b[0m\u001b[32m ✅ Tool Execution Completed (#2) \u001b[0m\u001b[32m───────────────────────────────────────\u001b[0m\u001b[32m─╮\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[1;32mTool Completed\u001b[0m                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mTool: \u001b[0m\u001b[1;32mpubmed_search\u001b[0m                                                                                            \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mOutput: \u001b[0m\u001b[32mPubMed exception: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: \u001b[0m          \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mself-signed certificate in certificate chain (_ssl.c:1010)>\u001b[0m                                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">[</span>CrewAIEventsBus<span style=\"font-weight: bold\">]</span> Warning: Event pairing mismatch. <span style=\"color: #008000; text-decoration-color: #008000\">'agent_execution_completed'</span> closed <span style=\"color: #008000; text-decoration-color: #008000\">'llm_call_started'</span> <span style=\"font-weight: bold\">(</span>expected \n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">'agent_execution_started'</span><span style=\"font-weight: bold\">)</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1m[\u001b[0mCrewAIEventsBus\u001b[1m]\u001b[0m Warning: Event pairing mismatch. \u001b[32m'agent_execution_completed'\u001b[0m closed \u001b[32m'llm_call_started'\u001b[0m \u001b[1m(\u001b[0mexpected \n",
       "\u001b[32m'agent_execution_started'\u001b[0m\u001b[1m)\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">[</span>CrewAIEventsBus<span style=\"font-weight: bold\">]</span> Warning: Event pairing mismatch. <span style=\"color: #008000; text-decoration-color: #008000\">'task_completed'</span> closed <span style=\"color: #008000; text-decoration-color: #008000\">'agent_execution_started'</span> <span style=\"font-weight: bold\">(</span>expected \n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">'task_started'</span><span style=\"font-weight: bold\">)</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1m[\u001b[0mCrewAIEventsBus\u001b[1m]\u001b[0m Warning: Event pairing mismatch. \u001b[32m'task_completed'\u001b[0m closed \u001b[32m'agent_execution_started'\u001b[0m \u001b[1m(\u001b[0mexpected \n",
       "\u001b[32m'task_started'\u001b[0m\u001b[1m)\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008000; text-decoration-color: #008000\">╭────────────────────────────────────────────── 📋 Task Completion ───────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000; font-weight: bold\">Task Completed</span>                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Name: </span>                                                                                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    User Question :</span>                                                                                            <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    severe fever</span>                                                                                               <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    Steps:</span>                                                                                                     <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    1. Use the PubMed tool to search for user given disease\"</span>                                                   <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    2. Focus on recent publications and clinical findings</span>                                                      <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    3. Identify key findings on causes, symptoms, or treatments</span>                                                <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    4. Summarize the most relevant research findings</span>                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    5. Keep total response under 500 tokens</span>                                                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">    </span>                                                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Agent: </span>                                                                                                        <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">Medical Research Analyst</span>                                                                                       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[32m╭─\u001b[0m\u001b[32m─────────────────────────────────────────────\u001b[0m\u001b[32m 📋 Task Completion \u001b[0m\u001b[32m──────────────────────────────────────────────\u001b[0m\u001b[32m─╮\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[1;32mTask Completed\u001b[0m                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mName: \u001b[0m                                                                                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    User Question :\u001b[0m                                                                                            \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    severe fever\u001b[0m                                                                                               \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    Steps:\u001b[0m                                                                                                     \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    1. Use the PubMed tool to search for user given disease\"\u001b[0m                                                   \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    2. Focus on recent publications and clinical findings\u001b[0m                                                      \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    3. Identify key findings on causes, symptoms, or treatments\u001b[0m                                                \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    4. Summarize the most relevant research findings\u001b[0m                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    5. Keep total response under 500 tokens\u001b[0m                                                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m    \u001b[0m                                                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mAgent: \u001b[0m                                                                                                        \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mMedical Research Analyst\u001b[0m                                                                                       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">[</span>CrewAIEventsBus<span style=\"font-weight: bold\">]</span> Warning: Event pairing mismatch. <span style=\"color: #008000; text-decoration-color: #008000\">'crew_kickoff_completed'</span> closed <span style=\"color: #008000; text-decoration-color: #008000\">'task_started'</span> <span style=\"font-weight: bold\">(</span>expected \n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">'crew_kickoff_started'</span><span style=\"font-weight: bold\">)</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1m[\u001b[0mCrewAIEventsBus\u001b[1m]\u001b[0m Warning: Event pairing mismatch. \u001b[32m'crew_kickoff_completed'\u001b[0m closed \u001b[32m'task_started'\u001b[0m \u001b[1m(\u001b[0mexpected \n",
       "\u001b[32m'crew_kickoff_started'\u001b[0m\u001b[1m)\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #008000; text-decoration-color: #008000\">╭──────────────────────────────────────────────── Crew Completion ────────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000; font-weight: bold\">Crew Execution Completed</span>                                                                                       <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Name: </span>                                                                                                         <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">crew</span>                                                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">ID: </span>                                                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #008000; text-decoration-color: #008000\">002d1c23-17bc-4515-8980-bc967b1d38e1</span>                                                                           <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">Final Output: PubMed exception: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: </span>    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>  <span style=\"color: #c0c0c0; text-decoration-color: #c0c0c0\">self-signed certificate in certificate chain (_ssl.c:1010)&gt;</span>                                                    <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">│</span>                                                                                                                 <span style=\"color: #008000; text-decoration-color: #008000\">│</span>\n",
       "<span style=\"color: #008000; text-decoration-color: #008000\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[32m╭─\u001b[0m\u001b[32m───────────────────────────────────────────────\u001b[0m\u001b[32m Crew Completion \u001b[0m\u001b[32m───────────────────────────────────────────────\u001b[0m\u001b[32m─╮\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[1;32mCrew Execution Completed\u001b[0m                                                                                       \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mName: \u001b[0m                                                                                                         \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32mcrew\u001b[0m                                                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mID: \u001b[0m                                                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[32m002d1c23-17bc-4515-8980-bc967b1d38e1\u001b[0m                                                                           \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mFinal Output: PubMed exception: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: \u001b[0m    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m  \u001b[37mself-signed certificate in certificate chain (_ssl.c:1010)>\u001b[0m                                                    \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m│\u001b[0m                                                                                                                 \u001b[32m│\u001b[0m\n",
       "\u001b[32m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PubMed exception: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1010)>\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #000080; text-decoration-color: #000080\">╭──────────────────────────────────────────────── Tracing Status ─────────────────────────────────────────────────╮</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>                                                                                                                 <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  Info: Tracing is disabled.                                                                                     <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>                                                                                                                 <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  To enable tracing, do any one of these:                                                                        <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  • Set tracing=True in your Crew/Flow code                                                                      <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  • Set CREWAI_TRACING_ENABLED=true in your project's .env file                                                  <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>  • Run: crewai traces enable                                                                                    <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">│</span>                                                                                                                 <span style=\"color: #000080; text-decoration-color: #000080\">│</span>\n",
       "<span style=\"color: #000080; text-decoration-color: #000080\">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[34m╭─\u001b[0m\u001b[34m───────────────────────────────────────────────\u001b[0m\u001b[34m Tracing Status \u001b[0m\u001b[34m────────────────────────────────────────────────\u001b[0m\u001b[34m─╮\u001b[0m\n",
       "\u001b[34m│\u001b[0m                                                                                                                 \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  Info: Tracing is disabled.                                                                                     \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m                                                                                                                 \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  To enable tracing, do any one of these:                                                                        \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  • Set tracing=True in your Crew/Flow code                                                                      \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  • Set CREWAI_TRACING_ENABLED=true in your project's .env file                                                  \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m  • Run: crewai traces enable                                                                                    \u001b[34m│\u001b[0m\n",
       "\u001b[34m│\u001b[0m                                                                                                                 \u001b[34m│\u001b[0m\n",
       "\u001b[34m╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[36m┌─\u001b[0m\u001b[36m────────────────────────────\u001b[0m\u001b[36m \u001b[0m\u001b[1;36mExecution Traces\u001b[0m\u001b[36m \u001b[0m\u001b[36m─────────────────────────────\u001b[0m\u001b[36m─┐\u001b[0m\n",
      "\u001b[36m│\u001b[0m                                                                             \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[1;36m🔍 \u001b[0m\u001b[1;36mDetailed execution traces are available!\u001b[0m                                \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m                                                                             \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[37mView insights including:\u001b[0m                                                   \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[94m  • Agent decision-making process\u001b[0m                                          \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[94m  • Task execution flow and timing\u001b[0m                                         \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m  \u001b[94m  • Tool usage details\u001b[0m                                                     \u001b[36m│\u001b[0m\n",
      "\u001b[36m│\u001b[0m                                                                             \u001b[36m│\u001b[0m\n",
      "\u001b[36m└─────────────────────────────────────────────────────────────────────────────┘\u001b[0m\n",
      "Would you like to view your execution traces? [y/N] (20s timeout): \n",
      "\n",
      "\u001b[34m┌─\u001b[0m\u001b[34m────────────────────────\u001b[0m\u001b[34m Tracing Preference Saved \u001b[0m\u001b[34m─────────────────────────\u001b[0m\u001b[34m─┐\u001b[0m\n",
      "\u001b[34m│\u001b[0m                                                                             \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  Info: Tracing has been disabled.                                           \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m                                                                             \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  Your preference has been saved. Future Crew/Flow executions will not       \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  collect traces.                                                            \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m                                                                             \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  To enable tracing later, do any one of these:                              \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  • Set tracing=True in your Crew/Flow code                                  \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  • Set CREWAI_TRACING_ENABLED=true in your project's .env file              \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m  • Run: crewai traces enable                                                \u001b[34m│\u001b[0m\n",
      "\u001b[34m│\u001b[0m                                                                             \u001b[34m│\u001b[0m\n",
      "\u001b[34m└─────────────────────────────────────────────────────────────────────────────┘\u001b[0m\n",
      "\n"
     ]
    }
   ],
   "source": [
    "result = main2()\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da9ed886",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b633644",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45b0e367",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d5bf497",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "crewai-course",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

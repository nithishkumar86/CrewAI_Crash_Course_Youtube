import asyncio
from crewai import Crew, Agent, Task, LLM
from pydantic import BaseModel


llm = LLM(
    model="ollama/deepseek-v3.1:671b-cloud",
    base_url="http://localhost:11434",
    temperature=0.2
)

# ============ PYDANTIC MODELS ============

class JobMatcher(BaseModel):
    company: str
    role: str
    focus: str

class JobMatcherFinal(BaseModel):
    detail: list[JobMatcher]

# ============ AGENTS ============

resume_analyst = Agent(
    role="Resume Analyst",
    goal="Analyze resume and identify skill gaps",
    backstory="Expert HR professional with 15 years of recruitment experience.",
    llm=llm,
    verbose=True
)

job_matcher = Agent(
    role="Job Matcher",
    goal="Match candidate profile with best job opportunities",
    backstory="You have deep knowledge of job market trends and requirements.",
    llm=llm,
    verbose=True
)

cover_letter_writer = Agent(
    role="Cover Letter Writer",
    goal="Write highly personalized cover letters",
    backstory="Professional writer who has helped 10,000+ candidates land jobs.",
    llm=llm,
    verbose=True
)

interview_coach = Agent(
    role="Interview Coach",
    goal="Prepare candidate with likely interview questions",
    backstory="Ex-Google interviewer who knows exactly what companies look for.",
    llm=llm,
    verbose=True
)

# ============ TASKS ============

resume_task = Task(
    description="""
    Analyze this resume: {resume}
    Identify:
    1. Strong skills
    2. Skill gaps for {target_role}
    3. Experience level
    """,
    agent=resume_analyst,
    expected_output="Detailed resume analysis with skill gaps"
)

job_match_task = Task(
    description="""
    Based on this profile: {resume}
    Find top 3 matching roles for {target_role} in {location}
    Consider skills, experience, salary expectations: {expected_salary}
    """,
    agent=job_matcher,
    expected_output="Top 3 job matches with company, role, focus",  # ✅ comma fixed
    output_pydantic=JobMatcherFinal
)

# ============ CREWS ============

resume_crew = Crew(agents=[resume_analyst], tasks=[resume_task])
job_match_crew = Crew(agents=[job_matcher], tasks=[job_match_task])

# ============ PHASE 1 ============

async def phase_1(candidate_profile):
    print("🚀 Phase 1: Analyzing resume & finding jobs simultaneously...")

    resume_result, job_matches = await asyncio.gather(
        resume_crew.akickoff(inputs={
            "resume": candidate_profile["resume"],
            "target_role": candidate_profile["target_role"]
        }),
        job_match_crew.akickoff(inputs={
            "resume": candidate_profile["resume"],
            "target_role": candidate_profile["target_role"],
            "location": candidate_profile["location"],
            "expected_salary": candidate_profile["expected_salary"]
        })
    )

    return resume_result, job_matches

# ============ PHASE 2 ============

async def phase_2(resume_result, job_matches, candidate_profile):
    print("🚀 Phase 2: Writing cover letters for all jobs simultaneously...")

    # Fix — Now using actual Phase 1 pydantic output instead of hardcoded list
    matched_jobs = [
        {"company": job.company, "role": job.role, "focus": job.focus}
        for job in job_matches.pydantic.detail
    ]

    cover_letter_inputs = [
        {
            "resume": candidate_profile["resume"],
            "company": job["company"],
            "role": job["role"],
            "focus": job["focus"],
            "resume_analysis": str(resume_result)
        }
        for job in matched_jobs
    ]

    cover_letter_task = Task(
        description="""
        Write a personalized cover letter for {company}
        Role: {role}
        Key focus: {focus}
        Based on resume analysis: {resume_analysis}
        Candidate resume: {resume}
        """,
        agent=cover_letter_writer,
        expected_output="Professional cover letter tailored for the company"
    )

    interview_task = Task(
        description="""
        Generate top 5 interview questions for {role} at {company}
        Focus area: {focus}
        Include: Technical + Behavioral questions
        """,
        agent=interview_coach,
        expected_output="5 likely interview questions with precise and concise answer approach "
    )

    cover_letter_crew = Crew(agents=[cover_letter_writer], tasks=[cover_letter_task])
    interview_crew = Crew(agents=[interview_coach], tasks=[interview_task])

    cover_letters, interview_preps = await asyncio.gather(
        cover_letter_crew.akickoff_for_each(cover_letter_inputs),
        interview_crew.akickoff_for_each(cover_letter_inputs)
    )

    return cover_letters, interview_preps

# ============ MAIN ============

async def main():
    candidate_profile = {
        "resume": """
            NITHISHKUMAR M
            Email: nkumar861019@gmail.com | GitHub: github.com/nithishkumar86

            TECHNICAL SKILLS
            Programming Languages: Python, Java, C
            Web Frameworks & Libraries: FastAPI, Flask, HTML, CSS, Streamlit
            Python Libraries: Pandas, NumPy, Seaborn, Matplotlib
            Traditional Databases: MySQL, SQLite, PostgreSQL, MongoDB
            ML & DL Frameworks: Scikit-Learn, TensorFlow, PyTorch, NLP, ANN, CNN, OpenCV
            Generative & Agentic AI: LangChain, LangSmith, LlamaIndex, Fine-tuning, LangGraph,
                                      CrewAI, Agno, LangFlow, Autogen, n8n, Google ADK
            Vector Databases: FAISS, Chroma, Pinecone, AstraDB
            Cloud & DevOps: AWS (Lambda, S3, ECR, Bedrock, SageMaker, Fargate),
                            Docker, Git, Jenkins, SonarQube

            EDUCATION
            B.Tech Information Technology | CGPA: 7.09/10
            University College Of Engineering, Tiruchirappalli (Nov 2022 - Present)

            PROJECTS
            1. Insurance Premium Prediction System
               - Predicted insurance premium categories using age, BMI, lifestyle, income, occupation
               - Built with Pydantic, Scikit-learn, FastAPI, Streamlit
               - Containerized with Docker, deployed on AWS ECR

            2. Medical Chatbot (GenAI + AWS)
               - AI-powered medical query chatbot using Groq API, Pinecone, Flask, HTML/CSS
               - CI/CD with Jenkins, security scanning with AquaTrivy
               - Dockerized and deployed on AWS ECR

            3. Bus Booking System with Agents (Agentic AI + AWS)
               - CRUD-based bus booking platform with agent workflows
               - Built with FastAPI, Streamlit, PostgreSQL, Pydantic
               - CI/CD with Jenkins + SonarQube, deployed on AWS Fargate

            4. Data Analyst & Report Generator (CrewAI + GenAI)
               - AI-powered dataset analysis and executive report generation
               - Built with CrewAI, OpenRouter API, LangSmith, ElevenLabs (voice-over)
               - Frontend with Streamlit, visualizations with Pandas, Matplotlib, Seaborn

        """,
        "target_role": "Agentic AI / GenAI Engineer",
        "location": "Bangalore",
        "expected_salary": "8-12 LPA"
    }

    resume_result, job_matches = await phase_1(candidate_profile)

    cover_letters, interview_preps = await phase_2(
        resume_result, job_matches, candidate_profile
    )

    print("\n✅ Resume Analysis Done")
    print("✅ Job Matches Found")
    print(f"✅ {len(cover_letters)} Cover Letters Generated")
    print(f"✅ {len(interview_preps)} Interview Preps Ready")

asyncio.run(main())


'''
Summary Table

            akickoff()   akickoff_for_each()

Inputs     Single dict     List of dicts
Runs       Once            Multiple times 
Results    Single results  List of results
Use case   One task        Batch processing
Internally Direct async    gather + akickoff'''
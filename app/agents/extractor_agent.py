from app.prompts.extractor_prompt import EXTRACTOR_PROMPT
from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from app.graph.states import JDExtraction

load_dotenv()

def loadJd(path , state : JDExtraction):
    loader = PyPDFLoader(path)
    docs = loader.load()
    text = "\n\n".join(doc.page_content for doc in docs)

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv('GROQ_API_KEY'),
        temperature=0.6
    )

    prompt = EXTRACTOR_PROMPT.format(description=text)
    structured_llm = llm.with_structured_output(JDExtraction)
    response = structured_llm.invoke(prompt)
    content = response.model_dump()

    state.company = content["company"]
    state.role = content["role"]
    state.location = content["location"]
    state.employment_type = content["employment_type"]
    state.experience = content["experience"]
    state.skills = content["skills"]
    state.education = content["education"]
    state.responsibilities = content["responsibilities"]
    state.preferred_skills = content["preferred_skills"]
    state.recruiter_email = content["recruiter_email"]
    state.application_deadline = content["application_deadline"]
    state.salary = content["salary"]
    state.search_summary = content["search_summary"]
    return state



from langgraph.types import interrupt
from app.graph.states import JobApplicationState
from app.prompts.email_prompt import EMAIL_GENERATION_PROMPT
from resume_ingestion.retrieval import get_resume
from dotenv import load_dotenv
import os
from app.graph.embedder import embeddings
from db.connection import get_connection
from langchain_groq import ChatGroq

load_dotenv()

def email_creation(state: JobApplicationState):
    decision = interrupt(
        {
            "type": "human_approval",
            "question": (
                f"The estimated selection probability is "
                f"{state['analysis'].selection_probability}%. "
                "Do you want me to generate an application email?"
            ),
        }
    )

    if decision.lower() == "yes":
        # Generate email here
        return {
           "mail" :  generate_mail(state)
        }

    return {}


def generate_mail(state : JobApplicationState):
    recuiter_mail = state['job'].recruiter_email
    job_title = state['job'].role
    company = state['job'].company
    overall_analysis = state['analysis'].overall_analysis
    search_summary = state['job'].search_summary
    resume = get_resume()
    
    if search_summary : 
        embedding = embeddings.embed_query(search_summary)
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                    SELECT chunk_text ,
                    embedding <=> %s :: vector AS distance 
                    from resume_chunks WHERE resume_id = %s 
                    ORDER BY distance LIMIT 3;
                    """ , (embedding , resume[0],),)
            relevant_chunks = cur.fetchall()
        conn.close()
            
   
    resume_context = "\n\n".join(chunk_text for chunk_text, _ in relevant_chunks)
    print(resume_context)
    resume_summary = resume_context
    
    prompt = EMAIL_GENERATION_PROMPT.format(
    recruiter_mail=recuiter_mail,
    job_title=job_title,
    company=company,
    search_summary=search_summary,
    overall_analysis=overall_analysis,
    resume_summary=resume_summary,
    )    
    
    
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv('GROQ_API_KEY'),
        temperature=0.6
    )
    
    response = llm.invoke(prompt)
    return response.content 
    
    
    
    
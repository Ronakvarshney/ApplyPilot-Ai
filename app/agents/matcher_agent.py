from resume_ingestion.retrieval import get_resume
from app.graph.embedder import embeddings
from db.connection import get_connection
from app.prompts.matcher_prompt import MATCHER_PROMPT
from app.graph.states import JobApplicationState , AnalysisResponse
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()







def Semantic_search(state :JobApplicationState ):
    resume = get_resume()
    print(resume[0])  
    search_summary = state["job"].search_summary
    # company = state['job'].company
    # role = state['job'].role
    # location = state['job'].location
    # employment_type = state['job'].employment_type
    # experience = state['job'].experience
    # skills = state['job'].skills
    # education = state['job'].education
    # responsibilities = state['job'].responsibilities
    # preferred_skills = state['job'].preferred_skills
    
    
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
        
        

        
    print(relevant_chunks)
    
   
    resume_context = "\n\n".join(chunk_text for chunk_text, _ in relevant_chunks)
    print(resume_context)
    
    prompt = MATCHER_PROMPT.format(
    search_summary=search_summary,
    resume_context=resume_context,
    )
    
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv('GROQ_API_KEY'),
        temperature=0.6
    )
    
    structured_llm = llm.with_structured_output(AnalysisResponse)
    
    response = structured_llm.invoke(prompt)
    return {
        'analysis' : response
    }

    

    
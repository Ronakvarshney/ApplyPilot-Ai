from app.prompts.extractor_prompt import EXTRACTOR_PROMPT
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from app.graph.states import JDExtraction , JobApplicationState
from app.graph.loader import load_pdf
from app.agents.matcher_agent import Semantic_search

load_dotenv()

def loadJd(state : JobApplicationState):
    path = state['source']
    
    docs = load_pdf(path)
 
    text = "\n\n".join(doc.page_content for doc in docs)

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv('GROQ_API_KEY'),
        temperature=0.6
    )

    prompt = EXTRACTOR_PROMPT.format(description=text)
    structured_llm = llm.with_structured_output(JDExtraction)
    response = structured_llm.invoke(prompt)    
    return {
        'job' : response
    }



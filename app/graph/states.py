from typing_extensions import TypedDict , Annotated 
from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages
from pydantic import BaseModel
from typing import List , Optional

class ResumeInfo(TypedDict):
    id : str 
    filename : str 
    filepath : str
    summary : str 
    skills : str 
    
class JDExtraction(BaseModel):
    company: Optional[str] = None
    role: str
    location: Optional[str] = None
    employment_type: Optional[str] = None
    experience: Optional[str] = None
    skills: List[str] = []
    education: Optional[str] = None
    responsibilities: List[str] = []
    preferred_skills: List[str] = []
    recruiter_email: Optional[str] = None
    application_deadline: Optional[str] = None
    salary: Optional[str] = None
    search_summary: str

class AnalysisResponse(BaseModel):
    matches: list[str]
    missings: list[str]
    ats_score: float
    recommendations: str 
    
class MailState(TypedDict):
    receiver: str
    subject: str
    body: str
    attachment: str    
    

class JobApplicationState(TypedDict):

    source: str
    job: JDExtraction
    candidates_resume : list[ResumeInfo]
    selected_resume: ResumeInfo
    analysis: AnalysisResponse
    mail: MailState
    approved_mailcreation: bool
    approved_mailsend: bool
    messages: Annotated[list[BaseMessage], add_messages]
    
from typing_extensions import TypedDict , Annotated 
from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages

class ResumeInfo(TypedDict):
    id : str 
    filename : str 
    filepath : str
    summary : str 
    skills : str 
    
class JobInfo(TypedDict):
    job_description: str
    company: str
    role: str
    skills: list[str]
    experience: str
    recruiter_email: str
    
class AnalyseState(TypedDict):
    matches : list[str]
    missings : list[str]
    ats_score : float
    recommendations : str 
    
class MailState(TypedDict):
    receiver: str
    subject: str
    body: str
    attachment: str    
    

class JobApplicationState(TypedDict):

    source: str
    job: JobInfo
    candidates_resume : list[ResumeInfo]
    selected_resume: ResumeInfo
    analysis: AnalyseState
    mail: MailState
    approved_mailcreation: bool
    approved_mailsend: bool
    messages: Annotated[list[BaseMessage], add_messages]
    
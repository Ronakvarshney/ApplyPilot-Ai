from langgraph.graph import StateGraph , START , END
from app.agents.extractor_agent import loadJd
from app.agents.matcher_agent import Semantic_search
from app.graph.states import JobApplicationState
from langgraph.checkpoint.sqlite import SqliteSaver
from app.agents.email_writer import email_creation
import sqlite3


conn = sqlite3.connect(database="store.db" , check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)

config = {"configurable" : {"thread_id" : "123"}}


graph = StateGraph(JobApplicationState)
graph.add_node("extractor" , loadJd)
graph.add_node("matcher" , Semantic_search)
graph.add_node("email_create" , email_creation)




graph.add_edge(START , "extractor")
graph.add_edge("extractor" , "matcher")
graph.add_edge("matcher" , 'email_create')
graph.add_edge('email_create' , END)


chatbot = graph.compile(checkpointer=checkpointer)
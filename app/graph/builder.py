from langgraph.graph import StateGraph , START , END
from app.agents.extractor_agent import loadJd
from app.agents.matcher_agent import Semantic_search
from app.graph.states import JobApplicationState




graph = StateGraph(JobApplicationState)
graph.add_node("extractor" , loadJd)
graph.add_node("matcher" , Semantic_search)



graph.add_edge(START , "extractor")
graph.add_edge("extractor" , "matcher")
graph.add_edge("matcher" , END)


chatbot = graph.compile()
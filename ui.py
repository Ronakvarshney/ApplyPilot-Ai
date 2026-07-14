import streamlit as st 
import os 
from resume_ingestion.ingestion import insert_resume
from app.agents.extractor_agent import loadJd
from app.graph.states import JDExtraction


with st.sidebar:
    st.title("Upload your resume and JD")
    
    st.subheader("Resume Upload....")
    resumefile = st.file_uploader("Upload your resume file")
    if resumefile:
        path = os.path.join('uploads' , resumefile.name)
        with open(path , "wb") as f :
            f.write(resumefile.getbuffer())
        
        st.success("Upload successfully")
        insert_resume(resumefile.name , path)
       
    
    
    st.header("Upload your JD")
    jdfile = st.file_uploader("Upload file")
    if jdfile:
        path = os.path.join("uploads" , jdfile.name)
        with open(path , "wb") as f:
            f.write(jdfile.getbuffer())
        loadJd(path , JDExtraction )
        
        st.success("Jd upload successfully")
        

if "welcome_shown" not in st.session_state:
    with st.chat_message("assistant"):
        st.markdown("""
# 👋 Welcome to ApplyPilot AI

Your AI-powered Job Application Copilot.

Upload your Resume and Job Description from the sidebar.

I'll:
- 📄 Extract the job details
- 🧠 Find the best matching resume
- 📊 Analyze compatibility
- ✉️ Draft a personalized email
- 📧 Send it after your approval

**Let's get started! 🚀**
""")
    st.session_state.welcome_shown = True


st.chat_input("Here start by uploading your JD nd Resume")
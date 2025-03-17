from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
import PyPDF2 as pdf

load_dotenv()  # load all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini Pro Response
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Streamlit Code
st.title("Gemini ATS")
st.text("       - Developed By: Mohammad Ayaz Alam")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

submit = st.button("SUBMIT")

if submit:  
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)
        input_prompt = f"""
        Hey Act like a skilled or very experience ATS(Application Tracking system) with a deep understanding of tech field, software engineering, data science,data engineer, data analytics and big data engineer.
        Your task is to evaluate the resume based on the given job description.
        You must consider the job market is very very competitive and you should provide best assistance
        for improving the resumes. Assign the percentage matching based on JD(Job Description) and the
        missing keywords with high accuracy. And after all this generate a very Good and Accurate Cover Letter for the given JD(Job Description) 
        using the Resume details.

        Resume:{resume_text}
        description:{jd}
        Cover Letter:
        """
        
        response = get_gemini_response(input_prompt)
        st.subheader("Response")
        st.text(response)

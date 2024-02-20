import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv


load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#response
# def get_gemini_response(input):
#     model= genai.GenerativeModel('gemini-pro')
#     response=model.generate_content(input)
#     return response.text

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input, pdf_content, prompt])
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template


input_prompt1 = """
Your task is to review the provided resume against the job description.
 Please share your professional evaluation on whether the candidate's profile aligns with the role.
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements
"""

input_prompt2 = """
Your role is to scrutinize the resume in light of the job description provided.
Share your insights on the candidate's suitability for the role
Additionally, offer advice on enhancing the candidate's skills and identify areas where improvement is needed.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of Software Functionality and ATS functionality,
your task is to evaluate the resume against the provided job description. assess the compatibility of the resume with the role. Give me what are the keywords that are missing
 Also, provide recommendations for enhancing the candidate's skills and identify which areas require further development.
"""
input_prompt4 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality,
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. The output should only be a percentage match score.
"""
input_prompt5= """ Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech feild related to the job description. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Job Description and
the missing keywords with high accuracy
resume:{text}
description:{jd}

Provide detailed yet comprehensive response and only use tabular structure for the response"""
## streamlit app


st.markdown("<h1 style='text-align: center;'><strong><u>JobFit Analyzer</u></strong></h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>This Application helps you in your Resume Review with help of GEMINI AI [LLM]</h3>", unsafe_allow_html=True)


job_description =st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

if uploaded_file is not None:
    st.success("File uploaded successfully", icon="✅")
    col1, col2 = st.columns((2))  # Creates columns with equal width
    with col1:
        submit1 = st.button("Tell Me About the Resume")

    with col2:
        submit2 = st.button("How Can I Improvise my Skills")

    with col1:
        submit3 = st.button("What are the Missing Keywords")
    with col2:
        submit4 = st.button("Percentage match")

    if submit1:
        if uploaded_file is not None:
            pdf_content = input_pdf_text(uploaded_file)
            response = get_gemini_response(input_prompt1, pdf_content, job_description)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.error("Please upload a PDF file to proceed", icon="🚨")

    elif submit2:
        if uploaded_file is not None:
            pdf_content = input_pdf_text(uploaded_file)
            response = get_gemini_response(input_prompt2, pdf_content, job_description)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.error("Please upload a PDF file to proceed", icon="🚨")

    elif submit3:
        if uploaded_file is not None:
            pdf_content = input_pdf_text(uploaded_file)
            response = get_gemini_response(input_prompt3, pdf_content, job_description)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.error("Please upload a PDF file to proceed", icon="🚨")

    elif submit4:
        if uploaded_file is not None:
            pdf_content = input_pdf_text(uploaded_file)
            response = get_gemini_response(input_prompt4, pdf_content, job_description)
            #st.subheader("The Response is")

            # % Bar
            progress = int(response[:-1])
            html_content = f"""
            <div style="width: 100%; height: 20px; background-color: #F0F0F0; border: 1px solid #D3D3D3; border-radius: 5px;">
            <div style="width: {progress}%; height: 100%; background-color: #4CAF50; border-radius: 5px;">
            </div>
            </div>
            """
            st.markdown(html_content, unsafe_allow_html=True)
            st.write(f"Percentage Match is {response}")
        else:
            st.error("Please upload a PDF file to proceed", icon="🚨")

   
    st.subheader("Or you can")
    submit5 = st.button("Get Full Resume Analysis")  
    
    if submit5:
        # Hide other buttons when submit5 is clicked
        if uploaded_file is not None:
            pdf_content = input_pdf_text(uploaded_file)
            response = get_gemini_response(input_prompt5, pdf_content, job_description)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.error("Please upload a PDF file to proceed", icon="🚨")

st.markdown("---")
st.markdown("<h5 style='text-align: center;'>Making Job Applications Easier</h5>", unsafe_allow_html=True)

with st.container():
    footer_text = """
    <div style="text-align: center; padding: 10px; font-size: 12px;">
        &copy; Made with love by Afzal Asar❤️.
    </div>
    """
    st.markdown(footer_text, unsafe_allow_html=True)


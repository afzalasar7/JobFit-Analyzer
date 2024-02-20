# JobFit Analyzer: AI-Powered Resume Matchmaker

**Tired of struggling to assess resume-job fit?**  The JobFit Analyzer streamlines this process with the power of **Large Language Models (LLMs)**. Get **instant, insightful feedback** on how well a resume aligns with a job description, helping you make **informed hiring decisions** or **improve your candidacy**.

## Key Features

- **Powerful LLM Analysis:** Leverage the advanced capabilities of Google's GEMINI-Pro model to provide comprehensive match assessments.
- **Multiple Analysis Styles:** Choose from various prompts to tailor the feedback to your specific needs (e.g., strengths/weaknesses, improvement suggestions, ATS optimization, personalized insights).
- **Intuitive Streamlit Interface:** Enjoy a user-friendly experience with clear instructions and informative responses.
- **Detailed Match Scores:** Gain valuable insights into how closely the resume aligns with the job description, even receiving a precise percentage match for ATS applications (for tech fields).
- **Visual Feedback:** Get engaging progress bars and tabular output for clarity and ease of understanding.
- **Privacy-Focused:** Your data is treated with utmost care. No identifiable information is stored or shared.

## Getting Started

1. **Set up:**
   - Install required libraries: `pip install streamlit PyPDF2 google-generativeai`
   - Obtain a Google Generative AI API key and create a `.env` file to store it: `GOOGLE_API_KEY=YOUR_API_KEY`
2. **Run the app:**
   - Execute `streamlit run app.py` in your terminal.
3. **Use the app:**
   - Paste the job description in the designated field.
   - Upload your resume in PDF format.
   - Select the desired analysis style using the provided buttons.
   - Get insightful feedback tailored to your choice.

## Example Analysis

**Prompt:** Act Like a skilled or very experience ATS(Application Tracking System) with a deep understanding of tech feild related to the job description. Your task is to evaluate the resume based on the given job description. You must consider the job market is very competitive and you should provide best assistance for improving thr resumes. Assign the percentage Matching based on Job Description and the missing keywords with high accuracy
resume:{text}
description:{jd}

Provide detailed yet comprehensive response and only use tabular structure for the response

### Response (sample):

| Category | Strengths | Weaknesses | Recommendations | Missing Keywords |
|---|---|---|---|---|
| Skills | Proficient in Python, Java, and JavaScript | Limited experience with cloud platforms | Focus on cloud-related projects and certifications | DevOps, Kubernetes, AWS |
| Experience | 3 years in software development | Lack of leadership experience | Highlight leadership roles in previous projects or extracurricular activities | Team Lead, Project Management |
| Education | Master's degree in Computer Science | Consider pursuing industry-specific certifications | Mention relevant certifications or online courses | Big Data, Machine Learning |

## Contributing

We welcome contributions to improve JobFit Analyzer! Fork the repository, create a pull request with your changes, and follow the contribution guidelines.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

**Stay tuned for further updates and enhancements!**

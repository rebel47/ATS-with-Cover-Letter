# Gemini ATS: Resume Evaluator and Cover Letter Generator 📄✍️

Gemini ATS is a Streamlit-based web application designed to help job seekers optimize their resumes for Applicant Tracking Systems (ATS). It evaluates resumes against a given job description, identifies areas for improvement, and generates a tailored cover letter to increase your chances of landing an interview.

## Features
- **Resume Evaluation:** Analyze your resume against a job description and receive a percentage match score.
- **Keyword Suggestions:** Identify missing keywords critical to the job role.
- **Cover Letter Generation:** Create a professional and customized cover letter based on your resume and job description.

## Live Demo
Try the app here: [Gemini ATS](https://atswithcoverletter.streamlit.app/)

## Installation

### Prerequisites
- Python 3.8 or above
- Google Cloud API key for the Gemini Pro Vision API

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/rebel47/gemini-ats.git
   cd gemini-ats
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the project root and add:
   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

4. Run the application:
   ```bash
   streamlit run main.py
   ```

## How It Works
1. **Upload Your Resume:** Upload a PDF version of your resume.
2. **Provide Job Description:** Paste the job description into the text area.
3. **Get Feedback:** The app evaluates your resume based on the job description and provides:
   - Matching percentage
   - Missing keywords
   - Suggestions for improvement
4. **Generate Cover Letter:** A professional cover letter tailored to the job description is generated automatically.

## Supported Formats
- Resume: PDF

## Technologies Used
- **Streamlit:** For the interactive web application
- **Google Gemini Pro Vision API:** For AI-driven text analysis and content generation
- **PyPDF2:** For extracting text from PDF resumes
- **Python-dotenv:** For secure API key management

## Future Enhancements
- Add support for additional resume file formats (e.g., DOCX).
- Provide detailed feedback on specific sections of the resume.
- Offer multiple cover letter templates to choose from.

## Example Workflow
1. **Upload Resume:** *Upload a resume PDF.*
2. **Job Description:** *"We are looking for a Data Scientist with expertise in Python, Machine Learning, and Big Data."*
3. **Response:**
   - Matching Percentage: *85%*
   - Missing Keywords: *"Deep Learning, Data Visualization"*
   - Cover Letter: 
     ```
     Dear Hiring Manager,
     I am excited to apply for the Data Scientist role at [Company Name]...
     ```

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- **Google Cloud:** For their powerful AI APIs
- **Streamlit:** For simplifying the development of web applications

---

**Developed with ❤️ by Mohammad Ayaz Alam**
```

import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

# load_env()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
                        model="llama-3.3-70b-versatile",
                        temperature=0,
                        max_tokens=None,
                        timeout=None,
                        max_retries=2)
    
    
    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template("""
                I will give you scraped text from the job posting. 
                Your job is to extract the job details & requirements in a JSON format containing the following keys: 'role', 'experience', 'skills', and 'description'. 
                Only return valid JSON. No preamble, please.
                Here is the scraped text: {page_data}
                """)    
        
        chain_extract = prompt_extract | self.llm
        response = chain_extract.invoke(input={"page_data" : cleaned_text})
        
        try:
            json_parser = JsonOutputParser()
            response = json_parser.parse(response.content)
        except OutputParserException:
            raise OutputParserException("Content too big, unable to parse jobs.")
        
        return response if isinstance(response, list) else [response]


    def write_email(self, job_description, portfolio_urls):
        prompt_email = PromptTemplate.from_template(
                """
                I will give you a role and a task that you have to perform in that specific role.
    Your Role: Your name is Shivaramakrishna, You are an Backend Developer Java (m/f/d) with TypeScript experience
Permanent employee, Full or part time · Germany-wide (mobile)
52,000 - 80,000 € per year, your phone number is +91 9100353010, and your email is shivaramakrishnam984@gmail.com, also give my experience according to the job, not only backend developer
Your mission:
You develop microservices in modern cloud environments (e.g. AWS).

You test and operate your services independently - from CI/CD to monitoring.

You are actively involved in architecture and technology decisions.

You are part of our agile development team: inner team and help design our solutions.

That is what you bring with you:
You enjoy coding and want to learn.

You have experience with Java (Spring), ideally also with TypeScript.

You are familiar with SQL/noSQL databases.

You have already worked with AWS or other cloud platforms.

You feel comfortable in an agile environment and communicate confidently in English.
. 
    Your Job: Your Job is to write cold emails to clients regarding the Job openings that they have advertised. Try to pitch your clients with an email hook that opens a conversation about a possibility of working with them. Add the most relevant portfolio URLs from
    the following (shared below) to showcase that we have the right expertise to get the job done. 
    I will now provide you with the Job description and the portfolio URLs:
    JOB DESCRIPTION: {job_description}
    ------
    PORTFOLIO URLS: {portfolio_urls}
    """)
        
        chain_email = prompt_email | self.llm
        response = chain_email.invoke({"job_description": str(job_description), "portfolio_urls": portfolio_urls})

        return response.content
        
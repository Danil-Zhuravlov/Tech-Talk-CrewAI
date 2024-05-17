import os
from crewai import Agent
from textwrap import dedent
from langchain_groq import ChatGroq
from tools.search_tools import SearchTools, ScrapeWebsite, SearchWikipedia, SearchNews, SearchAcademicPapers

class TechTalkAgents:
    def __init__(self):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-8b-8192"
        )

    def slide_designer(self):
        return Agent(
            role="Slide Designer",
            backstory=dedent(
                f"""Expert in creating professional PowerPoint, Keynote, and
                Google Slides presentation. I have decades of experience making
                creating presentations on even the most complex topics. 
                My presentations have been used even by the biggest companies
                where the stakes are very high.
                """),
            goal=dedent(f"""
                        Create a text for each slide of the presentation using
                        all your knowledge and storytelling techniques to create
                        the best possible result and for each slide write
                        notes for presenter to ensure that no matter how
                        the speaker is prepared he will be able to amaze
                        the public.
                        """),
            tools=[],
            verbose=True,
            llm=self.llm,
        )

    def storytelling_consultant(self):
        return Agent(
            role="Storytelling Consultant",
            backstory=dedent(
                f"""Expert at writing text for public presentations.
                I'm a master at storytelling with 40 years of experience.
                I have a degree in Journalism, Communications, Creative Writing,
                Playwriting, and Public Speaking.
                """),
            goal=dedent(
                f"""Edit the provided text to make it professional and engaging
                using the best storytelling practices.
                """),
            tools=[],
            verbose=True,
            llm=self.llm,
        )

    def copywriter(self):
        return Agent(
            role="Copywriter",
            backstory=dedent(f"""Experienced and very smart copywriter who is
                             working for the last 20 years and helps others to
                             make the text as concise as it is possible without
                             loss of truly important information.
                             """),
            goal=dedent(
                f"""Provide only the most important information from the research
                papers to make them more easy to read and concise to other
                professionals who are working to create a stunning PowerPoint
                presentations.
                """),
            tools=[],
            verbose=True,
            llm=self.llm,
        )

    def researcher(self):
        return Agent(
            role="Researcher",
            backstory=dedent(f"""Professional researcher whose goal in life
                             is to learn as much as possible. I can find all necessary
                             information for specific topics and write a nice research
                             paper about it that will contain all mandatory information
                             to help other people to learn the topic easier and
                             more efficiently.
                             """),
            goal=dedent(
                f"""Find all necessary information for a specific topic and write
                 a nice research paper about it that will contain all mandatory information
                 to help other people to learn the topic easier and more efficiently.
                """),
            tools=[
                SearchTools.search_internet, ScrapeWebsite.scrape_website,
                SearchWikipedia.search_wikipedia, SearchNews.search_news,
                SearchAcademicPapers.search_academic_papers],
            verbose=True,
            llm=self.llm,
        )

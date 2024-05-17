import os
from crewai import Agent
from textwrap import dedent
from langchain_groq import ChatGroq
from tools.search_tools import SearchTools

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
                """Expert in creating professional PowerPoint, Keynote, and
                Google Slides presentations. I have decades of experience making
                presentations on even the most complex topics. 
                My presentations have been used even by the biggest companies
                where the stakes are very high.
                """
            ),
            goal=dedent(
                """Create a text for each slide of the presentation using
                all your knowledge and storytelling techniques to create
                the best possible result and for each slide write
                notes for the presenter to ensure that no matter how
                the speaker is prepared, he will be able to amaze
                the public.
                """
            ),
            tools=[
                SearchTools.search_internet,
                SearchTools.search_wikipedia
            ],
            verbose=True,
            llm=self.llm
        )

    def storytelling_consultant(self):
        return Agent(
            role="Storytelling Consultant",
            backstory=dedent(
                """Expert at writing text for public presentations.
                I'm a master at storytelling with 40 years of experience.
                I have a degree in Journalism, Communications, Creative Writing,
                Playwriting, and Public Speaking.
                """
            ),
            goal=dedent(
                """Edit the provided text to make it professional and engaging
                using the best storytelling practices.
                """
            ),
            tools=[
                SearchTools.search_internet,
                SearchTools.search_news
            ],
            verbose=True,
            llm=self.llm
        )

    def copywriter(self):
        return Agent(
            role="Copywriter",
            backstory=dedent(
                """Experienced and very smart copywriter who has
                been working for the last 20 years and helps others to
                make text as concise as possible without
                losing truly important information.
                """
            ),
            goal=dedent(
                """Provide only the most important information from research
                papers to make them easier to read and concise for other
                professionals who are working to create stunning PowerPoint
                presentations.
                """
            ),
            tools=[
                SearchTools.search_internet,
                SearchTools.search_wikipedia
            ],
            verbose=True,
            llm=self.llm
        )

    def researcher(self):
        return Agent(
            role="Researcher",
            backstory=dedent(
                """Professional researcher whose goal in life
                is to learn as much as possible. I can find all necessary
                information on specific topics and write a thorough research
                paper that contains all mandatory information
                to help other people learn the topic more easily and
                efficiently.
                """
            ),
            goal=dedent(
                """Find all necessary information on a specific topic and write
                a thorough research paper that contains all mandatory information
                to help other people learn the topic more easily and efficiently.
                """
            ),
            tools=[
                SearchTools.search_internet,
                SearchTools.scrape_website,
                SearchTools.search_wikipedia,
                SearchTools.search_news,
                SearchTools.search_academic_papers
            ],
            verbose=True,
            llm=self.llm
        )

# Example instantiation of the agents
if __name__ == "__main__":
    agents = TechTalkAgents()
    slide_designer_agent = agents.slide_designer()
    storytelling_consultant_agent = agents.storytelling_consultant()
    copywriter_agent = agents.copywriter()
    researcher_agent = agents.researcher()

    # Test to ensure agents are configured correctly
    print(slide_designer_agent)
    print(storytelling_consultant_agent)
    print(copywriter_agent)
    print(researcher_agent)

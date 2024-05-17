from crewai import Crew
from textwrap import dedent
from agents import TechTalkAgents
from tasks import TechTalkTasks
from dotenv import load_dotenv
load_dotenv()

class TechTalkCrew:
    def __init__(self, topic, length, interests, pain_point, type_of_presentation):
        self.topic = topic
        self.length = length
        self.pain_point = pain_point
        self.type_of_presentation = type_of_presentation
        self.interests = interests

    def run(self):
        # Initialize agents and tasks
        agents = TechTalkAgents()
        tasks = TechTalkTasks()

        researcher = agents.researcher()
        copywriter = agents.copywriter()
        storytelling_consultant = agents.storytelling_consultant()
        slide_designer = agents.slide_designer()

        # Perform research task
        research_task = tasks.research_subject(researcher, self.topic)
        research_crew = Crew(agents=[researcher], tasks=[research_task], verbose=True)
        research_result = research_crew.kickoff()

        # Perform rewriting task
        rewrite_task = tasks.rewrite_research_paper(copywriter, research_result, self.topic)
        rewrite_crew = Crew(agents=[copywriter], tasks=[rewrite_task], verbose=True)
        rewrite_result = rewrite_crew.kickoff()

        # Perform storytelling task
        story_task = tasks.create_a_story(
            storytelling_consultant, rewrite_result, self.topic, self.interests,
            self.pain_point, self.type_of_presentation)
        story_crew = Crew(agents=[storytelling_consultant], tasks=[story_task], verbose=True)
        story_result = story_crew.kickoff()

        # Perform slide design task
        slide_task = tasks.create_presentation_text(slide_designer, self.topic, self.length, story_result)
        slide_crew = Crew(agents=[slide_designer], tasks=[slide_task], verbose=True)
        slide_result = slide_crew.kickoff()

        return story_result, slide_result

# Main function to run the crew
if __name__ == "__main__":
    print("## Welcome to Tech Talk Crew")
    print('-------------------------------')
    topic = input(dedent("What is the topic?\n"))
    length = input(dedent("What length of the presentation do you want?\n"))
    interests = input(dedent("What are the interests of the audience?\n"))
    pain_point = input(dedent("What are the pain points of your audience you can use to target?\n"))
    type_of_presentation = input(dedent("What type of presentation do you want to make: Online or Offline?\n"))

    tech_talk_crew = TechTalkCrew(topic, length, interests, pain_point, type_of_presentation)
    story_result, slide_result = tech_talk_crew.run()

    print("\n\n########################")
    print("## Here is your PowerPoint Presentation Blueprint")
    print("########################\n")
    print(slide_result)
    
    print("\n\n########################")
    print("## Here is the storytelling consultant's output")
    print("########################\n")
    print(story_result)

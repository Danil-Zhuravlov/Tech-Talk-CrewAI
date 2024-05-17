from crewai import Task
from textwrap import dedent

class TechTalkTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def create_presentation_text(self, agent, topic, length, text):
        return Task(
            description=dedent(
                f"""
                **Task**: Create a detailed and engaging presentation.
                **Description**: Write comprehensive and engaging text for each PowerPoint slide. 
                Include clear and relevant visuals for each slide. Recommend the best fonts and provide detailed speaker notes to ensure the presenter delivers an impactful presentation. Ensure the slides include bullet points, key words, and stories to make the content easy to follow.

                **Parameters**: 
                - Topic: {topic}
                - Length of the presentation: {length}

                **Dependencies**:
                - Input text from storytelling consultant: {text}

                **Note**: {self.__tip_section()}
                """
            ),
            agent=agent,
            dependencies=[text],
            expected_output=dedent("""
            Recommended Font: Font_name for the entire presentation based on the {topic} and readability. Aim to use concise font through the entire presentation

            Slide 1: Title Slide
            1) Text: 
               - Title: Presentation Title. (It should be short, concise and catchy)
               - Subtitle: Subtitle (if any) (It should be short, concise and describe the title)
               - Presenter: Presenter's Name and Title. Put the placeholders of the name and title like this: [NAME], [TITLE]
            2) Speaker Hint: "Welcome to our presentation on [topic]. My name is [NAME] and today we'll be discussing..."

            Slide 2: Agenda
            1) Text: 
               - Bullet Point 1: Introduction
               - Bullet Point 2: Problem Statement
               - Bullet Point 3: Solution Overview
               - Bullet Point 4: Benefits
               - Bullet Point 5: Conclusion
               - Bullet Point 6: Q&A
               Story: Outline the flow of the presentation to set expectations.
            2) Prompt: Visual description of a picture for an agenda slide to use it as a prompt for DALL-E 3.
            3) Speaker Hint: "Here's an overview of what we'll cover today. We'll start with an introduction, followed by a discussion on the problem statement..."

            Mid-part: Actual Material
            - For each slide in this section:
            Slide slide_number: Title_of_the_slide
            1) Text: 
               - Bullet Point 1
               - Bullet Point 2
               - Bullet Point 3
               Key words: [keyword1, keyword2, keyword3]
               Story: Brief engaging story related to the slide content.
            2) Prompt: Detailed visual description to generate image relevant to the slide
            3) Speaker Hint: Full speech text for the presenter to follow.

            Slide X: Conclusion
            1) Text: 
               - Summarize key points.
               - Call to action or final thoughts.
               Story: Wrap up the presentation with a powerful closing message.
            2) Prompt: Visual description of a conclusion with emphasis on the summary and final thoughts.
            3) Speaker Hint: "To sum up, we've explored... Remember to take action on..."

            Slide Y: Source List
            1) Text: 
               - Source 1: Link
               - Source 2: Link
               - Source 3: Link
               Key words: [sources, references, links]
               Story: Provide credibility by listing all the sources.
            2) Prompt: Visual description of a slide listing all the sources with links.
            3) Speaker Hint: "Here are the sources we referenced throughout the presentation. You can find more details at these links..."

            Slide Z: Q&A
            1) Text: 
               - Title: Questions & Answers
               - Instruction: "Feel free to ask any questions."
            2) Prompt: Visual description of a Q&A slide inviting audience participation.
            3) Speaker Hint: "We've covered a lot today. Now, I'd like to open the floor to any questions you might have..."
            """)
        )

    def create_a_story(self, agent, text, topic, interests, pain_point, type_of_presentation='Tech Talk'):
        return Task(
            description=dedent(
                f"""
                **Task**: Enhance the text using storytelling techniques.
                **Description**: Transform the provided text into an engaging story. Use techniques such as character creation, humor, and narrative flow to make the content relatable and interesting.

                **Parameters**: 
                - Topic: {topic}
                - Public Interests: {interests}
                - Type of the presentation: {type_of_presentation}
                - Public's pain point: {pain_point}

                **Dependencies**:
                - Input text from copywriter: {text}

                **Note**: {self.__tip_section()}
                """
            ),
            agent=agent,
            dependencies=[text],
            expected_output="""
            Professionally written short article that is easy to learn and understand. The text should be engaging and use storytelling techniques effectively.
            """
        )

    def rewrite_research_paper(self, agent, text, topic):
        return Task(
            description=dedent(
                f"""
                **Task**: Rewrite the research paper to make it concise and clear.
                **Description**: Condense the research paper into concise and easy-to-understand content while retaining all essential information. Ensure the rewritten text is suitable for professionals.

                **Parameters**: 
                - Topic: {topic}

                **Dependencies**:
                - Input text from researcher: {text}

                **Note**: {self.__tip_section()}
                """
            ),
            agent=agent,
            dependencies=[text],
            expected_output="""
            Concise and well-organized text that presents the research information clearly and effectively.
            """
        )

    def research_subject(self, agent, topic):
        return Task(
            description=dedent(
                f"""
                **Task**: Gather comprehensive information on the subject.
                **Description**: Conduct thorough research on the topic. Collect key information, practical tips, and interesting facts to create a well-rounded and informative research paper.

                **Parameters**: 
                - Topic: {topic}

                **Note**: {self.__tip_section()}
                """
            ),
            agent=agent,
            expected_output=f"""
            A detailed research paper containing all essential information about {topic}. The paper should be thorough, well-structured, and include practical tips and interesting facts.
            """
        )

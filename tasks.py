from crewai import Task
from textwrap import dedent

class TechTalkTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def create_presentation_text(self, agent, input_text, topic, length):
        return Task(
            description=dedent(
                f"""
                **Task**: Create a detailed blueprint of the presentation.
                **Description**: Write text for each PowerPoint slide,
                recommend what type of visuals to show on each slide.
                Recommend what fonts could be nice for this type of
                presentation.
                **Parameters**: 
                - Input Text: {input_text}
                - Topic: {topic}
                - Length of the presentation: {length}
                **Note**: {self.__tip_section()}
                """
            ),
            agent=agent,
            expected_output="""
            Text in format:
            Recommended Font: Font_Name
            slide slide_number: Title_of_the_slide
            1) Text: Text_for_the_slide
            2) Prompt: Prompt_to_generate_the_image_using_DALL-E_3
            3) Speaker Hint: Text to put in the notes for the speaker in order
            to know what to tell.
            """
        )

    def create_a_story(self, agent, input_text, topic, interests, pain_point, type='Tech Talk'):
        return Task(
            description=dedent(
                f"""
                **Task**: Change the text by using the best storytelling techniques.
                **Description**: Use the text you have received and apply all
                necessary storytelling techniques that can help to tell this material
                as a complete nicely written story. Create characters, use different
                styles, jokes, etc to make the boring text as enjoyable by public
                as possible.
                **Parameters**: 
                - Input Text: {input_text}
                - Topic: {topic}
                - Public Interests: {interests}
                - Type of the presentation: {type}
                - Public's pain point: {pain_point}
                **Note**: {self.__tip_section()}
                """
            ),
            agent=agent,
            expected_output="""
            Professionally written short article that is easy to learn and understand.
            """
        )

    def rewrite_research_paper(self, agent, input_text, topic):
        return Task(
            description=dedent(
                f"""
                **Task**: Rewrite the research paper to make it concise.
                **Description**: Use the research paper and rewrite it by
                keeping the most important information from there that is
                needed in order to describe the topic and make it easy to
                understand to your colleagues.
                **Parameters**: 
                - Input Text: {input_text}
                - Topic: {topic}
                **Note**: {self.__tip_section()}
                """
            ),
            agent=agent,
            expected_output="""
            Text that arranges material to make it easy to learn step-by-step,
            starting from zero and going more and more in-depth.
            """
        )

    def research_subject(self, agent, topic):
        return Task(
            description=dedent(
                f"""
                **Task**: Gather In-depth Subject Information.
                **Description**: Gather in-depth all the information about
                the topic: key knowledge needed in order to use it, some
                life-hacks and ways of how to use the topic more efficiently,
                and interesting facts about the topic in order to teach the
                audience.
                **Parameters**: 
                - Topic: {topic}
                **Note**: {self.__tip_section()}
                """
            ),
            agent=agent,
            expected_output=f"""
            A research paper that has everything important in order to know
            enough about the {topic} to understand it and to be able to use
            the knowledge about the {topic}.
            """
        )

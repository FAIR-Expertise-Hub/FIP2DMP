from dmp_questions import *

class DMP:
    def __init__(self):
        # Initialize the DMP with an empty dictionary of sections
        self.sections = {}
        # Initialize a counter to generate unique section IDs
        self.section_id_counter = 0

    def add_section(self, section_name, section_id=None):
        # If no section ID is provided, generate a unique one
        if section_id is None:
            section_id = self.section_id_counter
            self.section_id_counter += 1
        # Add the new section to the DMP's sections dictionary
        self.sections[section_name] = {"SectionID": section_id, "Questions": {}}

    def add_question(self, section_name, question_id, question_text, fip_question):
        # Add the new question to the specified section's Questions dictionary
        self.sections[section_name]["Questions"][question_id] = {"QuestionText": question_text, "FIPQuestion": fip_question}

    def print_sections(self):
        # Iterate through each section in the DMP and print its name and ID
        for section_name, section in self.sections.items():
            print(f"{section_name}\n\tSectionID: {section['SectionID']}")
            # Iterate through each question in the section and print its ID, text, and associated FIP questions
            for question_id, question in section["Questions"].items():
                fip_question_str = "[" + ", ".join([q.question_id for q in question["FIPQuestion"]]) + "]"
                print(f"\tQuestion {question_id}\n\t\tQID: {question_id}\n\t\tQuestionText: {question['QuestionText']}\n\t\tFIPQuestion: {fip_question_str}")


# Create DMP and add sections/questions
vu_dmp = DMP()
vu_dmp.add_section("Section 0")
vu_dmp.add_section("Section 1")
vu_dmp.add_section("Section 2")
vu_dmp.add_section("Section 3")
vu_dmp.add_section("Section 4")
vu_dmp.add_section("Section 5")
vu_dmp.add_section("Section 6")


for question in vu_dmp_questions:
    section_prefix = question.question_id.split('.')[0]
    section_name = f"Section {section_prefix}"
    vu_dmp.add_question(section_name, question.question_id, question.question_text, question.fip_questions)


# Print Sections and Questions
vu_dmp.print_sections()

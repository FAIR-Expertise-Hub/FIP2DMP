from fip_questions import fip_questions

class Question:
    """
    Represents a question in a DMP.

    Attributes:
        question_id (str): The identifier for the question.
        question_text (str): The text of the question.
        fip_questions (list): A list of FIPQuestions associated with the question.
    """
    def __init__(self, question_id, question_text, fip_question_ids=[]):
        self.question_id = question_id
        self.question_text = question_text
        self.fip_questions = []
        
        # Populates the list of associated FIP questions by checking if each provided FIP question ID exists in the fip_questions dictionary
        for fip_question_id in fip_question_ids:
            if fip_question_id in fip_questions:
                self.fip_questions.append(fip_questions[fip_question_id])
            else:
                # Prints an error message if a provided FIP question ID does not exist in the fip_questions dictionary
                print(f"Error: FIP question {fip_question_id} does not exist")

    def __str__(self):
        return f"QuestionText: {self.question_text}\nFIPQuestion: {self.fip_question}"


vu_dmp_questions = [
    Question("0.1", "Document version & date"),
    Question("0.2", "Project Title"),
    Question("0.3", "Project Summary"),
    Question("0.4", "Your contact details", ["F1-MD"]),
    Question("0.5", "List other people involved (incl. partner organization) in the project", ["F1-MD"]),
    Question("0.6", "Funding organization & grant number", ["F1-MD"]),
    Question("0.7", "Project code"),
    Question("0.8", "Consulted data management expert", ["F1-MD"]),

    Question("1.1", "Will you collect and/or process personal data in this project?"),
    Question("1.2", "Will you use existing data?"),
    Question("1.3", "Will you collect or produce new data?"),
    Question("1.4", "Describe the population/participants/subjects that will be studied"),
    Question("1.5", "Do you process any of the following (personal) data?"),
    Question("1.6", "Do you process the personal data based on informed consent?"),
    Question("1.7", "On what legal ground will the data processing take place if it is not based on informed consent?"),
    Question("1.8", "Does the data collection include any of the following types of personal data?"),
    Question("1.9", "If your research involves special categories of personal data and you will not use explicit informed consent, what is the legal ground for exemption?"),
    Question("1.10", "What kinds of outputs will you produce in this project?"),
    Question("1.11", "How much digital data storage will your project require?"),
    Question("1.12", "Will you collect physical data?"),
    Question("1.13", "Will you take measures to ensure data quality?"),

    Question("2.1", "What legislation applies to your research project?"),
    Question("2.2", "What legislation applies to your research project?"),
    Question("2.3", "Do you require approval of an ethical committee for this project?"),
    Question("2.4", "Will you work with data for which intellectual property and/or confidentiality are an issue?"),
    Question("2.5", "Do you plan on generating a marketable product from your research project?"),

    Question("3.1", "What measures will you take to secure and protect data during the research process?"),
    Question("3.2", "What measures will you take to secure and protect data during the research process?"),
    Question("3.3", "Which tools are used in the collection, processing or storage of data during research?"),
    Question("3.4", "What other tools or software do you intend to use during your research?"),
    Question("3.5", "Is it necessary to transfer the (physical or digital) data assets to other locations or research partners?"),
    Question("3.6", "Is it necessary to transfer the (physical or digital) data assets to other locations or research partners?"),
    Question("3.7", "Do you transfer personal data outside of the European Economic Area (EEA)?"),

    Question("4.1", "Which data assets will be archived and which will be published?"),
    Question("4.2", "Where will you archive your data assets?", ["F4-MD", "F4-D"]),
    Question("4.3", "What other archive(s) do you intend to use to archive data assets?", ["F4-MD", "F4-D"]),
    Question("4.4", "For how long will the data be available in the archive?"),
    Question("4.5", "For how long will the data be available in the archive?"),
    Question("4.6", "Where will you publish your data assets?", ["F4-MD", "F4-D"]),
    Question("4.7", "Where will you publish your data assets?", ["F4-MD", "F4-D"]),
    Question("4.8", "How will you ensure your data assets get a persistent identifier?", ["F1-MD", "F1-D"]),
    Question("4.9", "Will you register your datasets in an online registry other than PURE?", ["F1-MD", "F1-D"]),
    Question("4.10", "Are there restrictions to data publishing?", ["A1.2-MD", "A1.2-D"]),
    Question("4.11", "Are there restrictions to data publishing?", ["A1.2-MD", "A1.2-D"]),
    Question("4.12", "When will you share the data?"),
    Question("4.13", "Please indicate the license and/ or terms of use under which you share your data.", ["R1.1-MD", "R1.1-D"]),

    Question("5.1", "What metadata and documentation will accompany the project?", ["R1.2-MD", "F2"]),
    Question("5.2", "What metadata and documentation will accompany the data assets?", ["F2"]),
    Question("5.3", "What methods, software or hardware are needed to access and use your data?", ["R1.2-MD", "R1.2-D"]),
    # Added 2 new questions here 5.4/5.5 for the new VU DMP
    Question("5.4", "What's the domain-specific vocabularies that you use in metadata that can make your dataset findable/interoperable? ", ["I2-MD"]),
    Question("5.5", "What's the domain-specific vocabularies that you use in data that can make your dataset findable/interoperable? ", ["I2-D"]),

    Question("6.1", "Who will be responsible for management of the data assets during the project?"),
    Question("6.2", "Who will be responsible for management of the data assets after completion of the project?"),
    Question("6.3", "For data that are only available upon request, what methods will be used to handle requests for access and how will data be made available to those requesting access?", ["A1.2-MD", "A1.2-D"]),
    Question("6.4", "What resources will be dedicated to research data management?")
]

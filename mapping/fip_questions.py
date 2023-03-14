from enum import Enum

class FERType(Enum):
    AUTHENTICATION_AND_AUTHORIZATION_SERVICE = "Authentication and authorization service"
    COMMUNICATION_PROTOCOL = "Communication protocol"
    DATA_USAGE_LICENSE = "Data usage license"
    IDENTIFIER_SERVICE = "Identifier service"
    KNOWLEDGE_REPRESENTATION_LANGUAGE = "Knowledge representation language"
    METADATA_PRESERVATION_POLICY = "Metadata preservation policy"
    METADATA_SCHEMA = "Metadata schema"
    METADATA_DATA_LINKING_SCHEMA = "Metadata-data linking schema"
    PROVENANCE_MODEL = "Provenance model"
    REGISTRY = "Registry"
    SEMANTIC_MODEL = "Semantic model"
    STRUCTURED_VOCABULARY = "Structured vocabulary"


class FIPQuestion:
    """
    Represents a FIP question.

    Attributes:
        question_id (str): The identifier for the FIP question.
        question_text (str): The text of the FIP question.
        fer_type (FERType): The type of FER for the FIP question.
    """
    def __init__(self, question_id: str, question_text: str, fer_type: FERType) -> None:
        self.question_id = question_id
        self.question_text = question_text
        self.fer_type = fer_type

    def __str__(self) -> str:
        return f"FIP question {self.question_id}: {self.question_text}, {self.fer_type}"
    

# Define FIP Questions
fip_questions = {
    "F1-MD": FIPQuestion(
        "F1-MD",
        "What globally unique, persistent, resolvable identifiers do you use for metadata records?",
        FERType.IDENTIFIER_SERVICE.value
    ),
    "F1-D": FIPQuestion(
        "F1-D",
        "What globally unique, persistent, resolvable identifiers do you use for datasets?",
        FERType.IDENTIFIER_SERVICE.value
    ),
    "F2": FIPQuestion(
        "F2",
        "Which metadata schemas do you use for findability?",
        FERType.METADATA_SCHEMA.value
    ),
    "F3": FIPQuestion(
        "F3",
        "What is the technology that links the persistent identifiers of your data to the metadata description?",
        FERType.METADATA_DATA_LINKING_SCHEMA.value
    ),
    "F4-MD": FIPQuestion(
        "F4-MD",
        "In which search engines are your metadata records indexed?",
        FERType.REGISTRY.value
    ),
    "F4-D": FIPQuestion(
        "F4-D",
        "In which search engines are your datasets indexed?",
        FERType.REGISTRY.value
    ),
    "A1.1-MD": FIPQuestion(
        "A1.1-MD",
        "Which standardized communication protocol do you use for metadata records?",
        FERType.COMMUNICATION_PROTOCOL.value
    ),
    "A1.1-D": FIPQuestion(
        "A1.1-D",
        "Which standardized communication protocol do you use for datasets?",
        FERType.COMMUNICATION_PROTOCOL.value
    ),
    "A1.2-MD": FIPQuestion(
        "A1.2-MD",
        "Which authentication & authorisation technique do you use for metadata records?",
        FERType.AUTHENTICATION_AND_AUTHORIZATION_SERVICE.value
    ),
    "A1.2-D": FIPQuestion(
        "A1.2-D",
        "Which authentication & authorisation technique do you use for datasets?",
        FERType.AUTHENTICATION_AND_AUTHORIZATION_SERVICE.value
    ),
    "A2": FIPQuestion(
        "A2",
        "Which metadata longevity plan do you use?",
        FERType.METADATA_PRESERVATION_POLICY.value
    ),
    "I1-MD": FIPQuestion(
        "I1-MD",
        "Which knowledge representation languages (allowing machine interoperation) do you use for metadata records?",
        FERType.KNOWLEDGE_REPRESENTATION_LANGUAGE.value
    ),
    "I1-D": FIPQuestion(
        "I1-D",
        "Which knowledge representation languages (allowing machine interoperation) do you use for datasets?",
        FERType.KNOWLEDGE_REPRESENTATION_LANGUAGE.value
    ),
    "I2-MD": FIPQuestion(
        "I2-MD",
        "Which structured vocabularies do you use to annotate your metadata records?",
        FERType.STRUCTURED_VOCABULARY.value
    ),
    "I2-D": FIPQuestion(
        "I2-D",
        "Which structured vocabularies do you use to encode your datasets?",
        FERType.STRUCTURED_VOCABULARY.value
    ),
    "I3-MD": FIPQuestion(
        "I3-MD",
        "Which models, schema(s) do you use for your metadata records?",
        FERType.SEMANTIC_MODEL.value
    ),
    "I3-D": FIPQuestion(
        "I3-D",
        "Which models, schema(s) do you use for your datasets?",
        FERType.SEMANTIC_MODEL.value
    ),
    "R1.1-MD": FIPQuestion(
        "R1.1-MD",
        "Which usage license do you use for your metadata records?",
        FERType.DATA_USAGE_LICENSE.value
    ),
    "R1.1-D": FIPQuestion(
        "R1.1-D",
        "Which usage license do you use for your datasets?",
        FERType.DATA_USAGE_LICENSE.value
    ),
    "R1.2-MD": FIPQuestion(
        "R1.2-MD",
        "Which metadata schemas do you use for describing the provenance of your metadata records?",
        FERType.PROVENANCE_MODEL.value
    ),
    "R1.2-D": FIPQuestion(
        "R1.2-D",
        "Which metadata schemas do you use for describing the provenance of your datasets?",
        FERType.PROVENANCE_MODEL.value
    )
}

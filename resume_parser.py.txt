import spacy

# Load English tokenizer, POS tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Define a simple skill list for demo
SKILLS_DB = [
    "Python", "Java", "Django", "SQL", "Git", "REST APIs",
    "Data Analysis", "Machine Learning", "Communication", "AWS",
]

def extract_skills_from_resume(text):
    doc = nlp(text)
    extracted_skills = set()

    for token in doc:
        if token.text in SKILLS_DB:
            extracted_skills.add(token.text)

    return list(extracted_skills)

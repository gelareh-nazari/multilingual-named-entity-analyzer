import spacy
english_nlp = spacy.load("en_core_web_sm")
german_nlp = spacy.load("de_core_news_sm")


def analyze_text(text, language):
    if language == "English":
        doc = english_nlp(text)
    elif language == "German":
        doc = german_nlp(text)
    else:
        raise ValueError("Unsupported language")

    entities = []

    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_,
            "start": ent.start_char,
            "end": ent.end_char
        })

    return entities


def get_doc(text, language):
    if language == "English":
        return english_nlp(text)
    elif language == "German":
        return german_nlp(text)
    else:
        raise ValueError("Unsupported language")

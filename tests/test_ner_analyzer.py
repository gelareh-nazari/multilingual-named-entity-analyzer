from ner_analyzer import analyze_text
import pytest

def test_english_entities():
    text = "Microsoft opened a new office in Berlin in July 2026."

    result = analyze_text(text, "English")

    entity_texts = [entity["text"] for entity in result]

    assert "Microsoft" in entity_texts
    assert "Berlin" in entity_texts
    assert "July 2026" in entity_texts


    
def test_german_entities():
    text = "Siemens eröffnete im Juli 2026 ein neues Büro in München."

    result = analyze_text(text, "German")

    entity_texts = [entity["text"] for entity in result]

    assert "Siemens" in entity_texts
    assert "München" in entity_texts


def test_unsupported_language():
    with pytest.raises(ValueError):
        analyze_text("This is a test.", "French")

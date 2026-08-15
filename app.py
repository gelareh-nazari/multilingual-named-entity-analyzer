import streamlit as st
from spacy import displacy

from ner_analyzer import analyze_text, get_doc
from database import create_database, save_analysis, get_analysis_history

import pandas as pd

create_database()

LABEL_DESCRIPTIONS = {
    "PERSON": "Person",
    "PER": "Person",
    "ORG": "Organization",
    "GPE": "Country, city, or state",
    "LOC": "Location",
    "DATE": "Date",
    "MONEY": "Money",
    "QUANTITY": "Quantity",
    "CARDINAL": "Number"
}


st.set_page_config(
    page_title="Multilingual_Named_Entity_Analyzer",
    page_icon="🌍",
    layout="wide"

)

st.title("Multilingual Named Entity Analyzer")

st.write(
    "Analyze English and German text and explore named entities "
    "such as people, organizations, locations, and dates."
)

language = st.selectbox(
    "Select language:",
    ["English", "German"]
)

text = st.text_area(
    "Enter text for analysis:",
    height=200,
    placeholder="Enter an English or German text here..."
)
if st.button("Analyze"):
    if text.strip():
        results = analyze_text(text, language)
        save_analysis(text, language)
        doc = get_doc(text, language)

        if results:
            st.subheader("Detected Entities")
            st.write(f"Total entities detected: {len(results)}")
            for entity in results:
                entity["description"] = LABEL_DESCRIPTIONS.get(
                    entity["label"],
                    "Other"
                )
            st.dataframe(results, width="stretch")
            df = pd.DataFrame(results)
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download results as CSV",
                data=csv,
                file_name="ner_results.cvs",
                mime="text/csv"
            )

            html = displacy.render(doc, style="ent")
            st.markdown(html, unsafe_allow_html=True)

            st.subheader("Entity Statistics")

            label_counts = {}

            for entity in results:
                label = entity["label"]
                label_counts[label] = label_counts.get(label, 0) + 1

            st.bar_chart(label_counts)

        else:
            st.info("No named entities were detected in the text.")
    else:
        st.warning("Please enter some text before starting the analysis.")

st.subheader("Analysis History")
history = get_analysis_history()

if history:
    history_df = pd.DataFrame(history, columns=["ID", "Text", "Language"])
    st.dataframe(history_df, width="stretch", hide_index=True)

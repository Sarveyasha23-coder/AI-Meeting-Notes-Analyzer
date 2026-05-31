import streamlit as st

from workflow import graph

st.set_page_config(
    page_title="AI Meeting Notes Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title(
    "🤖 AI Meeting Notes Analyzer"
)

uploaded = st.file_uploader(
    "Upload Meeting Transcript",
    type=["txt"]
)

if uploaded:

    transcript = (
        uploaded.read()
        .decode("utf-8")
    )

    with st.spinner(
        "Analyzing Meeting..."
    ):

        result = graph.invoke(
            {
                "transcript": transcript
            }
        )

    st.subheader(
        "Meeting Summary"
    )

    st.write(
        result["summary"]
    )

    st.subheader(
        "Key Topics"
    )

    st.write(
        result["topics"]
    )

    st.subheader(
        "Action Items"
    )

    st.write(
        result["actions"]
    )

    st.subheader(
        "Priority"
    )

    st.success(
        result["priority"]
    )

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

# -----------------------------
# Load Gemini API Key
# -----------------------------
try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
except Exception:
    raise ValueError(
        """
        GOOGLE_API_KEY not found.

        For Streamlit Cloud:
        App Settings → Secrets

        Add:

        GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
        """
    )

# -----------------------------
# Initialize Gemini Model
# -----------------------------
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.3
    )
except Exception as e:
    raise ValueError(
        f"Failed to initialize Gemini model: {str(e)}"
    )

# -----------------------------
# Topic Extraction Agent
# -----------------------------
def topic_agent(text):

    prompt = f"""
    You are an expert meeting analyst.

    Extract the main discussion topics from the transcript.

    Return:
    - Bullet points only
    - No explanations

    Transcript:
    {text}
    """

    response = llm.invoke(prompt)

    return response.content


# -----------------------------
# Meeting Summary Agent
# -----------------------------
def summary_agent(text):

    prompt = f"""
    You are an expert meeting analyst.

    Summarize this meeting in 3 to 5 concise sentences.

    Focus on:
    - Main discussion
    - Decisions made
    - Goals

    Transcript:
    {text}
    """

    response = llm.invoke(prompt)

    return response.content


# -----------------------------
# Action Item Agent
# -----------------------------
def action_agent(text):

    prompt = f"""
    Extract all action items.

    For each action item provide:

    Task:
    Owner:

    If no action items exist,
    return exactly:

    NO ACTION ITEMS

    Transcript:
    {text}
    """

    response = llm.invoke(prompt)

    return response.content


# -----------------------------
# Priority Agent
# -----------------------------
def priority_agent(text):

    prompt = f"""
    Determine the overall priority.

    Rules:

    High Priority:
    - urgent
    - asap
    - today
    - tomorrow
    - by friday
    - this week

    Medium Priority:
    - planned work
    - near future work

    Low Priority:
    - discussion only
    - no urgency

    Return ONLY ONE:

    High
    Medium
    Low

    Transcript:
    {text}
    """

    response = llm.invoke(prompt)

    return response.content.strip()


# -----------------------------
# Health Check Function
# -----------------------------
def test_connection():

    try:

        response = llm.invoke(
            "Reply with only: Connection Successful"
        )

        return response.content

    except Exception as e:

        return f"Connection Error: {str(e)}"

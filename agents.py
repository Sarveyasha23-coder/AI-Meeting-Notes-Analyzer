from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def topic_agent(text):

    prompt = f"""
    Extract key discussion topics.

    Transcript:
    {text}

    Return bullet points only.
    """

    return llm.invoke(prompt).content


def summary_agent(text):

    prompt = f"""
    Summarize this meeting in 3-5 sentences.

    Transcript:
    {text}
    """

    return llm.invoke(prompt).content


def action_agent(text):

    prompt = f"""
    Extract all action items.

    Return:
    Task
    Owner

    If no action items exist,
    return exactly:
    NO ACTION ITEMS
    """

    return llm.invoke(prompt).content


def priority_agent(text):

    prompt = f"""
    Classify meeting priority.

    Output only:

    High
    Medium
    Low

    Transcript:
    {text}
    """

    return llm.invoke(prompt).content

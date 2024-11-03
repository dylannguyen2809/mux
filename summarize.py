from openai import OpenAI

client = OpenAI()

def summarize_conversation(transcript_list):
    """
    Summarizes a conversation transcript using OpenAI's API.

    Parameters:
    transcript_list (list of str): A list of strings representing the conversation transcript.

    Returns:
    str: A summary of the conversation.
    """
    # Join the list of strings into a single string
    conversation = "\n".join(transcript_list)

    # Call the OpenAI API to summarize the conversation
    response = client.chat.completions.create(model="gpt-4o-mini",  # or any other model you prefer
    messages=[
        {"role": "user", "content": f"Please summarize the following conversation:\n{conversation}"}
    ])

    # Extract the summary from the response
    summary = response.choices[0].message.content
    return summary

# Example usage
if __name__ == "__main__":
    conversation_transcript = [
        "User: Hi, how are you?",
        "Assistant: I'm good, thank you! How can I help you today?",
        "User: I wanted to know about the weather.",
        "Assistant: Sure! What location are you interested in?",
        "User: New York City.",
        "Assistant: The weather in New York City is currently sunny with a high of 75°F."
    ]

    summary = summarize_conversation(conversation_transcript)
    print("Summary of the conversation:")
    print(summary)
import requests
from openai import OpenAI
import os

client = OpenAI()

# Function to fetch and summarize the latest news article
def get_latest_news(api_key, query, target_language='en'):
    url = f'https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api_key}'
    response = requests.get(url)
    articles = response.json().get('articles', [])
    
    if not articles:
        return "No articles found."
    
    latest_article = articles[0]
    title = latest_article['title']
    description = latest_article['description']
    content = latest_article['content']
    
    summary = f"Title: {title}\nDescription: {description}\nContent: {content}..."  # Truncate content for brevity
        
    return summary

# Function to send the summary to ChatGPT
def send_to_chatgpt(summary, language):    
    completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Here is a news article summary:\n\n{summary}\n\nPlease translate this into {language}."
                }
            ]
        )
    return completion.choices[0].message.content

# Function definition for OpenAI API
function_definition = {
    "name": "get_latest_news",
    "description": "Fetch and summarize the latest news article.",
    "parameters": {
        "type": "object",
        "properties": {
            "api_key": {"type": "string", "description": "API key for News API."},
            "query": {"type": "string", "description": "Search query for news articles."},
            "target_language": {"type": "string", "description": "Language code for translation."}
        },
        "required": ["api_key", "query"],
        "additionalProperties": False
    }
}

# Example usage
news_api_key = '0e609076b759448fa77f3cff7d0b38bc'
openai_api_key = os.getenv("OPENAI_APIKEY")
query = 'latest news'

summary = get_latest_news(news_api_key, query)  # Translate to Spanish
chatgpt_response = send_to_chatgpt(summary, "chinese")
print(chatgpt_response)

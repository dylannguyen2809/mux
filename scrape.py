# Step 0. Importing relevant Langchain libraries
from langchain_community.adapters.openai import convert_openai_messages
from langchain_community.chat_models import ChatOpenAI

from firecrawl import FirecrawlApp
from firecrawl import FirecrawlApp
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

tavily_key = os.getenv("Tavily_API")
firecrawl_key = os.getenv("Firecrawl_API")

# Step 1. Instantiating your TavilyClient
from tavily import TavilyClient
client = TavilyClient(api_key=tavily_key)

results = client.search("Find current news articles", include_answer=True, search_depth="advanced", topic='news', max_results=3)
urls_extracted = [response['url'] for response in results['results']]

# Step 3. That's it! You've done a Tavily Search!
print(urls_extracted)

# Initialize the FirecrawlApp with your API key
app = FirecrawlApp(api_key=firecrawl_key)

class ExtractSchema(BaseModel):
    article_summary: str
    title: str
    
for url in urls_extracted:
    data = app.scrape_url(url, {
        'formats': ['extract'],
        'extract': {
            'schema': ExtractSchema.model_json_schema(),
        }
    })
    print(data["extract"])
    
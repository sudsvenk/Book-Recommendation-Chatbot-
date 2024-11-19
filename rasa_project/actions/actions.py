# actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import random

class ActionSearchBook(Action):
    def name(self) -> Text:
        return "action_search_book"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the search query from user's message
        query = tracker.latest_message.get('text')
        
        # Google Books API endpoint
        api_key = "AIzaSyD35BlViGcJmAekWkiJZMVMLh7NCJK4xnM"
        base_url = "https://www.googleapis.com/books/v1/volumes"
        
        # Make API request
        params = {
            "q": query,
            "key": api_key,
            "maxResults": 3
        }
        
        response = requests.get(base_url, params=params)
        books = response.json()
        
        if "items" in books:
            for book in books["items"]:
                title = book["volumeInfo"].get("title", "No title available")
                authors = ", ".join(book["volumeInfo"].get("authors", ["Unknown author"]))
                description = book["volumeInfo"].get("description", "No description available")[:200] + "..."
                
                message = f"📚 {title}\nBy: {authors}\n\nDescription: {description}"
                dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="I couldn't find any books matching your query.")
        
        return []

class ActionRecommendBook(Action):
    def name(self) -> Text:
        return "action_recommend_book"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get user preferences from the conversation
        # This is a simple implementation - you can make it more sophisticated
        genres = ["fiction", "mystery", "science fiction", "romance", "non-fiction"]
        genre = random.choice(genres)
        
        # Google Books API request for the chosen genre
        api_key = "YOUR_GOOGLE_BOOKS_API_KEY"
        base_url = "https://www.googleapis.com/books/v1/volumes"
        
        params = {
            "q": f"subject:{genre}",
            "key": api_key,
            "maxResults": 1,
            "orderBy": "relevance"
        }
        
        response = requests.get(base_url, params=params)
        books = response.json()
        
        if "items" in books:
            book = books["items"][0]
            title = book["volumeInfo"].get("title", "No title available")
            authors = ", ".join(book["volumeInfo"].get("authors", ["Unknown author"]))
            description = book["volumeInfo"].get("description", "No description available")[:200] + "..."
            
            message = f"Based on your interests, I recommend:\n\n📚 {title}\nBy: {authors}\n\nDescription: {description}"
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="I'm sorry, I couldn't find a recommendation at the moment.")
        
        return []
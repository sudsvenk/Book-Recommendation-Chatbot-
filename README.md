# Book Recommendation Chatbot

A conversational AI chatbot built with Rasa that helps users find and get book recommendations using the Google Books API.

## Features

- Book search functionality
- Personalized book recommendations
- Integration with Google Books API
- Web-based chat interface

## Prerequisites

- Python 3.8 or higher
- Rasa 3.x
- Google Books API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/book-recommendation-chatbot.git
cd book-recommendation-chatbot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your Google Books API key:
- Get an API key from the Google Cloud Console
- Add it to your environment variables:
  ```bash
  export GOOGLE_BOOKS_API_KEY=your_api_key_here
  ```

## Running the Chatbot

1. Train the Rasa model:
```bash
cd rasa_project
rasa train
```

2. Start the Rasa action server (in a separate terminal):
```bash
rasa run actions
```

3. Start the Rasa server (in a separate terminal):
```bash
rasa run --enable-api --cors "*"
```

4. Start the web server (in a separate terminal):
```bash
python serve.py
```

5. Open your web browser and navigate to:
```
http://localhost:8000
```

## Project Structure

- `index.html`: Web-based chat interface
- `serve.py`: Simple HTTP server for serving the web interface
- `rasa_project/`: Main Rasa project directory
  - `actions/`: Custom action code
  - `data/`: Training data
  - `config.yml`: Rasa configuration
  - `domain.yml`: Domain specification
  - `endpoints.yml`: Endpoint configuration

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

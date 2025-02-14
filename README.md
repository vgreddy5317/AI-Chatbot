# AI Chatbot with Gemini API

A modern, responsive chatbot built with Streamlit and powered by Google's Gemini AI. This application provides an intuitive chat interface for interacting with Google's advanced language model.

## Features

- Clean, modern user interface
- Real-time chat interactions
- Error handling and recovery
- Message history management
- Responsive design
- Custom styling

## Project Structure

```
├── main.py              # Main application file
├── styles.css           # Custom CSS styling
├── .env                 # Environment variables
├── .streamlit/
│   └── config.toml     # Streamlit configuration
└── pyproject.toml      # Python dependencies
```

## File Descriptions

1. `main.py`: Contains the core application logic, Streamlit UI components, and Gemini AI integration.
2. `styles.css`: Custom styling for chat messages, input area, and overall layout.
3. `.env`: Configuration file for API keys (Google Gemini API key).
4. `.streamlit/config.toml`: Streamlit server configuration.
5. `pyproject.toml`: Python project dependencies.

## Required Environment Variables

- `GOOGLE_API_KEY`: Your Google Gemini API key

## Dependencies

- streamlit
- google-generativeai
- python-dotenv
- time

## Usage

1. Ensure all dependencies are installed
2. Set up your environment variables
3. Run the application using: `streamlit run main.py`
4. Access the chat interface through your web browser

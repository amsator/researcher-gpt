# Researcher GPT

This project exposes a small FastAPI service that wraps a LangChain based research agent. The service provides search and web scraping tools to gather information on a given topic.

## Setup

1. Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
```

2. Provide the required API keys via environment variables:

- `BROWSERLESS_API_KEY` – Browserless API token used for scraping
- `SERP_API_KEY` – Serper API key used for search
- `OPENAI_API_KEY` – OpenAI API key used by LangChain

You can place these in a `.env` file in the project root.

## Running the API

Start the FastAPI server with `uvicorn`:

```bash
uvicorn app:app --reload
```

The service exposes a single `POST /` endpoint that accepts a JSON body of the form `{"query": "your research goal"}` and returns the agent's response.

## Testing

Basic unit tests are provided using `pytest`:

```bash
pytest
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

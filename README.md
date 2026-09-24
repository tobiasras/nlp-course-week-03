# Text to persons

Assignment for a DTU NLP course: extract person names from text with the CampusAI LLM API and DSPy.

`POST /v1/extract-persons` takes JSON `{"text": "..."}` and returns:

```json
{ "persons": ["Einstein", "von Neumann"] }
```

The backend is FastAPI on port **8000**. The demo UI on port **8001** was provided by the course; it can try examples, show latency, and run the built-in test set.

## Result

On the UI test dataset the service scored **37 / 40**.

## Run

Put your CampusAI key in `backend/.env` (do not commit the key):

```
CAMPUSAI_API_KEY=sk-...
CAMPUSAI_MODEL=google/gemma-4-26b-a4b
CAMPUSAI_EMBED_MODEL=cai-embedding
CAMPUSAI_API_URL=https://api.campusai.compute.dtu.dk/v1
```

Then:

```bash
docker compose up --build
```

- API docs: http://127.0.0.1:8000/docs
- Demo UI: http://localhost:8001

```bash
curl -s -X POST http://localhost:8000/v1/extract-persons \
  -H 'Content-Type: application/json' \
  -d '{"text":"Einstein and von Neumann meet each other."}'
```

## Tests

```bash
python -m pytest test/backend/test_main.py
```

`test_examples_from_prompt` calls CampusAI for the two examples from the assignment (`Mette Frederiksen`, `Einstein` / `von Neumann`).

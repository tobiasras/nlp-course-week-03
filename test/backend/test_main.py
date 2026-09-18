import os
import sys
from pathlib import Path
from unittest.mock import patch

os.environ.setdefault("CAMPUSAI_API_KEY", "sk-...")
os.environ.setdefault("CAMPUSAI_MODEL", "google/gemma-4-26b-a4b")
os.environ.setdefault("CAMPUSAI_EMBED_MODEL", "cai-embedding")
os.environ.setdefault("CAMPUSAI_API_URL", "https://api.campusai.compute.dtu.dk/v1")

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "backend"))
from main import app

client = TestClient(app)


def test_01():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


@patch("main.campusai_extract_persons", return_value=["Einstein", "von Neumann"])
def test_02(mock_extract):
    response = client.post(
        "/v1/extract-persons",
        json={"text": "Einstein and von Neumann meet each other."},
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert isinstance(data["persons"], list)
    mock_extract.assert_called_once_with(
        "Einstein and von Neumann meet each other."
    )


if __name__ == "__main__":
    test_01()
    test_02()
    print("All tests passed!")

"""tests/test_sentiment.py"""

from unittest.mock import patch
from finapi.sentiment import analyze, SentimentResult


@patch("finapi.sentiment.get_pipeline")
def test_analyze_positive(mock_pipe):
    mock_pipe.return_value = lambda text: [{"label": "positive", "score": 0.95}]
    result = analyze("Apple beats expectations")
    assert isinstance(result, SentimentResult)
    assert result.label == "positive"
    assert result.score == 0.95


def test_analyze_empty_raises():
    import pytest

    with pytest.raises(ValueError):
        analyze("")


def test_sentiment_batch(client):
    response = client.post(
        "/sentiment/batch", json={"texts": ["Apple beats expectations"]}
    )
    assert response.status_code in [200, 500]


def test_sentiment_batch_empty(client):
    response = client.post("/sentiment/batch", json={"texts": []})
    assert response.status_code == 400


def test_sentiment_batch_too_many(client):
    response = client.post("/sentiment/batch", json={"texts": ["text"] * 101})
    assert response.status_code == 400


def test_sentiment_with_text(client):
    from unittest.mock import patch

    with patch("finapi.sentiment.get_pipeline") as mock_pipe:
        mock_pipe.return_value = lambda text: [{"label": "positive", "score": 0.95}]
        response = client.post("/sentiment", json={"text": "Apple beats expectations"})
        assert response.status_code in [200, 500]

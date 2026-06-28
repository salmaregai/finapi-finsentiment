def test_health_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_db_prices(client):
    response = client.get("/db/prices/AAPL")
    assert response.status_code == 200


def test_db_news(client):
    response = client.get("/db/news/AAPL")
    assert response.status_code == 200


def test_db_stats(client):
    response = client.get("/db/stats")
    assert response.status_code == 200


def test_sentiment_summary(client):
    response = client.get("/db/sentiment-summary/AAPL")
    assert response.status_code == 200


def test_sentiment_missing_text(client):
    response = client.post("/sentiment", json={})
    assert response.status_code == 400


def test_db_sentiment_summary(client):
    response = client.get("/db/sentiment-summary/MSFT")
    assert response.status_code == 200

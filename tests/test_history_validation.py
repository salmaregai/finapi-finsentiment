def test_invalid_days(client):
    response = client.get("/history/AAPL?days=abc")
    assert response.status_code == 400


def test_days_out_of_range(client):
    response = client.get("/history/AAPL?days=999")
    assert response.status_code == 400


def test_history_valid(client):
    response = client.get("/history/AAPL?days=5")
    assert response.status_code in [200, 404]


def test_price_valid(client):
    response = client.get("/price/AAPL")
    assert response.status_code in [200, 404]


def test_price_invalid_ticker(client):
    response = client.get("/price/INVALIDTICKER123")
    assert response.status_code == 404

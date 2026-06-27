# FinAPI — API Flask pour cours boursiers

## Installation

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Lancement

python -m finapi.app

## Endpoints

### Health check
curl http://localhost:5000/health

### Prix d'une action
curl http://localhost:5000/price/AAPL

### Historique des prix
curl http://localhost:5000/history/AAPL?days=5
curl http://localhost:5000/history/MSFT?days=30

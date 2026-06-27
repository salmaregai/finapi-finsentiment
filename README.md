# FinAPI — API Flask + ETL + SQLite

## Installation

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Lancement du serveur

python -m finapi.app

## Ingestion des données

python -m scripts.run_etl AAPL MSFT GOOGL

## Endpoints Lab 1

curl http://localhost:5000/health
curl http://localhost:5000/price/AAPL
curl http://localhost:5000/history/AAPL?days=5

## Endpoints Lab 2

curl http://localhost:5000/db/prices/AAPL
curl http://localhost:5000/db/news/MSFT
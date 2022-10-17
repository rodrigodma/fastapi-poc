export $(cat .env)
uvicorn app.main:app --reload
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz():
	return {"projeto": "Gecko BioTracker", "status": "online"}

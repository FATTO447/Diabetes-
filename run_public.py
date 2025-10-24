import nest_asyncio
from pyngrok import ngrok
import uvicorn
from fastapi import FastAPI

nest_asyncio.apply()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Diabetes Predictor API is running"}

public_url = ngrok.connect(8000)
print("Public URL:", public_url)

uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Local Gemma 4B API Configuration (Assuming Ollama)
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma4:e4b" # Adjusted to match user's local model tag

class PromptRequest(BaseModel):
    text: str
    mode: str # 'swap', 'waste', 'challenge'

def build_prompt(text, mode):
    prompts = {
        "swap": f"You are EcoMind AI, a sustainability expert. The user wants a green alternative for: '{text}'. Provide a concise, actionable sustainable alternative in 1-2 sentences. Be positive and encouraging.",
        "waste": f"You are EcoMind AI, a waste management expert. The user is asking how to dispose of: '{text}'. Tell them if it goes in recycle, compost, or landfill, and give a brief reason. Keep it under 2 sentences.",
        "challenge": "You are EcoMind AI. Generate a random, simple, and impactful daily eco-friendly micro-challenge for a beginner (e.g., 'Use a reusable bag today'). Keep it to one short sentence."
    }
    return prompts.get(mode, f"You are EcoMind AI. Answer this: {text}")

@app.post("/api/chat")
async def chat(request: PromptRequest):
    full_prompt = build_prompt(request.text, request.mode)

    try:
        payload = {
            "model": MODEL_NAME,
            "prompt": full_prompt,
            "stream": False
        }
        response = requests.post(OLLAMA_URL, json=payload, timeout=30)
        response.raise_for_status()

        data = response.json()
        return {"response": data.get("response", "I'm sorry, I couldn't generate a response.")}

    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=503, detail="Local AI server (Ollama) not found. Please make sure it is running.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

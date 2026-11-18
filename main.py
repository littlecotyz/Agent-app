from fastapi import FastAPI
from pydantic import BaseModel
from google import genai

# PASTE YOUR AQ... KEY HERE
client = genai.Client(api_key="GEMINI_API_KEY")

app = FastAPI()

class AgentRequest(BaseModel):
    user_id: str
    prompt: str

@app.post("/run-agent")
def run_agent(req: AgentRequest):
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=req.prompt
    )
    return {
        "status": "success",
        "user_id": req.user_id,
        "agent_output": response.text
    }
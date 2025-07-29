from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static folder
app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.post("/get-response")
async def get_response(request: Request):
    data = await request.json()
    user_message = data.get("message", "").strip()
    if user_message.lower() == "ima":
        return JSONResponse(content={"reply": "bye"})
    else:
        return JSONResponse(content={"reply": "You said: " + user_message})

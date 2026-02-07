from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="WV Food Check API")

# Allow your Vercel site to call this API from the browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later we can lock this down to your Vercel domain
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok", "service": "wv-food-check-api"}

@app.get("/v1/health")
def health():
    return {"ok": True}

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <html>
      <head><title>NIFTY50 Intraday Scanner</title></head>
      <body style="font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial;">
        <h1>🚀 NIFTY50 Intraday Scanner</h1>
        <p>Your Render deployment is live.</p>
      </body>
    </html>
    """

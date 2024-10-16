from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>My FastAPI Website</title>
        </head>
        <body>
            <h1>Welcome to My Website</h1>
            <p>This is a simple page built with FastAPI and Python.</p>
        </body>
    </html>
    """

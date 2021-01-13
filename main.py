from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get('/')
def home():
    return FileResponse('client/public/index.html')

# Place After All Other Routes
app.mount('/', StaticFiles(directory="client/public/"), name="static")

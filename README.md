# fastapi-svelte

Simple Combination of FastAPI and Svelte.

## Setup Instructions:

1. Clone this Repo
2. ```pip install -r requirements.txt``` to install python dependencies.
3. Run ```npx degit sveltejs/template client``` inside root directory to create Svelte app inside ```client``` directory.

## Local Development:

**Build Svelte app and watch for changes:**```npm run autobuild``` (run inside client folder)

**Run Uvicorn server for FastAPI app with hotreloading:** ```uvicorn main:app --reload```

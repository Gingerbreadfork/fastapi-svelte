# fastapi-svelte

Simple Combination of FastAPI and Svelte.

## Setup Instructions:

1. Clone this Repo ```git clone https://github.com/Gingerbreadfork/fastapi-svelte```
3. ```pip install -r requirements.txt``` to install python dependencies (ideally in a virtualenv or similar - don't be a savage).
4. Run ```npm create vite@latest client -- --template svelte``` inside root directory to create Svelte app inside ```client``` directory.
5. Inside ```client``` directory run ```npm install```

## Local Development:

1. Build Svelte app if you haven't yet (and after any future changes) with ```npm run build``` inside client folder

2. In a second terminal run a Uvicorn server (ideally with hotreloading so it refreshes after new builds of the app are generated): ```uvicorn main:app --reload```

## Why?
You can build some pretty interesting/weird little apps using FastAPI to create a few endpoints while also serving a nice little frontend Svelte client at the same time.

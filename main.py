from fastapi import FastAPI
import logging
import os

app = FastAPI()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(level=LOG_LEVEL)

@app.get("/info")
def info():
    logging.info('This is an info message')
    return {"message": "Info"}

@app.get("/debug")
def debug():
    logging.debug('This is a debug message')
    return {"message": "Debug"}

@app.get("/error")
def error():
    logging.error('This is an error message')
    return {"message": "Error"}

@app.get("/fatal")
def fatal():
    logging.fatal('This is a fatal message')
    return {"message": "Fatal"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

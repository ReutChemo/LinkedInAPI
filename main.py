from fastapi import FastAPI

import api

app = FastAPI()
@app.get("/get-message")
async def read_root():
    return {"Message": "Congrats! This is your first API!"}

@app.get("/get-linkedin-response")
async def read_linkedin():
    return {api.get_linkedin_response()}
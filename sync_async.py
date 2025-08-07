from fastapi import FastAPI
import time, asyncio

app = FastAPI()

@app.get("/sync")
def sync_route():
    time.sleep(3) #blocks for 3 seconds
    return {"message": "Sync done"}

@app.get("/async")
async def async_route():
    await asyncio.sleep(3) #non blocking 3 seconds
    return {"message": "Async done"}
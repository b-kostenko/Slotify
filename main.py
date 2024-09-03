import asyncio
import datetime

import uvicorn
from fastapi import FastAPI


app = FastAPI(title="Slotify")



@app.get("/health-check", tags=["Health"])
def health_check():
    return {
        "status": "ok",
        "date": datetime.date.today(),
    }

async def start_server():
    config = uvicorn.Config(app, host="0.0.0.0", port=8080)
    server = uvicorn.Server(config)
    await server.serve()


async def main() -> None:
    await asyncio.gather(
        start_server(),
    )

if __name__ == '__main__':
    asyncio.run(main())
from fastapi import FastAPI


app = FastAPI(
    title="IG Worker",
)


@app.get("/health")
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "ig-worker",
    }

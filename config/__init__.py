import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.framework.routers import root

app = FastAPI(
    title="Fastapi base template for Python API projects",
    description="Base template project to expand your ideas without need to build the project from scratch.",
    version="v1",
    docs_url="/docs"
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(
    root.router
)



def start():
    uvicorn.run(
        "config:app",
        host="0.0.0.0",
        port=5003,
        reload=True,
        log_level="info"
    )

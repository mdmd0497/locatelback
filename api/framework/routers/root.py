from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


@router.get("/", tags=["Root"])
async def root():
    return JSONResponse(
        content={
            "title": "Fastapi base template for API projects",
            "author": "Oscar Cely",
            "contact": "oscarcej@gmail.com",
            "version": "v1",
            "docs": "/docs",
        }
    )


@router.get("/health", tags=["Health"])
async def health():
    return JSONResponse(
        content={
            "status": "ok",
            "status_code": 200,
        }
    )

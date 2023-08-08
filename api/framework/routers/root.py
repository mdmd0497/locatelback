from fastapi import APIRouter
from starlette.responses import JSONResponse
from api.src.handlers import AccountsHandler
from api.framework.serializers import CreateAccountSerializer,UpdateValueAccountSerializer,ConsultAccountSerializer

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

@router.post("/account", tags=["Account"])
async def create_account(account:CreateAccountSerializer):
    try:
        response = AccountsHandler.create_account(
            name=account.name,
            value=account.value
        )
        return JSONResponse(
            content=response,
            status_code=response["status"]
        )
    except Exception as e:
        return JSONResponse(
            content={
                "status": 500,
                "message": "Internal Server Error"
            }, status_code=500
        )
    
@router.patch("/updatevalue", tags=["Account"])
async def update_account(account:UpdateValueAccountSerializer):
    try:
        response = AccountsHandler.update_value_account(
            account = account.account,
            value = account.value
        )
        return JSONResponse(
            content=response,
            status_code=response["status"]
        )
    except Exception as e:
        return JSONResponse(
            content={
                "status": 500,
                "message": "Internal Server Error"
            }, status_code=500
        )

@router.get("/consultaccount/{account}", tags=["Account"])
async def consult_account(account: int):
    try:
        response = AccountsHandler.consult_account(
            account = account,
        )
        return JSONResponse(
            content=response,
            status_code=response["status"]
        )
    except Exception as e:
        return JSONResponse(
            content={
                "status": 500,
                "message": "Internal Server Error"
            }, status_code=500
        )
    

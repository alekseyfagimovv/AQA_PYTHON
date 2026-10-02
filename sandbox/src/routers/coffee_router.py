from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(tags=["Coffee"])

@router.get('/coffee/{size}')
async def get_coffee(size):
    if size == 'small':
        return {"size": size, "price": 2.5}
    elif size == 'medium':
         return {"size": size, "price": 3.5}
    else:
        return JSONResponse(status_code=400, content={"error": "unknown size"})

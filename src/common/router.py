from fastapi import APIRouter, Depends

from common.db.dependencies import get_db

router = APIRouter()


@router.get("/health")
def health(db=Depends(get_db)):
    return {"status": "ok"}

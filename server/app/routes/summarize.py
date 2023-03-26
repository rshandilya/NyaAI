from fastapi import APIRouter, HTTPException
from app.utils.apicalls import judgement_list, judgement_detail

router = APIRouter(
    prefix="/summary"
)

@router.get("/judgements/list/{keyword}")
def get_judgement_list(keyword:str):
    data = judgement_list(keyword)
    if not data:
        raise HTTPException(status_code=404, detail="Item not downloaded")
    return data


@router.get("/judgements/{tid}/detail")
def get_judgement_list(tid:int):
    data = judgement_detail(tid)
    if not data:
        raise HTTPException(status_code=404, detail="Item not downloaded")
    return data



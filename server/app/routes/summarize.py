from fastapi import APIRouter, HTTPException, Form
from app.utils.apicalls import judgement_list, judgement_detail
from app.utils.summarizer import summarizer
from typing import Annotated
from app.schemas.summary import JudgementText

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

@router.post("/judgement/summary", response_model=None)
def judgement_summary(
    content: Annotated[str, Form()]
):
    result = summarizer(content)
    if not result:
        raise HTTPException(status_code=404, detail="Error in Sumarizing")
    return {"summary": result}




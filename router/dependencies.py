from fastapi import APIRouter, Request

router = APIRouter(
    preffix='dependencies',
    tags=['dependencies']
)

def convert_headers(request: Request):
    pass
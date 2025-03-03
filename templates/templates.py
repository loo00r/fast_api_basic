from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.background import BackgroundTasks
from fastapi import Request
from schemas import ProductBase
from custom_logger import log


router = APIRouter(
    prefix="/templates",
    tags=["templates"],
)

templates = Jinja2Templates(directory="templates")

@router.post(f"/products/{id}", response_class=HTMLResponse)
def get_product(id: str, product: ProductBase, request: Request, bt: BackgroundTasks):
    bt.add_task(log_template_call, f"Template read for product with id {id}")
    return templates.TemplateResponse(
        "product.html",
        {
            "request": request,
            "id": id,
            "title": product.title,
            "description": product.description,
            "price": product.price,
        }
    )

def log_template_call(message: str):
    log("MyAPI", message)
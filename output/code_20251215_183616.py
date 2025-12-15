# app/main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Coffee Order Service")

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def show_order_form(request: Request):
    try:
        logger.info("Order form accessed")
        return templates.TemplateResponse("order_form.html", {"request": request})
    except Exception as e:
        logger.exception("Error displaying order form")
        return HTMLResponse(content=f"Error: {e}", status_code=500)


@app.post("/order", response_class=HTMLResponse)
async def submit_order(request: Request, coffee: str = Form(...), size: str = Form(...)):
    try:
        logger.info(f"Order received: coffee={coffee}, size={size}")
        return templates.TemplateResponse(
            "order_result.html",
            {"request": request, "coffee": coffee, "size": size},
        )
    except Exception as e:
        logger.exception("Error submitting order")
        return HTMLResponse(content=f"Error: {e}", status_code=500)
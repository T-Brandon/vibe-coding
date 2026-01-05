from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="FastAPI + Jinja2 Template Example")

# 템플릿 디렉토리 설정
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    루트 경로에 접근 시 index.html 템플릿을 렌더링합니다.
    """
    try:
        logger.info("Root page requested")
        return templates.TemplateResponse("index.html", {"request": request, "message": "Hello from FastAPI with Jinja2!"})
    except Exception as e:
        logger.error(f"Error rendering root page: {e}")
        raise e

@app.get("/hello/{name}", response_class=HTMLResponse)
async def hello_name(request: Request, name: str):
    """
    경로 파라미터 name을 받아 인사 메시지를 표시합니다.
    """
    try:
        logger.info(f"Hello page requested for name: {name}")
        return templates.TemplateResponse("hello.html", {"request": request, "name": name})
    except Exception as e:
        logger.error(f"Error rendering hello page for {name}: {e}")
        raise e
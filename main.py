from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/validate", response_class=HTMLResponse)
async def validate_bank(
    request: Request,
    bank_name: str = Form(...),
    ifsc: str = Form(...),
    account_number: str = Form(...)
):
    # Basic input check
    if len(account_number) < 6 or len(ifsc) < 6:
        result = {"status": "failed", "message": "Invalid IFSC or account number"}
    else:
        # Mock success response (you can replace this with real API later)
        name_list = ["RAHUL KUMAR", "PRIYA SHARMA", "AMAN VERMA", "NEHA SINGH"]
        result = {
            "status": "success",
            "bank_name": bank_name.title(),
            "account_holder_name": random.choice(name_list),
            "ifsc": ifsc.upper(),
            "account_number": account_number,
            "verified": True,
            "message": "Account holder name verified successfully."
        }

    return templates.TemplateResponse("index.html", {"request": request, "result": result})

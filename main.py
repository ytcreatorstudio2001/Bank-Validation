from fastapi import FastAPI, Form, UploadFile, File
from fastapi.responses import HTMLResponse

app = FastAPI()

# Home page with form
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h2>Upload Form</h2>
    <form action="/validate" method="post" enctype="multipart/form-data">
        Name: <input type="text" name="name" required><br><br>
        File: <input type="file" name="file"><br><br>
        <input type="submit" value="Submit">
    </form>
    """

# Endpoint to handle form submission
@app.post("/validate", response_class=HTMLResponse)
async def validate(
    name: str = Form(...), 
    file: UploadFile | None = File(None)
):
    if file:
        content = await file.read()
        file_info = f"Uploaded file: {file.filename} ({len(content)} bytes)"
    else:
        file_info = "No file uploaded"
    
    return f"""
    <h2>Hello {name}!</h2>
    <p>{file_info}</p>
    """

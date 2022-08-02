import uvicorn
from fastapi import File, UploadFile, FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from window_seat.image_decoder import extract_created_from_filepath, extract_created_from_bytes

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        # file_location = f"/tmp/window-seat/{file.filename}"
        # with open(file_location, 'wb') as f:
        #     f.write(contents)
        # image_metadata = extract_created_from_filepath(file_location)

        image_metadata = extract_created_from_bytes(contents)
        print(f"Image created at {image_metadata}")

    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        await file.close()

    return {"message": f"Successfuly uploaded {file.filename}"}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

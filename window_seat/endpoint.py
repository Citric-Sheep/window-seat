import uvicorn
from fastapi import File, UploadFile, FastAPI

from window_seat.image_decoder import decode_image

app = FastAPI()


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image_metadata = decode_image(contents)
        print("herer")

        # with open(f"/tmp/window-seat/{file.filename}", 'wb') as f:
        #     f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        await file.close()

    return {"message": f"Successfuly uploaded {file.filename}"}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

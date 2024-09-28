from fastapi import FastAPI, HTTPException
from yt_dlp import YoutubeDL
from fastapi.responses import StreamingResponse, HTMLResponse
import os
import glob

app = FastAPI()

@app.get("/", include_in_schema=False, response_class=HTMLResponse)
async def root():
    return HTMLResponse("This is YouTube Video Downloader API<br>go to <a href='/docs'>/docs</a> to see docs")

@app.get("/api/v1/download")
async def download_video(url: str):
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': f'%(title)s.%(ext)s',
        'noplaylist': True,
    }
    mp4 = glob.glob("*.mp4")[0]
    print(mp4)
    os.remove(mp4)
    try:
        os.remove(glob.glob("*.part")[0])
    except:
        pass

    with YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(url, download=True)
            file_name = ydl.prepare_filename(info_dict)

            return {"title": info_dict['title'], "url": "http://127.0.0.1:8000/api/oiewihfondsfjqhrfiohdvncojiuqtrewqawsedxcfrtgyhuwejfkmdfpvghoykwulpth0o9685u347swhiue5ry7r3hf0okmrtgnj8u543wedhbwje3g2t5frde67ts8fyt5hu4tt389wofsj"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/oiewihfondsfjqhrfiohdvncojiuqtrewqawsedxcfrtgyhuwejfkmdfpvghoykwulpth0o9685u347swhiue5ry7r3hf0okmrtgnj8u543wedhbwje3g2t5frde67ts8fyt5hu4tt389wofsj")
async def get_video():
    def iterate_file():
        with open(glob.glob("*.mp4")[0], 'rb') as f:
            yield from f

    return StreamingResponse(iterate_file(), media_type="video/mp4")

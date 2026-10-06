from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

# 1.ساختن یک اپلیکیشن (نمونه ای از FastAPI)
app = FastAPI()

# به مرورگر اجازه می دهیم از هر مبدایی با بکند حرف بزند: تنظیمات CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   #یعنی همه فرانت اندها مجاز هستند 
    allow_credentials=True,
    allow_methods=["*"],  #مجاز بودن متدهای GET, POST و غیره
    allow_headers=["*"],
)

#پوشه ای برای ذخیره موقت فایل های صوتی دریافتی
UPLOAD_DIR = "uploaded_audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# 2. تعریف کردن یک مسیر (Route)
# وقتی کسی به آدرس اصلی ("/") سر بزند، این تابع اجرا میشود
@app.get("/")
def home():
    return {"message": "سرور فعال است!"}

@app.get("/search")
def search(query: str):
    return {"message": f"بک اند موضوع {query} را با موفقیت دریافت کرد!"}
   

# روت جدید: دریافت ویس از فرانت اند
@app.post("/upload-audio")
async def upload_audio(audio_file: UploadFile = File(...)):
    # مسیر ذخیره فایل
    file_path = os.path.join(UPLOAD_DIR, audio_file.filename)

    #ذخیره فایل ضبط شده روی دیسک
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(audio_file.file, buffer)

    #حجم فایل را برای گزارش به کار حساب می کنیم
    file_size_kb = os.path.getsize




    print(f"درخواست جستوجو برای موضوع: {query}")
    return {
        "status": "succss",
        "message": f"بک اند موضوع {query} را با موفقیت دریافت کرد!"
    }
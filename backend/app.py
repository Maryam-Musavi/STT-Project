from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import time
import whisper

# 1.ساختن یک اپلیکیشن (نمونه ای از FastAPI)
app = FastAPI(title="Speach to Text API")

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

# بارگذاری مدل Whisper یک‌بار هنگام استارت سرور
print("در حال بارگذاری مدل هوش مصنوعی Whisper...")
model = whisper.load_model("base")
print("مدل Whisper آماده استفاده است!")

# 2. تعریف کردن یک مسیر (Route)
# وقتی کسی به آدرس اصلی ("/") سر بزند، این تابع اجرا میشود
@app.get("/")
def home():
    return {"message": "سرور فعال است!"}

# روت جدید: دریافت ویس از فرانت اند
@app.post("/upload-audio")
async def upload_audio(audio_file: UploadFile = File(...)):
    # مسیر ذخیره فایل
    file_path = os.path.join(UPLOAD_DIR, audio_file.filename)

    #ذخیره فایل ضبط شده روی دیسک
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(audio_file.file, buffer)

    #حجم فایل را برای گزارش به کار حساب می کنیم
    file_size_kb = os.path.getsize(file_path) / 1024
    print(f"فایل صوتی با موفقیت ذخیره شد {audio_file.filename}")

    start_time = time.time()
    result = model.transcribe(file_path)
    elapsed_time = time.time() - start_time


    
    return {
        "status": "success",
        "filename": audio_file.filename,
        "size_kb": round(file_size_kb, 2),
        "text": result["text"].strip(),
        "detected_language": result.get("language", "unknown"),
        "processing_time_sec": round(elapsed_time, 2)
    }


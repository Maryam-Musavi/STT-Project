from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


# 2. تعریف کردن یک مسیر (Route)
# وقتی کسی به آدرس اصلی ("/") سر بزند، این تابع اجرا میشود
@app.get("/")
def read_root():
    return {"message": "Backend is working!"}
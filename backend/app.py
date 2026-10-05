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

@app.get("/search")
def search_youtube(query: str):
    """
    موضوع جستوجو را از فدانت  میگیرد و فعلا 
    تاییدیه را بر می گرداند.
    در مراحل بعد، وب اسکرپینگ یوتیوب را
    اینجا وصل میکنیم
    """
    print(f"درخواست جستوجو برای موضوع: {query}")
    return {
        "status": "succss",
        "message": f"بک اند موضوع {query} را با موفقیت دریافت کرد!"
    }
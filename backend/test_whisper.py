# backend/test_whisper.py
import whisper
import time

print("1. در حال بارگذاری مدل هوش مصنوعی Whisper")
start_time = time.time()

# لود کردن مدل: مدل base سبک، دقیق و سریع است
# Whisper خودش به صورت خودکار از کارت گرافیک (CUDA) استفاده می‌کند
model = whisper.load_model("base")

load_time = time.time() - start_time
print(f"مدل با موفقیت در {load_time:.2f} ثانیه روی حافظه لود شد.")

# مسیر فایل صوتی برای تست
audio_path = "uploaded_audio/temp.mp3"

print("2. در حال تبدیل گفتار به متن (Transcribing)...")
process_start = time.time()

# اجرای تبدیل صوت به متن
result = model.transcribe(audio_path)

process_time = time.time() - process_start

print(f"پردازش در {process_time:.2f} ثانیه به پایان رسید.\n")

print("=" * 40)
print("متن تشخیص داده شده:")
print(result["text"])
print("=" * 40)
print(f"زبان تشخیص داده شده: {result.get('language')}")
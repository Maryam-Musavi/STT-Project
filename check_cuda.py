import torch

print("=" * 45)
print("بررسی وضعیت پردازش کارت گرافیک (CUDA):")
print("=" * 45)

print(f"نسخه PyTorch: {torch.__version__}")

is_cuda_ready = torch.cuda.is_available()
print(f"آیا CUDA فعال و در دسترس است؟ {is_cuda_ready}")

if is_cuda_ready:
    gpu_name = torch.cuda.get_device_name(0)
    gpu_count = torch.cuda.device_count()
    print(f"مدل کارت گرافیک: {gpu_name}")
    print(f"تعداد GPU: {gpu_count}")
    print("نتیجه: عالی! هوش مصنوعی با حداکثر سرعت روی کارت گرافیک اجرا می‌شود.")
else:
    print("نتیجه: کارت گرافیک پیدا نشد؛ پردازش روی CPU انجام خواهد شد.")

print("=" * 45)

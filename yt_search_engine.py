import yt_dlp

def format_duration(seconds: int | float | None) -> str:
    """
    ثانیه را می‌گیرد و به فرمت دقیقه:ثانیه یا ساعت:دقیقه:ثانیه تبدیل می‌کند.
    مثال: 125 ثانیه -> '02:05'
    """
    if not seconds:
        return "نامشخص"
    
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{remaining_seconds:02d}"
    else:
        return f"{minutes:02d}:{remaining_seconds:02d}"

def search_youtube(query: str, max_results: int = 3) -> list:
    """
    موتور جستجو: عبارت کاربر را می‌گیرد و اطلاعات ویدیوها را برمی‌گرداند.
    """
    ydl_opts = {
        'extract_flat': True,  # فقط اطلاعات متنی، بدون دانلود ویدیو
        'quiet': True,         # لاگ‌های اضافی را خاموش کن
    }

    search_query = f"ytsearch{max_results}:{query}"
    videos = []

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(search_query, download=False)
        
        if 'entries' in result:
            for entry in result['entries']:
                if entry:
                    videos.append({
                        'title': entry.get('title'),
                        'url': f"https://www.youtube.com/watch?v={entry.get('id')}"
                    })

    return videos

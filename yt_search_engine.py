import yt_dlp

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

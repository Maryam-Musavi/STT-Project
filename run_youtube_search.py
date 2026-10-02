from yt_search_engine import search_youtube

def main():
    print("=" * 45)
    print("🔍 سامانه جستجوی آموزش‌های یوتیوب (نسخه ۲)")
    print("=" * 45)

    topic = input("\nچه مبحث آموزشی را سرچ می کنی؟")
    print(f"\nدر حال جستوجوی '{topic}' در یوتیوب ... لطفا شکیبا باشید.\n")

    results = search_youtube(query=topic, max_results=3)

    if not results:
        print("موردی بافت نشد.")
        return
    
    for idx, item in enumerate(results, start=1):
        print(f"[{idx}] {item['title']}")
        print(f"   ⏱️ مدت زمان: {item['duration']}")
        print(f"   🔗 لینک: {item['url']}")
        print("-" * 45)


if __name__ == "__main__":
    main()



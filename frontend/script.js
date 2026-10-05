// 1. انتخاب المانها از طریق id
const searchInput = document.getElementById("search-input");
const searchBtn = document.getElementById("search-btn");
const resultText = document.getElementById("result");

// 2. اضافه کردن رویداد کلیک به دکمه
searchBtn.addEventListener("click", async () => {
    // خواندن متنی که کاربر تایپ کرده
    const query = searchInput.value.trim();

    // اگر کاربر چیزی تایپ نکرده بود بهش هشدار بده
    if (!query) {
        resultText.innerText = "لطفا ابندا یک موضوع برای جستوجو بنویسید!";

        return;
    }

    resultText.innerText = " در حال ارسال درخواست بک اند...!";

    try {
        // 3. ارسال درخواست به مسیر جدید همراه با پارامتر جستوجو
        const response = await fetch(`http://127.0.0.1:8000/search?query=${encodeURIComponent(query)}`);

        // 4. تبدیل جواب به فرمت JSON
        const data = await response.json();

        // 5. نمایش پیام سرور در صفحه
        resultText.innerText = data.message;

    } catch (error) {
        // اگر سرور خاموش باشد یا مشکلی پیش بیاید
        resultText.innerText = "خطا در اتصال به سرور!";
        console.error("Error:", error);
    }
});


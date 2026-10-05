// 1. انتخاب المانهای دکمه و متن نتیجه
const testBtn = document.getElementById("test-btn");
const resultText = document.getElementById("result");

// 2. اضافه کردن رویداد کلیک به دکمه
testBtn.addEventListener("click", async () => {
    resultText.innerText = "در حال برقراری ارتباط ..."

    try {
        // 3. ارسال درخواست به بک اند پایتون
        const response = await fetch("http://127.0.0.1:8000/")
        console.log("2. پاسخ خام سرور دریافت شد", response.status);

        // 4. تبدیل جواب به فرمت JSON
        const data = await response.json();
        console.log("3. داده تبدیل شد به json:, data");

        // 5. نمایش پیام دریافتی روی صفحه
        resultText.innerText = "پاسخ از بک اند: " + data.message;
    } catch (error) {
        // اگر سرور خاموش باشد یا مشکلی پیش بیاید
        resultText.innerText = "خطا در اتصال به سرور!";
        console.error("Error:", error);
    }
});


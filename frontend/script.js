// 1. انتخاب المانها از طریق id
const searchInput = document.getElementById("search-input");
const searchBtn = document.getElementById("search-btn");
const recordBtn = document.getElementById("record-btn");
const stopBtn = document.getElementById("stop-btn");
const resultText = document.getElementById("result");


//متغیرهای مورد نیاز برای ضبط صدا
let mediaRecorder;
let audioChunks = [];

// ==========================================
// بخش جستجوی متنی (از مرحله قبل)
// ==========================================

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

// ==========================================
// بخش جدید: ضبط صدا و ارسال به بک‌اند
// ==========================================

// دکمه شروع صبط
recordBtn.addEventListener("click", async () => {
    try {
        // 1. درخواست دسترسی به میکروفون کاربر
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true});

        mediaRecorder = new MediaRecorder(stream);
        audioChunks = []; //خالی کردن حافظه قبلی

        // 2. جمع آوری داده های صوتی وقتی ضبط در جریان است
        mediaRecorder.ondataavailable = (event) => {
            audioChunks.push(event.data);
        };

        // 3. کاری که پس از توقف صبط باید انجام شود
        mediaRecorder.onstop = async () => {
            // از تکه های جمع آوری شده Blob ساخت یک فایل صوتی
            const audioBlob = new Blob(audioChunks, { type: "audio/webm" });

            //قرار دادن فایل صوتی داخل یک فرم استاندارد برای ارسال
            const formData = new FormData();
            formData.append("audio_file", audioBlob, "voice.webm");

            resultText.innerText = "در حال ارسال فایل صوتی به بک اند...";

            try {
                //ارسال درخواست POST حاوی فایل به بک اند
                const response = await fetch("http://127.0.0.1:8000/upload-audio", {
                    method: "POST",
                    body: formData
                });
                const data = await response.json();
                resultText.innerText = data.message;
            } catch (error) {
                resultText.innerText = "خطا در ارسال فایل صوتی به بک امد!";
                console.error("Error", error);
            }
        };
        // شروع فرآیند ضبط و تغییر وضعیت دکمه ها
        mediaRecorder.start();
        resultText.innerText = "در حال ضبط صدا ... صحبت کنید!";
        recordBtn.disabled = true;
        stopBtn.disabled = false;

    } catch (error) {
        resultText.innerText = "دسترسی به میکروفون داده نشده یا خطایی رخ داد!";
        console.error("Microphone error:", error);
    }
});

// دکمه توقف ضبط
stopBtn.addEventListener("click", () => {
    if (mediaRecorder && mediaRecorder.state !== "inactive") {
        mediaRecorder.stop();
        recordBtn.disabled = false;
        stopBtn.disabled = true;
    }
})
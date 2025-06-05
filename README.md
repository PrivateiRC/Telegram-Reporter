# **README.md - ابزار گزارشگر پیشرفته تلگرام (iRC Reporter)**  

**🇮🇷 نسخه فارسی | 🇬🇧 English Version Below**  

## **🔰 معرفی**  
اسکریپت **iRC Reporter** یک ابزار حرفه‌ای برای گزارش انبوه اکانت‌ها و کانال‌های متخلف در تلگرام است.  

**💻 ویژگی‌های اصلی:**  
- گزارش با 10 دلیل مختلف  
- تنظیم سرعت و مدت زمان گزارش  
- پشتیبانی از پروکسی  
- رابط کاربری ساده  

**📌 لینک‌های ارتباطی:**  
- کانال تلگرام: [@Iranian_Cybers](https://t.me/Iranian_Cybers)  
- پشتیبانی: [@PrivateiRC](https://t.me/PrivateiRC)  

---

## **🛠 نصب و راه‌اندازی**  
1. ابتدا مطمئن شوید پایتون 3 نصب شده است:  
   ```bash
   python --version
   ```
2. کتابخانه‌های مورد نیاز را نصب کنید:  
   ```bash
   pip install telethon requests
   ```
3. اسکریپت را اجرا کنید:  
   ```bash
   python3 irc_reporter.py
   ```

---

## **📝 راهنمای استفاده**  
پس از اجرا، اسکریپت از شما اطلاعات API تلگرام را می‌پرسد. این اطلاعات را از [my.telegram.org](https://my.telegram.org) دریافت کنید.  

**دستورات اصلی:**  
- `report @username reason duration speed`  
  مثال:  
  ```bash
  report @spammer 3 60 1
  ```
  - `3`: دلیل گزارش (مثلاً محتوای مستهجن)  
  - `60`: مدت زمان گزارش (ثانیه)  
  - `1`: تعداد گزارش در ثانیه  

- `help`: نمایش راهنما  
- `exit`: خروج از برنامه  

---

## **⚠️ هشدار**  
- استفاده نادرست ممکن است منجر به محدود شدن اکانت شما شود.  
- این ابزار فقط برای مقاصد آموزشی ارائه شده است.  

---

# **🇬🇧 iRC Reporter - Advanced Telegram Reporting Tool**  

## **🔰 Introduction**  
**iRC Reporter** is a professional tool for mass reporting Telegram accounts and channels.  

**💻 Main Features:**  
- 10 different report reasons  
- Adjustable speed and duration  
- Proxy support  
- Simple UI  

**📌 Contact:**  
- Telegram Channel: [@Iranian_Cybers](https://t.me/Iranian_Cybers)  
- Support: [@PrivateiRC](https://t.me/PrivateiRC)  

---

## **🛠 Installation**  
1. Ensure Python 3 is installed:  
   ```bash
   python --version
   ```
2. Install requirements:  
   ```bash
   pip install telethon requests
   ```
3. Run the script:  
   ```bash
   python3 irc_reporter.py
   ```

---

## **📝 Usage Guide**  
After running, the script will ask for your Telegram API details (get from [my.telegram.org](https://my.telegram.org)).  

**Main Commands:**  
- `report @username reason duration speed`  
  Example:  
  ```bash
  report @spammer 3 60 1
  ```
  - `3`: Report reason (e.g. pornography)  
  - `60`: Duration (seconds)  
  - `1`: Reports per second  

- `help`: Show help  
- `exit`: Quit  

---

## **⚠️ Warning**  
- Misuse may get your account limited.  
- This tool is for educational purposes only.  

--- 

**✅ توسعه داده شده توسط تیم ایرانیان سایبر | Developed by Iranian Cyber Team**  


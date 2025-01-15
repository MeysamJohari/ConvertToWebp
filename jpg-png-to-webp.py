import os
from PIL import Image

# مسیر پوشه عکس‌ها
input_folder = r"مسیر پوشه عکسهای تبدیل نشده"
output_folder = r"مسیر پوشه عکسها بعد از تبدیل"

# ایجاد پوشه خروجی اگر وجود نداشت
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# تبدیل تصاویر به فرمت webp
for filename in os.listdir(input_folder):
    # بررسی فرمت فایل‌ها
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        file_path = os.path.join(input_folder, filename)
        output_path = os.path.join(
            output_folder, os.path.splitext(filename)[0] + ".webp")
        try:
            with Image.open(file_path) as img:
                img.save(output_path, format="WEBP")
                print(f"تصویر {filename} با موفقیت تبدیل شد.")
        except Exception as e:
            print(f"خطا در تبدیل تصویر {filename}: {e}")

print("تبدیل تصاویر به پایان رسید.")

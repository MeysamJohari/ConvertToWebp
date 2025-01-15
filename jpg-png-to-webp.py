import os
from PIL import Image

# مسیر پوشه عکس‌ها
input_folder = r"مسیر پوشه عکسهای تبدیل نشده"
output_folder = r"مسیر پوشه عکسها بعد از تبدیل"

# ایجاد پوشه خروجی اگر وجود نداشت
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# حداکثر عرض تصویر
max_width = 1200
target_min_size = 40 * 1024  # حداقل حجم فایل (بر حسب بایت)
target_max_size = 60 * 1024  # حداکثر حجم فایل (بر حسب بایت)

# تبدیل تصاویر به فرمت webp
for filename in os.listdir(input_folder):
    # بررسی فرمت فایل‌ها
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        file_path = os.path.join(input_folder, filename)
        output_path = os.path.join(
            output_folder, os.path.splitext(filename)[0] + ".webp")
        try:
            with Image.open(file_path) as img:
                # بررسی عرض تصویر
                if img.width > max_width:
                    # محاسبه نسبت و تغییر اندازه
                    ratio = max_width / float(img.width)
                    new_height = int(img.height * ratio)
                    img = img.resize((max_width, new_height),
                                     Image.Resampling.LANCZOS)

                # تنظیم کیفیت برای رسیدن به حجم مناسب
                quality = 85  # شروع کیفیت
                for q in range(85, 30, -5):  # کاهش کیفیت تا یافتن محدوده مناسب
                    temp_path = output_path + "_temp.webp"
                    img.save(temp_path, format="WEBP", quality=q)
                    file_size = os.path.getsize(temp_path)
                    if target_min_size <= file_size <= target_max_size:
                        # تغییر نام فایل به فایل خروجی اصلی
                        os.rename(temp_path, output_path)
                        print(
                            f"تصویر {filename} با کیفیت {q} و حجم {file_size // 1024} کیلوبایت ذخیره شد.")
                        break
                    os.remove(temp_path)
                else:
                    print(f"تصویر {filename} حجم مناسب پیدا نکرد.")
        except Exception as e:
            print(f"خطا در تبدیل تصویر {filename}: {e}")

print("تبدیل تصاویر به پایان رسید.")

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import pytz
import time
import re

# ---------------------- 1. AGE CALCULATOR ----------------------
print("\n--- Age Calculator ---")
birth_str = input("Tug'ilgan kuningizni kiriting (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_str, "%Y-%m-%d")
today = datetime.today()
diff = relativedelta(today, birth_date)
print(f"Siz {diff.years} yil, {diff.months} oy, {diff.days} kundan beri yashayapsiz.")

# ---------------------- 2. DAYS UNTIL NEXT BIRTHDAY ----------------------
print("\n--- Days Until Next Birthday ---")
birth_str = input("Tug'ilgan kuningizni qayta kiriting (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_str, "%Y-%m-%d")
today = datetime.today()
next_birthday = birth_date.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)
days_left = (next_birthday - today).days
print(f"Keyingi tug'ilgan kuningizgacha {days_left} kun qoldi.")

# ---------------------- 3. MEETING SCHEDULER ----------------------
print("\n--- Meeting Scheduler ---")
current_str = input("Hozirgi vaqtni kiriting (YYYY-MM-DD HH:MM): ")
hours = int(input("Uchrashuv davomiyligi (soat): "))
current_time = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
end_time = current_time + timedelta(hours=hours)
print("Uchrashuv tugaydigan vaqt:", end_time.strftime("%Y-%m-%d %H:%M"))

# ---------------------- 4. TIMEZONE CONVERTER ----------------------
print("\n--- Timezone Converter ---")
time_str = input("Vaqtni kiriting (YYYY-MM-DD HH:MM): ")
from_zone = input("Hozirgi timezone (masalan: Asia/Tashkent): ")
to_zone = input("Qaysi timezone ga o'tkazilsin (masalan: Europe/London): ")
try:
    from_tz = pytz.timezone(from_zone)
    to_tz = pytz.timezone(to_zone)
    local_time = from_tz.localize(datetime.strptime(time_str, "%Y-%m-%d %H:%M"))
    converted = local_time.astimezone(to_tz)
    print("O'zgartirilgan vaqt:", converted.strftime("%Y-%m-%d %H:%M (%Z)"))
except Exception as e:
    print("Xatolik:", e)



# ---------------------- 6. EMAIL VALIDATOR ----------------------
print("\n--- Email Validator ---")
email = input("Email manzilini kiriting: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
if re.match(pattern, email):
    print("Email manzili to'g'ri.")
else:
    print("Email manzili noto'g'ri.")

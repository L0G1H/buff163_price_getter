import os
import time
from buff163_price_getter import Buff163_Price_Getter


cookie = os.getenv("buff163_cookie")
getter = Buff163_Price_Getter(cookie=cookie, currency="EUR")

a = time.time()

print(getter.get_item("AK-47 | Redline (Minimal Wear)"))

b = time.time()

print(b - a)

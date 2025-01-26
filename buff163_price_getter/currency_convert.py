from __future__ import annotations
import requests
from bs4 import BeautifulSoup
import re


def get_rate(base_currency: str, target_currency: str) -> float | None:
    base_currency = base_currency.lower()
    target_currency = target_currency.lower()

    if base_currency == target_currency:
        return 1.0

    url = f"https://www.forbes.com/advisor/money-transfer/currency-converter/{base_currency}-{target_currency}/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        exchange_rate_text = soup.find("h2").text
        exchange_rate_match = re.search(r"(\d+\.\d+)", exchange_rate_text)

        if exchange_rate_match:
            return float(exchange_rate_match.group(1))

    except Exception as _:
        return None


if __name__ == "__main__":
    a = get_rate("EUR", "RUB")
    print(a)


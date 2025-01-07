import time
import aiohttp
import asyncio
import currency_convert
import os
import requests


OK_STATUS = 200


class Buff163PriceGetter:
    def __init__(self, cookie: str, currency: str) -> None:
        self.url = "https://buff.163.com/api/market/goods/sell_order"
        self.params = {
            "game": "csgo",
            "page_num": 1,
            "sort_by": "default",
            "allow_tradable_cooldown": 1,
        }
        self.headers = {"Cookie": cookie}
        self.currency_rate = currency_convert.get_exchange_rate("CNY", currency)
        cs2_marketplace_ids_url = (
            "https://raw.githubusercontent.com/ModestSerhat/"
            "cs2-marketplace-ids/refs/heads/main/cs2_marketplaceids.json"
        )
        response = requests.get(cs2_marketplace_ids_url)
        response.raise_for_status()
        data = response.json()
        self.buff_id_lookup = {}
        for item_name, item_info in data.get("items", {}).items():
            self.buff_id_lookup[item_name] = item_info.get("buff163_goods_id")

    async def get_item(self, item_name: str) -> dict:
        item_id = self.buff_id_lookup.get(item_name)
        assert item_id

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                    self.url,
                    params={"goods_id": item_id, **self.params},
                    headers=self.headers,
                    timeout=aiohttp.ClientTimeout(total=30),
                ) as response:
                    if response.status != OK_STATUS:
                        raise aiohttp.ClientResponseError(
                            response.request_info,
                            response.history,
                            status=response.status,
                        )
                    response_data = await response.json()
            except aiohttp.ClientError as e:
                print(f"Error fetching item {item_name}: {e}")
                return None

        item_data = response_data["data"]["goods_infos"][str(item_id)]
        buff_price = round(
            float(item_data.get("sell_min_price")) * self.currency_rate, 2
        )
        steam_price = round(
            float(item_data.get("steam_price_cny")) * self.currency_rate, 2
        )
        return {"buff_price": buff_price, "steam_price": steam_price}


async def main() -> None:
    getter = Buff163PriceGetter(os.getenv("BUFF163_COOKIE"), "EUR")
    start = time.time()

    results = await asyncio.gather(
        getter.get_item("AK-47 | Redline (Minimal Wear)"),
        getter.get_item("AK-47 | Redline (Field-Tested)"),
        getter.get_item("AK-47 | Redline (Well-Worn)"),
        getter.get_item("AK-47 | Redline (Battle-Scarred)"),
    )

    end = time.time()

    for result in results:
        if result:
            print(result)

    print(f"Total time: {end - start}")


if __name__ == "__main__":
    asyncio.run(main())


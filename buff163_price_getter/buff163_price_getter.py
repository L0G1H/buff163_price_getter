import aiohttp
import requests
from . import currency_convert


OK_STATUS = 200


class Buff163PriceGetter:
    def __init__(self, currency: str) -> None:
        self.url = "https://buff.163.com/api/market/goods/sell_order"
        self.params = {
            "game": "csgo",
            "page_num": 1,
            "sort_by": "default",
            "allow_tradable_cooldown": 1,
        }

        self.currency_rate = currency_convert.get_rate("CNY", currency)
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

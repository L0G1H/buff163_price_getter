import requests
import currency_convert


class Buff163_Price_Getter:
    def __init__(self, cookie: str, currency: str):
        self.url = "https://buff.163.com/api/market/goods/sell_order"

        self.params = {
            "game": "csgo",
            "page_num": 1,
            "sort_by": "default",
            "allow_tradable_cooldown": 1,
        }

        self.headers = {
            "Cookie": cookie
        }

        self.currency_rate = currency_convert.get_safe_rate(base_curr="CNY", target_curr=currency)

        response = requests.get("https://raw.githubusercontent.com/ModestSerhat/cs2-marketplace-ids/refs/heads/main/cs2_marketplaceids.json")
        response.raise_for_status()

        self.buff_id_lookup = {}

        for item_name, item_info in response.json().get("items", {}).items():
            self.buff_id_lookup[item_name] = item_info.get("buff163_goods_id")



    def get_item(self, item_name) -> dict:
        item_id = self.buff_id_lookup.get(item_name)

        if item_id is None:
            raise Exception("Item ID not find")

        response = requests.get(self.url, params={"goods_id": item_id, **self.params}, headers=self.headers)
        response.raise_for_status()

        response = response.json()

        item_data = response["data"]["goods_infos"][str(item_id)]

        buff_price = round(float(item_data.get("sell_min_price")) * self.currency_rate, 2)
        steam_price = round(float(item_data.get("steam_price_cny")) * self.currency_rate, 2)

        return {"buff_price": buff_price, "steam_price": steam_price}
import unittest
import asyncio
import os
from buff163_price_getter import Buff163_Price_Getter


class TestBuff163PriceGetter(unittest.TestCase):
    def setUp(self):
        self.cookie = os.getenv("BUFF163_COOKIE")
        self.getter = Buff163_Price_Getter(self.cookie, "EUR")

    async def async_test_get_item(self):
        result = await self.getter.get_item("AK-47 | Redline (Minimal Wear)")
        self.assertIsInstance(result, dict)
        self.assertIn('buff_price', result)
        self.assertIn('steam_price', result)
        self.assertIsInstance(result['buff_price'], float)
        self.assertIsInstance(result['steam_price'], float)

    def test_get_item(self):
        asyncio.run(self.async_test_get_item())

    def test_invalid_item(self):
        with self.assertRaises(Exception):
            asyncio.run(self.getter.get_item("Invalid Item Name"))


if __name__ == '__main__':
    unittest.main()
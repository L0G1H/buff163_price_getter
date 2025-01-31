from buff163_price_getter.buff163_price_getter import Buff163PriceGetter
import asyncio


async def main() -> None:
    import time
    getter = Buff163PriceGetter(currency="EUR")
    start = time.time()

    results = await asyncio.gather(
        getter.get_item("StatTrak™ AK-47 | Redline (Minimal Wear)"),
        getter.get_item("StatTrak™ AK-47 | Redline (Field-Tested)"),
        getter.get_item("StatTrak™ AK-47 | Redline (Well-Worn)"),
        getter.get_item("StatTrak™ AK-47 | Redline (Battle-Scarred)"),
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

# Buff163 Price Getter 

A Python module for retrieving CS2 item prices from Buff163 marketplace.

## Features

- Async support for efficient API calls
- Currency conversion
- Steam prices addition 

## Installation

```bash
pip install git+https://github.com/L0G1H/buff163_price_getter.git
``` 
## Usage

```python
import asyncio 
from buff163_price_getter import Buff163PriceGetter


async def main():
    # Initialize with your Buff163 cookie and desired currency 
    getter = Buff163PriceGetter(currency="EUR")
    
    # Get items prices
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

    for result in results:
        print(result) # {"buff_price": 123.45, "steam_price": 150.67} 


if __name__ == "__main__": 
    asyncio.run(main())
``` 
## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

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
import os
from buff163_price_getter import Buff163PriceGetter

async def main():
    # Initialize with your Buff163 cookie and desired currency 
    getter = Buff163PriceGetter(cookie=cookie, currency="EUR")
    
    # Get item prices
    result = await getter.get_item("AK-47 | Redline (Minimal Wear)") 
    print(result) # {"buff_price": 123.45, "steam_price": 150.67} 


if __name__ == "__main__": 
    asyncio.run(main())
``` 
## License

This project is licensed under the GNU General Public License v3.0.

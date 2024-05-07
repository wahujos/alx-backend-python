#!/usr/bin/env python3
"""
module documentation
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    for i in range(10):
        await asyncio.sleep(1)
        random_number = random.uniform(0, 10)
        yield random_number

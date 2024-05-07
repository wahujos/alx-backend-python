#!/usr/bin/env python3
"""
documenting the module listing imports
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Documenting the function
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(*tasks)

    delays.extend(result)
    # delays.sort()
    return delays

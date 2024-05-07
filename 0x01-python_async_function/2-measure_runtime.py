#!/usr/bin/env python3
"""
Documenting module listing import below
"""

import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    """Documenting the function measure time"""
    wait_n = __import__('1-concurrent_coroutines').wait_n
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return ((time.time() - start_time) / n)

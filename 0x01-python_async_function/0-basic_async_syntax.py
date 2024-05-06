#!/usr/bin/env python3
"""Module documentation goes here"""

import asyncio
import random


async def wait_random(max_delay=10):
    """documenting the function"""
    random_delay = random.random() * max_delay
    await asyncio.sleep(random_delay)
    return random_delay

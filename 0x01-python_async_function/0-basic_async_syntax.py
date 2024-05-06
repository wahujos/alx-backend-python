#!/usr/bin/env python3
"""
Module documentation goes here
all the import are shown below alphabetically
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    documenting the function
    """
    random_delay = random.random() * max_delay
    await asyncio.sleep(random_delay)
    return random_delay

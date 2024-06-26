#!/usr/bin/env python3
"""
documenting the module
"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Documenting the function
    """
    random_numbers = [i async for i in async_generator()]
    return random_numbers

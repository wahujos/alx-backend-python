#!/usr/bin/env python3
"""
documenting the module
"""
import asyncio
import random
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    Documenting the function
    """
    random_numbers = [i async for i in async_generator()]
    return random_numbers

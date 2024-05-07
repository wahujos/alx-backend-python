#!/usr/bin/env python3
"""
Module documentation
"""

import asyncio
import time


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Documenting the function"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    task = asyncio.create_task(wait_random(max_delay))
    return task

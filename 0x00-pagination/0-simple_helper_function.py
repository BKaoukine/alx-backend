#!/usr/bin/env python3
"""Function to get page start and end."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Index_page function calculate page start and end index.

    Args:
        page (int): page number
        page_size (int): page size

    Returns:
        Tuple: start and end index of the page.
    """
    start_index = page_size * (page-1)
    end_index = start_index + page_size

    return (start_index, end_index)

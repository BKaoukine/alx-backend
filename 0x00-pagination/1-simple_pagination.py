#!/usr/bin/env python3
"""Function to get page start and end."""

from typing import Tuple
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Constructore."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cache dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get_page func to get data requested in page."""
        assert isinstance(page and page_size, int)
        assert page and page_size > 0

        pages = index_range(page, page_size)
        data = self.dataset()

        return data[pages[0]:pages[1]]


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

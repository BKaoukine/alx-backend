#!/usr/bin/env python3
"""Function to get page start and end."""

from typing import Tuple, List, Dict
import csv
import math


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Construct the instance."""
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
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get pagination hypermedia."""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        pagination = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return pagination


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate start and end index for a given page and page size.

    Args:
        page (int): page number
        page_size (int): page size

    Returns:
        Tuple[int, int]: start and end index of the page.
    """
    start_index = page_size * (page - 1)
    end_index = start_index + page_size

    return start_index, end_index

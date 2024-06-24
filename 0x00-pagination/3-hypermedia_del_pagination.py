#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination."""

import csv
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with an empty dataset."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cache the dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Index the dataset by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
                }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get hypermedia pagination with index."""
        assert isinstance(index, (int, type(None)))
        assert isinstance(page_size, int) and page_size > 0

        data = self.indexed_dataset()
        dataset_size = len(data)

        if index is None:
            index = 0
        assert 0 <= index < dataset_size

        current_index = index
        data_page = []
        next_index = index

        while len(data_page) < page_size and next_index < dataset_size:
            item = data.get(next_index)
            if item is not None:
                data_page.append(item)
            next_index += 1

        next_index = next_index if next_index < dataset_size else None

        return {
            'index': current_index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data_page
        }

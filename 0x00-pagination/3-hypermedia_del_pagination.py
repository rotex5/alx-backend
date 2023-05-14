#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import Any, Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
         return a dictionary with the following key-value pairs
            * index: the current start index of the return page.
            * next_index: the next index to query with.
            * page_size: the current page size.
            * data: the actual page of the dataset.
        """
        indexed_data = self.indexed_dataset()

        assert type(index) is int and index < len(indexed_data) - 1

        count: int = 0
        current_index: int = index
        data: List[Any] = []

        while count < page_size and current_index < len(indexed_data):
            value = indexed_data.get(current_index)
            if value:
                data.append(value)
                count += 1
            current_index += 1

        next_index = None
        while current_index < len(indexed_data):
            value = indexed_data.get(current_index)
            if value:
                next_index = current_index
                break
            current_index += 1

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index,
        }

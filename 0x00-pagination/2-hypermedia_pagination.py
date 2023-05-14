#!/usr/bin/env python3
"""
Simple pagination
Hypermedia pagination
"""
import csv
from math import ceil
from typing import Any, Dict, List, Optional
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Takes 2 integer arguments (page (int) and page_size(int))
        Returns a list of lists containing required data from the dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        self.dataset()

        if self.__dataset is None:
            return []

        _range = index_range(page, page_size)
        return self.__dataset[_range[0]:_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Returns dictionary value containing information about dataset:
        * page_size: the length of the returned dataset page
        * page: the current page number
        * data: the dataset page (equivalent to return from previous task)
        * next_page: number of the next page, None if no next page
        * prev_page: number of the previous page, None if no previous page
        * total_pages: the total number of pages in the dataset as an integer
        """
        data: List[List] = self.get_page(page, page_size)
        total_pages: int = ceil(len(self.dataset()) / page_size)
        page_size = len(data)
        next_page: Optional[int] = page + 1 if page < total_pages else None
        prev_page: Optional[int] = page - 1 if page > 1 else None
        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

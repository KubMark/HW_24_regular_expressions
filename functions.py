import re
from re import Pattern
from typing import Iterable, Any


def filter_query(value: str, data: Iterable[str]) -> list:
    """return filtered data by value"""
    return list(filter(lambda x: value in x, data))


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> Iterable[str]:
    """return unique data"""
    return set(data)


def limit_query(value: str, data: Iterable[str]) -> list:
    """returns limit list"""
    limit: int = int(value)
    return list(data)[:limit]


def map_query(value: str, data: Iterable[str]) -> Iterable[str]:
    """returns by one column from data"""
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number], data)


def sort_query(value: str, data: Iterable[str]) -> Iterable[str]:
    """returns sorted data in asc. or desc. order"""
    reverse = value == "desc"
    return sorted(data, reverse=reverse)


def regex_query(value: str, data: Iterable[str]) -> Iterable[str]:
    regex: Pattern[str] = re.compile(value)
    return list(filter(lambda x: re.search(regex, x), data))
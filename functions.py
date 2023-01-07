from typing import Iterable


def filter_query(value: str, data: Iterable[str]):
    """return filtered data by value"""
    return filter(lambda x: value in x, data)


def unique_query(data, *args, **kwargs):
    """return unique data"""
    return set(data)


def limit_query(value, data):
    """returns limit list"""
    limit: int = int(value)
    return list(data)[:limit]


def map_query(value, data):
    """returns by one column from data"""
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number], data)


def sort_query(value, data):
    """returns sorted data in asc. or desc. order"""
    reverse = value == "desc"
    return sorted(data, reverse=reverse)

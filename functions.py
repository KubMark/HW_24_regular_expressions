import re
from re import Pattern
from typing import Iterable, Any, Generator, Optional, Callable
from flask import Response, jsonify


def read_file(file_name: str) -> Generator:
    with open(file_name) as file:
        for line in file:
            yield line


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

COMMANDS: dict[Optional[str], Callable] = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
    'regex': regex_query
}


def execute(query: dict[str, str], filename: str) -> Response:
    """
    Execute user commands
    """
    data = read_file(filename)
    cmd1 = query.get("cmd1")
    cmd2 = query.get("cmd2")
    data = COMMANDS[cmd1](value=query["value1"], data=data)
    if cmd2:
        data = COMMANDS[cmd2](value=query["value2"], data=data)
    return jsonify(list(data))
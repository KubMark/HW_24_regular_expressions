from typing import Optional, Generator, List, Any

from flask import Response

from functions import filter_query, unique_query, limit_query, map_query, sort_query, regex_query

CMD_TO_FUNCTIONS = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
    'regex': regex_query
}


def read_file(file_name: str) -> Generator:
    with open(file_name) as file:
        for line in file:
            yield line


def build_query(cmd: str, value: str, file_name: str, data: Optional[list[str]]) -> list[str]:

    prepared_data = read_file(file_name)
    return list(CMD_TO_FUNCTIONS[cmd](value=value, data=prepared_data))



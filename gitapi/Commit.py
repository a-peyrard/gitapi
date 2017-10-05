"""
Manage commit objects, parse, create, and so on...
"""

import re
from collections import namedtuple
from datetime import datetime

Commit = namedtuple(
    "Commit",
    "hash author date title"
)

LINE_PATTERN = re.compile(r"(\w+) '(.*?)' (\d+) (.*)")


def extract_commit(line: str) -> Commit:
    """
    Parse git log output line and extract a commit from it.

    :param line: the line to parse
    :return: the extracted commit
    """
    result = LINE_PATTERN.match(line)
    if len(result.groups()) != 4:
        raise RuntimeError(
            "Unable to parse line, found %d groups: %s" %
            (len(result.groups()), line)
        )

    return Commit(
        hash=result.group(1),
        author=result.group(2),
        date=datetime.utcfromtimestamp(int(result.group(3))),
        title=result.group(4)
    )

import os
from typing import Tuple

AUTHORS_FILENAME = "AUTHORS"
AUTHORS_FILEPATH = os.path.join(os.path.dirname(__file__), AUTHORS_FILENAME)


def get_authors() -> Tuple[str, str]:
    with open(AUTHORS_FILEPATH, "r") as fd:
        for author_line in fd.readlines():
            tokens = author_line.split("<")
            email = tokens[1].strip()[:-1]
            tokens = tokens[0].strip().split("(")
            name = tokens[0]
            nickname = tokens[1][:-1]
            yield (nickname, name, f"mailto:{email}")

"""Reject missing, malformed, or error cards before replacing the saved images."""

from pathlib import Path
import re
import xml.etree.ElementTree as ET


CARDS = (
    "profile-details",
    "streak",
    "streak-weekly",
    "trophies",
    "stats",
    "top-langs",
)
ERROR_MESSAGE = re.compile(
    r"something went wrong|rate limit|bad credentials|"
    r"error fetching|failed to (?:fetch|retrieve)|"
    r"could not (?:fetch|retrieve)|unable to (?:fetch|retrieve)|user not found",
    re.IGNORECASE,
)


def validate(directory=Path("profile")):
    for name in CARDS:
        path = directory / f"{name}.svg"
        root = ET.parse(path).getroot()
        if root.tag != "{http://www.w3.org/2000/svg}svg":
            raise ValueError(f"{path}: expected an SVG image")
        text = " ".join(root.itertext())
        if ERROR_MESSAGE.search(text):
            raise ValueError(f"{path}: renderer returned an error card")
        if not any(node.tag.endswith("}text") for node in root.iter()):
            raise ValueError(f"{path}: card contains no text")
        print(f"Valid: {path}")


if __name__ == "__main__":
    validate()

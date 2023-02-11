from typing import List


class KochSnowflake:
    def __init__(self, level: int = 3):
        self.level: int = level

    @property
    def data(self) -> List[str]:
        return ["Z"]

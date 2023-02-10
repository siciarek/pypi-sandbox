from typing import List


class KochSnowflake:
    def __init__(self, level: int = 3):
        self.level: int = level

    def get_data(self) -> List[str]:
        return ["Z"]

from . import images
from collections.abc import Iterator
from typing import Type

class Image:
    def __init__(self, image: Type[images.IMAGES], tag: str, build_logs: Iterator[dict | list | str | int | float | bool | None]):
        self.image = image
        self.tag = tag
        self.build_logs = build_logs

    # def delete_image(self):
    #     pass




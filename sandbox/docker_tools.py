from collections.abc import Iterator
from tkinter.tix import IMAGE
from typing import AnyStr

import docker
import utils
import images




class Builder:
    def build(self, dockerfile: images.IMAGES, path: str='.', suffix_len: int=16):
        import docker
        import os

        tag = f'di-{dockerfile.get_dockerfile_path()}-{utils.generate_random_hex(suffix_len)}'
        client = docker.from_env()
        image, build_logs = client.images.build(path=path,
                                                dockerfile=f'{os.path.abspath(os.path.curdir)}/docker_images/{dockerfile}',
                                                tag=tag)
        Image(tag=tag, build_logs=build_logs)

class Image:
    def __init__(self, image: images.IMAGES, tag: str, build_logs: Iterator[dict | list | str | int | float | bool | None]):
        self.image = image
        self.tag = tag
        self.build_logs = build_logs




class Runer:
    def run(self, image: Image, start_command='', mem='500M', nano_cpus=10000000):
        class Container(image.image):
            def __init__(self, container):
                self.container = container
                super().__init__(container=self.container)

            def delete_container(self):
                self.container.stop()

            def remove_container(self):
                self.container.remove()

            def restart_container(self):
                self.container.restart()

            def run_code(self, code: str):
                exec_command = self.container.exec_run(code)
                return exec_command.output.decode()

        client = docker.from_env()
        container = client.containers.run(
            image.tag,
            name=f'sandbox-{utils.generate_random_hex(16)}',
            detach=True,
            command=start_command,
            nano_cpus=nano_cpus,
            mem_limit=mem,
            network_mode="none"

        )
        return Container(container=container)












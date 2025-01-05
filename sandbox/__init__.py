from typing import Type
import docker

import os

from . import utils
from .images import IMAGES, Python, Ubuntu, Container
from .utils_types import Image


__all__ = ['build', 'run', 'get_container', 'Image', 'Container', 'Python', 'Ubuntu']


lib_path = '/'.join(__file__.split('/')[:-1])


def build(dockerfile: Type[IMAGES], path: str=f'{lib_path}/', suffix_len: int=16) -> Image:
    tag = f'di-{dockerfile.get_dockerfile_path()}-{utils.generate_random_hex(suffix_len)}'
    client = docker.from_env()
    image, build_logs = client.images.build(path=path,
                                            dockerfile=f'{lib_path}/docker_images/{dockerfile.get_dockerfile_path()}',
                                            tag=tag)
    return Image(image=dockerfile, tag=tag, build_logs=build_logs)


def run(image: Image, start_command='', mem='500M', nano_cpus=10000000) -> IMAGES:
    client = docker.from_env()
    container = client.containers.run(
        image.tag,
        name=f'sandbox-{utils.generate_random_hex(16)}',
        detach=True,
        command=start_command,
        nano_cpus=nano_cpus,
        mem_limit=mem,
        network_mode="none",
        tty=True,  # Создание псевдотерминала
        stdin_open=True

    )
    return image.image(container=container)


def get_container(container_id: str, image: Type[IMAGES]=None) -> IMAGES | Container:
    client = docker.from_env()
    container = client.containers.get(container_id)
    if image:
        return image(container=container)
    else:
        return Container(container=container)



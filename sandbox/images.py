import docker
from docker.models import containers
class Container:
    def __init__(self, container: containers.Container):
        self.container = container

    def start_container(self):
        self.container.start()

    def get_logs(self):
        return self.container.logs().decode()

    def stop_container(self):
        self.container.stop()

    def remove_container(self):
        self.container.remove()

    def restart_container(self):
        self.container.restart()

    def run_command(self, command: str) -> str:
        exec_command = self.container.exec_run(command, tty=True, stdin=True)
        return exec_command.output.decode()


class Python(Container):
    def __init__(self, container):
        self.container = container
        super().__init__(container=container)

    @staticmethod
    def get_dockerfile_path():
        return 'python.dockerfile'

    @staticmethod
    def code_format(code: str):
        return f'python -c "{code.replace("\u00A0", " ").replace('\"', r'\"')}"'

    def run_code(self, code):
        exec_command = self.container.exec_run(Python.code_format(code), tty=True, stdin=True)
        return exec_command.output.decode()


class Ubuntu(Container):
    def __init__(self, container):
        self.container = container
        super().__init__(container=container)

    @staticmethod
    def get_dockerfile_path():
        return 'ubuntu.dockerfile'




IMAGES = Python | Ubuntu
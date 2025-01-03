import docker



class Python:
    def __init__(self, container):
        self.container = container

    @staticmethod
    def get_dockerfile_path():
        return 'python.dockerfile'

    @staticmethod
    def code_format(code: str):
        return f'python -c "{code.replace("\u00A0", " ").replace('\"', r'\"')}"'

    def run_code(self, code):

        exec_command = self.container.exec_run(code)
        return exec_command.output.decode()



IMAGES = Python
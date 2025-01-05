# docker_sandbox



## Start
to use the library, you need to install and run docker and install python docker lib
```bash
pip install -r requirements.txt
```



## Example
```py
import sandbox
image = sandbox.build(dockerfile=sandbox.Python)
container = sandbox.run(image=image)
print(container.container.id)
print(container.run_command('echo hi')) # run command
print(container.run_code('print(1)')) # run python code
container.stop_container()
container.remove_container()
```
> [!TIP]
> you can get the container by its ID using `get_container`
> ```py
> sandbox.get_container('ID')
> ```

you can use `start_command`
```py
import sandbox
image = sandbox.build(dockerfile=sandbox.Python)
container = sandbox.run(image=image, start_command=sandbox.Python.code_format('print(1)'))
print(container.get_logs())
container.stop_container()
container.remove_container()
```
> [!WARNING]
> if you use `start_command`, the container will shut down after executing your command



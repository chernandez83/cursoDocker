# extras
import docker

client = docker.DockerClient('unix://var/run/docker.sock')

for container in client.containers.list():
    print(container.name)
    print(container.id)

container = client.containers.run('nginx', detach=True, ports={'80/tcp': 80})
print(container.id)
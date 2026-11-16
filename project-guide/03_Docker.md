# Docker – Important Commands

A practical reference for building, running, testing, and debugging Docker applications.

## 1. Docker Installation and Verification

**Check Docker version**

```powershell
docker --version
```

Displays the installed Docker version.

**Check Docker Compose version**

```powershell
docker compose version
```

Displays the installed Docker Compose version.

**Check whether Docker is running**

```powershell
docker info
```

Displays Docker engine information. If Docker is not running, start Docker Desktop.

**List running containers**

```powershell
docker ps
```

Displays currently running containers.

**List all containers**

```powershell
docker ps -a
```

Displays running and stopped containers.

## 2. Docker Images

**Build an image**

```powershell
docker build -t my-app .
```

Builds a Docker image using the Dockerfile in the current directory and assigns it the name `my-app`.

**Build without using cache**

```powershell
docker build --no-cache -t my-app .
```

Builds the image from scratch without reusing cached build layers. Useful when troubleshooting build issues.

**List images**

```powershell
docker images
```

Displays locally available Docker images.

**Remove an image**

```powershell
docker rmi my-app
```

Removes a local image. The image must not be in use by an existing container.

**Pull an image**

```powershell
docker pull python:3.11-slim
```

Downloads an image from a container registry.

## 3. Docker Containers

**Run a container**

```powershell
docker run -d -p 8501:8501 --name my-container my-app
```

Creates and starts a container in the background.

- `-d`: Runs in the background.
- `-p`: Maps a host port to a container port.
- `--name`: Assigns a container name.

**Run an interactive container**

```powershell
docker run -it python:3.11-slim bash
```

Starts a container with an interactive terminal.

**Stop a container**

```powershell
docker stop my-container
```

Gracefully stops a running container.

**Start a stopped container**

```powershell
docker start my-container
```

Starts an existing stopped container.

**Restart a container**

```powershell
docker restart my-container
```

Stops and starts the specified container.

**Remove a container**

```powershell
docker rm my-container
```

Removes a stopped container.

**Force remove a container**

```powershell
docker rm -f my-container
```

Stops and removes a container immediately.

## 4. Container Inspection and Debugging

**View container logs**

```powershell
docker logs my-container
```

Displays the container's logs.

**Follow live logs**

```powershell
docker logs -f my-container
```

Continuously displays new log messages.

**Show the last 100 log lines**

```powershell
docker logs --tail 100 my-container
```

Displays only the latest 100 log lines.

**Open a shell inside a running container**

```powershell
docker exec -it my-container bash
```

Opens an interactive Bash shell inside the container.

If Bash is unavailable:

```powershell
docker exec -it my-container sh
```

**Inspect container configuration**

```powershell
docker inspect my-container
```

Displays detailed container configuration, networking, mounts, and status information.

**Check container resource usage**

```powershell
docker stats
```

Displays live CPU, memory, network, and disk I/O statistics.

**Check port mappings**

```powershell
docker port my-container
```

Displays the host and container port mappings.

## 5. Docker Compose

Docker Compose manages multiple connected services using a `docker-compose.yml` file.

**Build and start all services**

```powershell
docker compose up -d --build
```

Builds images if necessary and starts all services in the background.

**Start services without rebuilding**

```powershell
docker compose up -d
```

Starts services using the existing images.

**Stop services**

```powershell
docker compose stop
```

Stops running services without removing their containers.

**Stop and remove containers and networks**

```powershell
docker compose down
```

Stops and removes the containers and networks created by Compose. Named volumes are retained by default.

**List service status**

```powershell
docker compose ps
```

Displays the status of Compose services.

**View logs**

```powershell
docker compose logs
```

Displays logs from all Compose services.

**Follow live logs**

```powershell
docker compose logs -f
```

Continuously displays logs from all services.

**View logs of one service**

```powershell
docker compose logs -f backend
```

Displays live logs for the specified service. Replace `backend` with your service name.

**Rebuild one service**

```powershell
docker compose up -d --build frontend
```

Rebuilds and restarts only the specified service and any required dependencies.

**Execute a command inside a service**

```powershell
docker compose exec backend sh
```

Opens a shell inside the running backend service.

**Validate Compose configuration**

```powershell
docker compose config
```

Checks and displays the resolved Compose configuration.

## 6. Docker Networks and Volumes

**List networks**

```powershell
docker network ls
```

Displays available Docker networks.

**Inspect a network**

```powershell
docker network inspect NETWORK_NAME
```

Displays connected containers and network configuration.

**List volumes**

```powershell
docker volume ls
```

Displays Docker volumes.

**Inspect a volume**

```powershell
docker volume inspect VOLUME_NAME
```

Displays details about a specific volume.

**Remove an unused volume**

```powershell
docker volume rm VOLUME_NAME
```

Removes a volume that is not being used by a container.

## 7. Cleanup Commands

**Remove stopped containers**

```powershell
docker container prune
```

Removes all stopped containers after confirmation.

**Remove unused images**

```powershell
docker image prune
```

Removes dangling images that are not being used.

**Remove unused Docker resources**

```powershell
docker system prune
```

Removes unused containers, networks, and dangling images after confirmation.

> Warning: Cleanup commands can delete resources. Check what is being used before confirming.

## 8. Common Docker Problems

| Problem | What to check |
|---|---|
| Docker daemon not running | Start Docker Desktop |
| Port already allocated | Check `docker ps` and existing port mappings |
| Image build fails | Check Dockerfile and build logs |
| Container exits immediately | Run `docker logs CONTAINER_NAME` |
| Application inaccessible | Verify port mapping and application host binding |
| Container cannot connect to another service | Check Compose service names and network configuration |
| Changes not reflected | Rebuild the image using `--build` |
| Container is unhealthy | Inspect health-check configuration and container logs |


# Install Antares Base

This installation of [Antares base](../overview/architecture.md#base-version) 
is more technical than the Desktop installation, as it involves
the use of an Ubuntu Server and Docker. 

You can find the architecture of the base version of Antares 
[here](../overview/architecture.md#base-version). 

## Installing Antares Web

### Prerequisites

#### System Requirements

- **OS**: Ubuntu 24.04.3 LTS
- **RAM**: 512 GB
- **CPU**: 72 cores
- **Access**: Root or sudo access
- **Internet**: Required to pull Docker images

#### Required Software

Ensure the following tools are installed:

- **uv**: Python package and project manager
  ([Download](https://docs.astral.sh/uv/getting-started/installation/))
- **Python**: >= 3.11.x ([Download](https://www.python.org/downloads/))
- **Node.js**: 22.13.0 ([Download](https://nodejs.org/en/download/))
- **Git**: Latest version ([Download](https://git-scm.com/downloads))
- **Docker**: For containerized deployment ([Download](https://docs.docker.com/get-docker/))
- **PostgreSQL**: For production database ([Download](https://www.postgresql.org/download/))
- **Redis**: For production caching ([Download](https://redis.io/download))

### Installation

#### Create Base Directory

```bash
sudo mkdir /opt/AntaREST/
cd /opt/AntaREST/
```

### Clone the repo for the latest version tag

```bash
sudo git clone --branch <tag> https://github.com/AntaresSimulatorTeam/AntaREST.git AntaREST-<tag>/
```

#### Set up python environment

```bash
uv venv .venv
source .venv/bin/activate  
```

#### Install python dependencies

```bash
uv pip install --upgrade pip
uv sync
```

#### Create a service (optional)

##### Create a symbolic link

```bash
sudo ln -sfn AntaREST-<tag> latest
```

##### Edit `antarest.service`

Create the file `/etc/systemd/system/antarest.service`:

```ini
[Unit]
Description=AntaREST Docker Compose Service
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
WorkingDirectory=/opt/AntaREST/latest
ExecStart=/usr/bin/docker compose up -d
ExecStop=/usr/bin/docker compose down
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

#### Install frontend dependencies

##### Dockerfile for jrontend

Create a file named `dockerfile_build_frontend`:

```docker
FROM node:22.13.0

WORKDIR /app

COPY webapp/ /app/

RUN npm install
RUN npm run build

CMD ["tail", "-f", "/dev/null"]
```

##### Build and run the Frontend

```docker
docker build -t webapp-builder -f dockerfile_build_frontend .
docker run --name webapp-build -d webapp-builder
docker cp webapp-build:/app/dist ./webapp
docker stop webapp-build
docker rm webapp-build
```

### Installation of Antares Simulator

#### Download latest version

```bash
curl -OL https://github.com/AntaresSimulatorTeam/Antares_Simulator/releases/download/v<x.x.x>/antares-<x.x.x>-Ubuntu-22.04.tar.gz
tar xzvf antares-<x.x.x>-Ubuntu-22.04.tar.gz
```

#### Edit `docker-compose.yml`

Edit the `docker-compose.yml` file to update the Antares Simulator version:

```yaml
services:
  antares-antarest:
    volumes:
      - ./antares-<x.x.x>-Ubuntu-22.04/bin:/antares_simulator
    depends_on:
      redis:
        condition: service_started
      postgresql:
        condition: service_started
```

#### Build Docker Image

```bash
sudo docker build --no-cache -t antarest\:latest .
docker images
```

#### Create and start containers

##### Using Docker Compose

```bash
docker compose up -d
docker compose ps -a
```

##### As a service

```bash
sudo systemctl start antarest
sudo systemctl status antarest
```

### Configuration

#### Change Default Port

Edit `resources/deploy/nginx.conf` to change the default port:

```
listen 8081;
listen [::]:8081;
```

#### Change Users’ Configurations

Edit `resources/deploy/config.prod.yaml` to update JWT token keys and user lists:

```yaml
security:
  disabled: false
  jwt:
    key: secretkeytochange
  login:
    admin:
      pwd: admin
```

## Troubleshooting

### Error on Postgres Database Version

#### Logs

```
postgres | Error: in 18+, these Docker images are configured to store database data in a format which is compatible with "pg_ctlcluster" (specifically, using major-version-specific directory names).
```

#### Solution

Update the PostgreSQL service image to version 17:

```yaml
postgresql:
  image: postgres:17
```

### GLIBC / GLIBCXX Version Errors in Docker

#### Symptoms

- `GLIBC_2.32 / 2.33 / 2.34 not found`
- `GLIBCXX_3.4.29 / 3.4.30 not found`

#### Solution

Use a newer Debian base image:

```
FROM python:3.11-slim-bookworm
```

### PostgreSQL “Too Many Clients Already” Error with Gunicorn

#### Symptoms

```
psycopg2.OperationalError: connection to server at "postgresql" (...) failed: FATAL: sorry, too many clients already
```

#### Solution

Limit the number of Gunicorn workers in `resources/deploy/gunicorn.py`:

```python
workers = 4
```

### Redis Connection Error with Non-Admin Users

#### Symptoms

```
aredis.exceptions.ConnectionError
TypeError: create_connection() got an unexpected keyword argument 'loop'
```

#### Workaround

Disable Redis-based rate limiting in `antarest/main.py`:

```python
application.add_middleware(
    RateLimitMiddleware,
    authenticate=auth_manager.create_auth_function(),
    backend=MemoryBackend(),
    config=RATE_LIMIT_CONFIG,
)
```

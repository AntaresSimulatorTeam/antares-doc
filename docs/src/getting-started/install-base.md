# Install Antares Base

!!! info

    This document describes a **clean installation** of AntaREST 2.26.0 using Docker Compose. It is intended as a **technical, step-by-step guide** for system administrators or engineers.

Here is the architecture of the base version of Antares: 

DIAGRAM

## AntaresWeb 2.26.0 – Installation Guide

### Prerequisites

### System Requirements

- **OS**: Ubuntu 24.04.3 LTS
- **RAM**: 512 GB
- **CPU**: 72 cores
- **Access**: Root or sudo access
- **Internet**: Required to pull Docker images

#### Required Software

Ensure the following tools are installed:

- **Python**: >= 3.11.x ([Download](https://www.python.org/downloads/))
- **Node.js**: 22.13.0 ([Download](https://nodejs.org/en/download/))
- **Git**: Latest version ([Download](https://git-scm.com/downloads))
- **Docker**: For containerized deployment ([Download](https://docs.docker.com/get-docker/))
- **PostgreSQL**: For production database ([Download](https://www.postgresql.org/download/))
- **Redis**: For production caching ([Download](https://redis.io/download))

### Installation of Antares REST API

Antares Web is a web application providing a modern REST API and web interface for managing Antares Simulator studies, adding powerful features for collaboration, storage optimization, and advanced editing capabilities.

- **License**: Apache-2.0
- **Documentation**: [Antares Web Installation Guide](https://antares-web.readthedocs.io/en/latest/developer-guide/install/0-INSTALL/)
- **GitHub**: [AntaREST Sources](https://github.com/AntaresSimulatorTeam/AntaREST)

#### Create Base Directory

```bash
sudo mkdir /opt/AntaREST/
cd /opt/AntaREST/
````
### Clone the Repository for Tag v2.26.0

```bash
sudo git clone --branch v2.26.0 https://github.com/AntaresSimulatorTeam/AntaREST.git AntaREST-2.26.0/
```

#### Set Up Python Environment

```bash
conda create -n antarest python=3.11
conda activate antarest
```

#### Install Python Dependencies

```bash
python3 -m pip install --upgrade pip
pip install -e .
pip install -r requirements.txt
```

#### Create a Service (Optional)

##### Create a Symbolic Link

```bash
sudo ln -sfn AntaREST-2.26.0 latest
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

#### Install Frontend Dependencies

##### Dockerfile for Frontend

Create a file named `dockerfile_build_frontend`:

```docker
FROM node:22.13.0

WORKDIR /app

COPY webapp/ /app/

RUN npm install
RUN npm run build

CMD ["tail", "-f", "/dev/null"]
```

##### Build and Run the Frontend

```docker
docker build -t webapp-builder -f dockerfile_build_frontend .
docker run --name webapp-build -d webapp-builder
docker cp webapp-build:/app/dist ./webapp
docker stop webapp-build
docker rm webapp-build
```

### Installation of Antares Simulator

Antares-Simulator is an Open Source power system simulator to quantify the adequacy or the economic performance of interconnected energy systems, at short or remote time horizons.

- **License**: Mozilla Public License Version 2.0
- **Documentation**: [Antares Simulator Installation Guide](https://antares-simulator.readthedocs.io/en/latest/user-guide/02-install/)
- **GitHub**: [Antares Simulator Sources](https://github.com/AntaresSimulatorTeam/Antares_Simulator)

#### Download Version 9.3.0

```bash
curl -OL https://github.com/AntaresSimulatorTeam/Antares_Simulator/releases/download/v9.3.0/antares-9.3.0-Ubuntu-22.04.tar.gz
tar xzvf antares-9.3.0-Ubuntu-22.04.tar.gz
```

#### Edit `docker-compose.yml`

Edit the `docker-compose.yml` file to update the Antares Simulator version:

```yaml
services:
  antares-antarest:
    volumes:
      # - ./antares-8.8.17-Ubuntu-22.04/bin:/antares_simulator
      - ./antares-9.3.0-Ubuntu-22.04/bin:/antares_simulator
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

#### Create and Start Containers

##### Using Docker Compose

```bash
docker compose up -d
docker compose ps -a
```

##### As a Service

```bash
sudo systemctl start antarest
sudo systemctl status antarest
```

---

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

---

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

---

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

---

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

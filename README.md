# Docker crash course

## Introduction

- What containers are and why they matter
- Containers vs Virtual Machines
- Docker overview: engine, CLI, registry

---

## 1. Core Docker concepts

### 1.1 Architecture & terminology

- Docker daemon, client, images, containers, registries
- Layers & the UnionFS concept

### 1.2 Basic commands

- `docker pull`, `run`, `ps`, `stop`, `rm`, `rmi`
- Detached mode, ports (`-p`), environment vars (`-e`), volumes (`-v`)
- Inspecting containers: `docker logs`, `exec`, `inspect`

---

## 2. Building and managing images

### 2.1 Dockerfile essentials

- Key instructions: `FROM`, `RUN`, `COPY`, `WORKDIR`, `CMD`, `EXPOSE`, `ENV`
- Build images (`docker build`), tagging, caching
- Lightweight and secure image best practices

### 2.2 Registries & sharing

- Docker Hub and private registries
- `docker push`, `docker login`, image tags and versioning

---

## 3. Data & networking

### 3.1 Volumes and persistence

- Bind mounts vs named volumes
- Typical use case: persisting database data

### 3.2 Networking basics

- Default bridge network
- Custom networks (`docker network create`, `connect`)
- Exposing services, container-to-container communication

---

## 4. Multi-container apps

- Intro to Docker Compose
- Structure of a `docker-compose.yml`
- `docker compose up/down`, scaling services, environment variables

---

## 5. Podman in a nutshell

### 5.1 What Podman is

- Daemonless and rootless approach
- CLI compatibility: `alias docker=podman`

### 5.2 Key differences & when to use

- Rootless containers for better isolation
- Pod concept (groups of containers)
- Integration with `systemd`
- Compatibility notes and ecosystem tradeoffs

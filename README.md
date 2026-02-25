# Payment API

[![CI](https://github.com/anshumaan-10/payment-api/actions/workflows/build-push.yaml/badge.svg)](https://github.com/anshumaan-10/payment-api/actions/workflows/build-push.yaml)
[![Docker Hub](https://img.shields.io/docker/v/anshumaan10/payment-api?label=Docker%20Hub)](https://hub.docker.com/r/anshumaan10/payment-api)

Part of the [k8s-security-lab](https://github.com/anshumaan-10/k8s-security-lab) — a hands-on Kubernetes security research environment.

> **Hardened service** — runs as non-root (`uid=1000`), read-only filesystem, no privilege escalation. Contrast with [phoenix](https://github.com/anshumaan-10/phoenix) which is intentionally vulnerable.

---

## What Is This

A mock payment transaction API that returns fake transaction and customer data. It exists to demonstrate:
- A **hardened** Kubernetes workload (vs. the vulnerable phoenix app)
- Internal service-to-service communication (checkout polls this)
- How `NetworkPolicy` should restrict access to this service

---

## Endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Service info |
| `GET` | `/health` | Health check |
| `GET` | `/transactions` | List transactions |
| `GET` | `/customers` | List customers |

---

## Quick Start

```bash
docker run -p 8081:8080 anshumaan10/payment-api:latest

curl http://localhost:8081/transactions
curl http://localhost:8081/customers
curl http://localhost:8081/health
```

Or with the full stack:

```bash
git clone https://github.com/anshumaan-10/k8s-security-lab
cd k8s-security-lab
docker compose up
```

---

## Security Properties

| Property | Value |
|---|---|
| Run as root | No — `uid=1000` (appuser) |
| Privilege escalation | Disabled (`allowPrivilegeEscalation: false`) |
| Read-only filesystem | Yes |
| Image | Multi-stage build — no build tools in final image |
| Dependency management | `uv` lock file — exact reproducible deps |

---

## CI/CD

On every push to `main`, GitHub Actions builds `linux/amd64` and pushes:
- `anshumaan10/payment-api:<commit-sha>`
- `anshumaan10/payment-api:latest`

Then updates `deployments/payment-api/deployment.yaml` in [k8s-lab-deployments](https://github.com/anshumaan-10/k8s-lab-deployments).

**Required GitHub Secrets:**

| Secret | Value |
|---|---|
| `DOCKERHUB_USERNAME` | `anshumaan10` |
| `DOCKERHUB_TOKEN` | Docker Hub access token |
| `DEPLOY_PAT` | GitHub PAT with `repo` scope |

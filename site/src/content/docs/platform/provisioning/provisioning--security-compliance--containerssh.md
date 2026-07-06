---
title: ContainerSSH
description: "ContainerSSH launches a new container for each SSH connection in Kubernetes, Podman or Docker. The user is transparently dropped in the container and the container is removed when the user disconnect…"
domain: "platform"
category: "Provisioning"
subcategory: "Security & Compliance"
project_id: "provisioning--security-compliance--containerssh"
maturity: "sandbox"
openapi_status: todo
sidebar:
  badge:
    text: Sandbox
    variant: note
---

# ContainerSSH

![ContainerSSH](/logos/adc1c159aef3ffe90437f3f435f3cec31111192a24a11893d90ff5a5971b9a8e.svg)

**Domena:** [Platforma i infrastruktura](../index.md) · **Kategoria:** [Provisioning](index.md) · Security & Compliance  
**Open source:** tak

## Opis

ContainerSSH launches a new container for each SSH connection in Kubernetes, Podman or Docker. The user is transparently dropped in the container and the container is removed when the user disconnects. Authentication and container configuration are dynamic using webhooks, no system users required.

## Use cases

- ContainerSSH: ContainerSSH launches a new container for each SSH connection in Kubernetes, Podman or Docker. The user is transparently dropped in the container and the container is removed when the user disconnects. Authentication and container configuration are dynamic using webhooks, no system users required
- Skanowanie obrazów i runtime security w K8s
- Policy-as-code dla admission control
- CIS benchmarks i hardening klastrów
- Budowa i utrzymanie platformy Kubernetes / cloud native

_Sekcja wygenerowana heurystycznie — popraw według własnego doświadczenia._

## Alternatywy

- [cert-manager](/platform/provisioning/provisioning--security-compliance--cert-manager/) — Ta sama subkategoria: Security & Compliance · CNCF graduated · ⭐ 13,859
- [Open Policy Agent (OPA)](/platform/provisioning/provisioning--security-compliance--open-policy-agent-opa/) — Ta sama subkategoria: Security & Compliance · CNCF graduated · ⭐ 11,852
- [Falco](/platform/provisioning/provisioning--security-compliance--falco/) — Ta sama subkategoria: Security & Compliance · CNCF graduated · ⭐ 9,040
- [Kyverno](/platform/provisioning/provisioning--security-compliance--kyverno/) — Ta sama subkategoria: Security & Compliance · CNCF graduated · ⭐ 7,831

## Dokumentacja

- [Strona główna](https://containerssh.io)
- [DevStats CNCF](https://containerssh.devstats.cncf.io/)
- [Slack](https://cloud-native.slack.com/)
- [Artwork](https://github.com/cncf/artwork/tree/master/projects/containerssh)

### Repozytoria

- [containerssh](https://github.com/containerssh/containerssh)

## OpenAPI

> **TODO:** Pełna specyfikacja w submodule `openapi/provisioning--security-compliance--containerssh` — aktualizacja przez CI/CD.

| | |
|---|---|
| Status | `todo` |
| Docelowy URL | [/openapi/provisioning--security-compliance--containerssh/](/openapi/provisioning--security-compliance--containerssh/) |
| Submodule | `openapi/provisioning--security-compliance--containerssh` |
| Szukaj w repo | [źródło](https://github.com/containerssh/containerssh/tree/HEAD) |

## Metadane CNCF

| Pole | Wartość |
|------|---------|
| Accepted | 2022-09-14 |
| Graduated | — |
| Incubating | — |
| Archived | — |
| CLOMonitor | containerssh |

## GitHub

- Gwiazdki GitHub: **3,054**
- Licencja: **Apache License 2.0**
- Tematy: `containers`, `devsecops`, `docker`, `kubernetes`, `security`, `security-tools`, `ssh`

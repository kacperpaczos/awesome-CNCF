---
title: bootc
description: "The bootc provides transactional, in-place operating system images and updates using OCI/Docker container images. This project applies the Docker container layering model to bootable host systems, us…"
domain: "platform"
category: "Runtime"
subcategory: "Container Runtime"
project_id: "runtime--container-runtime--bootc"
maturity: "sandbox"
openapi_status: todo
sidebar:
  badge:
    text: Sandbox
    variant: note
---

# bootc

![bootc](/logos/a703ff53acb6fd7ffb9e19709c76c14351ed9f88604b922a656ed6519695e48f.svg)

**Domena:** [Platforma i infrastruktura](../index.md) · **Kategoria:** [Runtime](index.md) · Container Runtime  
**Open source:** tak

## Opis

The bootc provides transactional, in-place operating system images and updates using OCI/Docker container images. This project applies the Docker container layering model to bootable host systems, using standard OCI/Docker containers as a transport and delivery format for base operating system updates.

## Use cases

- bootc: The bootc provides transactional, in-place operating system images and updates using OCI/Docker container images. This project applies the Docker container layering model to bootable host systems, using standard OCI/Docker containers as a transport and delivery format for base operating system updates
- Uruchamianie kontenerów OCI w Kubernetes i środowiskach edge
- Izolacja workloadów z niskim narzutem wydajnościowym
- Integracja z CRI w platformach PaaS i bare metal
- Warstwa wykonawcza kontenerów i storage/network dla podów

_Sekcja wygenerowana heurystycznie — popraw według własnego doświadczenia._

## Alternatywy

- [containerd](/platform/runtime/runtime--container-runtime--containerd/) — Ta sama subkategoria: Container Runtime · CNCF graduated · ⭐ 20,835
- [CRI-O](/platform/runtime/runtime--container-runtime--cri-o/) — Ta sama subkategoria: Container Runtime · CNCF graduated · ⭐ 5,622
- [Lima](/platform/runtime/runtime--container-runtime--lima/) — Ta sama subkategoria: Container Runtime · CNCF incubating · ⭐ 21,227
- [Podman Container Tools](/platform/runtime/runtime--container-runtime--podman-container-tools/) — Ta sama subkategoria: Container Runtime · CNCF sandbox · ⭐ 32,018

## Dokumentacja

- [Strona główna](https://bootc-dev.github.io)
- [DevStats CNCF](https://bootc.devstats.cncf.io)
- [Artwork](https://github.com/cncf/artwork/tree/master/projects/bootc)

### Repozytoria

- [bootc](https://github.com/bootc-dev/bootc)

## OpenAPI

> **TODO:** Pełna specyfikacja w submodule `openapi/runtime--container-runtime--bootc` — aktualizacja przez CI/CD.

| | |
|---|---|
| Status | `todo` |
| Docelowy URL | [/openapi/runtime--container-runtime--bootc/](/openapi/runtime--container-runtime--bootc/) |
| Submodule | `openapi/runtime--container-runtime--bootc` |
| Szukaj w repo | [źródło](https://github.com/bootc-dev/bootc/tree/HEAD) |

## Metadane CNCF

| Pole | Wartość |
|------|---------|
| Accepted | 2025-01-21 |
| Graduated | — |
| Incubating | — |
| Archived | — |
| CLOMonitor | bootc |

## GitHub

- Gwiazdki GitHub: **2,110**
- Licencja: **Apache License 2.0**

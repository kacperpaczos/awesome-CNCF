---
title: composefs
description: "A project that combines Linux kernel features to provide read-only mountable filesystem trees stacking on top of an underlying 'lower' Linux filesystem, particularly useful for mounting container ima…"
domain: "platform"
category: "Runtime"
subcategory: "Container Runtime"
project_id: "runtime--container-runtime--composefs"
maturity: "sandbox"
openapi_status: todo
sidebar:
  badge:
    text: Sandbox
    variant: note
---

# composefs

![composefs](/logos/2121ac233715cffe4a7d3c1debc815f2b3f2d6920ebd37be8a5b17298e4bd0a4.svg)

**Domena:** [Platforma i infrastruktura](../index.md) · **Kategoria:** [Runtime](index.md) · Container Runtime  
**Open source:** tak

## Opis

A project that combines Linux kernel features to provide read-only mountable filesystem trees stacking on top of an underlying "lower" Linux filesystem, particularly useful for mounting container images.

## Use cases

- composefs: A project that combines Linux kernel features to provide read-only mountable filesystem trees stacking on top of an underlying "lower" Linux filesystem, particularly useful for mounting container images
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

- [Strona główna](https://github.com/containers/composefs)
- [DevStats CNCF](https://composefs.devstats.cncf.io/)

### Repozytoria

- [composefs](https://github.com/containers/composefs)

## OpenAPI

> **TODO:** Pełna specyfikacja w submodule `openapi/runtime--container-runtime--composefs` — aktualizacja przez CI/CD.

| | |
|---|---|
| Status | `todo` |
| Docelowy URL | [/openapi/runtime--container-runtime--composefs/](/openapi/runtime--container-runtime--composefs/) |
| Submodule | `openapi/runtime--container-runtime--composefs` |
| Szukaj w repo | [źródło](https://github.com/containers/composefs/tree/HEAD) |

## Metadane CNCF

| Pole | Wartość |
|------|---------|
| Accepted | 2025-01-21 |
| Graduated | — |
| Incubating | — |
| Archived | — |
| CLOMonitor | composefs |

## GitHub

- Gwiazdki GitHub: **653**
- Licencja: **Other**
- Tematy: `containers`, `filesystem`, `linux`, `oci`, `oci-image`

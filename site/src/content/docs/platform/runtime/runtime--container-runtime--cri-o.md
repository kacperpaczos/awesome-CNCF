---
title: CRI-O
description: "Open Container Initiative-based implementation of Kubernetes Container Runtime Interface"
domain: "platform"
category: "Runtime"
subcategory: "Container Runtime"
project_id: "runtime--container-runtime--cri-o"
maturity: "graduated"
openapi_status: todo
sidebar:
  badge:
    text: Graduated
    variant: success
---

# CRI-O

![CRI-O](/logos/710f6a5529c3084bf79e0584c92e2334ffd011714df93de4beb6de5af7f7b3ee.svg)

**Domena:** [Platforma i infrastruktura](../index.md) · **Kategoria:** [Runtime](index.md) · Container Runtime  
**Open source:** tak

## Opis

Open Container Initiative-based implementation of Kubernetes Container Runtime Interface

## Use cases

- CRI-O: Open Container Initiative-based implementation of Kubernetes Container Runtime Interface
- Uruchamianie kontenerów OCI w Kubernetes i środowiskach edge
- Izolacja workloadów z niskim narzutem wydajnościowym
- Integracja z CRI w platformach PaaS i bare metal
- Warstwa wykonawcza kontenerów i storage/network dla podów

_Sekcja wygenerowana heurystycznie — popraw według własnego doświadczenia._

## Alternatywy

- [containerd](/platform/runtime/runtime--container-runtime--containerd/) — Ta sama subkategoria: Container Runtime · CNCF graduated · ⭐ 20,835
- [Lima](/platform/runtime/runtime--container-runtime--lima/) — Ta sama subkategoria: Container Runtime · CNCF incubating · ⭐ 21,227
- [Podman Container Tools](/platform/runtime/runtime--container-runtime--podman-container-tools/) — Ta sama subkategoria: Container Runtime · CNCF sandbox · ⭐ 32,018
- [WasmEdge Runtime](/platform/runtime/runtime--container-runtime--wasmedge-runtime/) — Ta sama subkategoria: Container Runtime · CNCF sandbox · ⭐ 10,638

## Dokumentacja

- [Strona główna](https://cri-o.io/)
- [DevStats CNCF](https://crio.devstats.cncf.io/)
- [Blog](https://medium.com/cri-o)
- [Slack](https://kubernetes.slack.com/messages/CAZH62UR1)
- [Artwork](https://github.com/cncf/artwork/blob/master/examples/graduated.md#cri-o-logos)

### Repozytoria

- [cri-o](https://github.com/cri-o/cri-o)

## OpenAPI

> **TODO:** Pełna specyfikacja w submodule `openapi/runtime--container-runtime--cri-o` — aktualizacja przez CI/CD.

| | |
|---|---|
| Status | `todo` |
| Docelowy URL | [/openapi/runtime--container-runtime--cri-o/](/openapi/runtime--container-runtime--cri-o/) |
| Submodule | `openapi/runtime--container-runtime--cri-o` |
| Szukaj w repo | [źródło](https://github.com/cri-o/cri-o/tree/HEAD) |

## Metadane CNCF

| Pole | Wartość |
|------|---------|
| Accepted | 2019-04-08 |
| Graduated | 2023-07-19 |
| Incubating | 2019-04-08 |
| Archived | — |
| CLOMonitor | cri-o |

## GitHub

- Gwiazdki GitHub: **5,622**
- Licencja: **Apache License 2.0**
- Tematy: `container-runtime-interface`, `crun`, `hacktoberfest`, `k8s-sig-node`, `kata-containers`, `kubernetes`, `oci`, `oci-runtime`, `runc`

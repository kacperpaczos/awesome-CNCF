---
title: Spegel
description: "Stateless cluster local OCI registry mirror. Spegel enables each node in a Kubernetes cluster to act as a local registry mirror, allowing nodes to share images between themselves. Any image already p…"
domain: "platform"
category: "Provisioning"
subcategory: "Container Registry"
project_id: "provisioning--container-registry--spegel"
maturity: null
openapi_status: todo
---

# Spegel

![Spegel](/logos/67c8e196d2bdc9de67a3875332a2f5522521ff364123e7d652c631dc30427809.svg)

**Domena:** [Platforma i infrastruktura](../index.md) · **Kategoria:** [Provisioning](index.md) · Container Registry  
**Open source:** tak

## Opis

Stateless cluster local OCI registry mirror. Spegel enables each node in a Kubernetes cluster to act as a local registry mirror, allowing nodes to share images between themselves. Any image already pulled by a node will be available for any other node in the cluster to pull.

## Use cases

- Spegel: Stateless cluster local OCI registry mirror. Spegel enables each node in a Kubernetes cluster to act as a local registry mirror, allowing nodes to share images between themselves. Any image already pulled by a node will be available for any other node in the cluster to pull
- Przechowywanie i dystrybucja obrazów kontenerów w CI/CD
- Skanowanie podatności i podpisywanie artefaktów
- Replikacja multi-region dla wdrożeń globalnych
- Budowa i utrzymanie platformy Kubernetes / cloud native

_Sekcja wygenerowana heurystycznie — popraw według własnego doświadczenia._

## Alternatywy

- [Harbor](/platform/provisioning/provisioning--container-registry--harbor/) — Ta sama subkategoria: Container Registry · CNCF graduated · ⭐ 28,691
- [Dragonfly](/platform/provisioning/provisioning--container-registry--dragonfly/) — Ta sama subkategoria: Container Registry · CNCF graduated · ⭐ 3,205
- [Distribution](/platform/provisioning/provisioning--container-registry--distribution/) — Ta sama subkategoria: Container Registry · CNCF sandbox · ⭐ 10,469
- [zot](/platform/provisioning/provisioning--container-registry--zot/) — Ta sama subkategoria: Container Registry · CNCF sandbox · ⭐ 2,345

## Dokumentacja

- [Strona główna](https://spegel.dev/)

### Repozytoria

- [spegel](https://github.com/spegel-org/spegel)

## OpenAPI

> **TODO:** Pełna specyfikacja w submodule `openapi/provisioning--container-registry--spegel` — aktualizacja przez CI/CD.

| | |
|---|---|
| Status | `todo` |
| Docelowy URL | [/openapi/provisioning--container-registry--spegel/](/openapi/provisioning--container-registry--spegel/) |
| Submodule | `openapi/provisioning--container-registry--spegel` |
| Szukaj w repo | [źródło](https://github.com/spegel-org/spegel/tree/HEAD) |

## Metadane CNCF

| Pole | Wartość |
|------|---------|
| Accepted | — |
| Graduated | — |
| Incubating | — |
| Archived | — |
| CLOMonitor | — |

## GitHub

- Gwiazdki GitHub: **3,680**
- Licencja: **MIT License**
- Tematy: `cloud`, `containerd`, `docker`, `go`, `golang`, `kubernetes`, `oci`, `p2p`, `registry`

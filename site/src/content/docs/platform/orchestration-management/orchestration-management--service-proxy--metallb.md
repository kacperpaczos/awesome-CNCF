---
title: MetalLB
description: "A network load-balancer implementation for Kubernetes using standard routing protocols"
domain: "platform"
category: "Orchestration & Management"
subcategory: "Service Proxy"
project_id: "orchestration-management--service-proxy--metallb"
maturity: "sandbox"
openapi_status: todo
sidebar:
  badge:
    text: Sandbox
    variant: note
---

# MetalLB

![MetalLB](/logos/d19371232c839420223f96327f99332bce52962724a113bd61f3eef10a0bc637.svg)

**Domena:** [Platforma i infrastruktura](../index.md) · **Kategoria:** [Orchestration & Management](index.md) · Service Proxy  
**Open source:** tak

## Opis

A network load-balancer implementation for Kubernetes using standard routing protocols

## Use cases

- MetalLB: A network load-balancer implementation for Kubernetes using standard routing protocols
- Zarządzanie ruchem east-west między mikrousługami
- mTLS, retry i circuit breaking bez zmian w kodzie aplikacji
- Observability L7 (metryki, trace) na poziomie mesh
- Zarządzanie cyklem życia aplikacji w klastrze

_Sekcja wygenerowana heurystycznie — popraw według własnego doświadczenia._

## Alternatywy

- [Envoy](/platform/orchestration-management/orchestration-management--service-proxy--envoy/) — Ta sama subkategoria: Service Proxy · CNCF graduated · ⭐ 28,389
- [Contour](/platform/orchestration-management/orchestration-management--service-proxy--contour/) — Ta sama subkategoria: Service Proxy · CNCF incubating · ⭐ 3,931
- [BFE](/platform/orchestration-management/orchestration-management--service-proxy--bfe/) — Ta sama subkategoria: Service Proxy · CNCF sandbox · ⭐ 6,247
- [LoxiLB](/platform/orchestration-management/orchestration-management--service-proxy--loxilb/) — Ta sama subkategoria: Service Proxy · CNCF sandbox · ⭐ 1,856

## Dokumentacja

- [Strona główna](https://metallb.universe.tf)
- [DevStats CNCF](https://metallb.devstats.cncf.io/)
- [Slack](https://slack.k8s.io/)
- [Artwork](https://github.com/cncf/artwork/tree/master/projects/metallb)
- [Annual review](https://github.com/cncf/toc/pull/942)

### Repozytoria

- [metallb](https://github.com/metallb/metallb)

## OpenAPI

> **TODO:** Pełna specyfikacja w submodule `openapi/orchestration-management--service-proxy--metallb` — aktualizacja przez CI/CD.

| | |
|---|---|
| Status | `todo` |
| Docelowy URL | [/openapi/orchestration-management--service-proxy--metallb/](/openapi/orchestration-management--service-proxy--metallb/) |
| Submodule | `openapi/orchestration-management--service-proxy--metallb` |
| Szukaj w repo | [źródło](https://github.com/metallb/metallb/tree/HEAD) |

## Metadane CNCF

| Pole | Wartość |
|------|---------|
| Accepted | 2021-09-14 |
| Graduated | — |
| Incubating | — |
| Archived | — |
| CLOMonitor | metallb |

## GitHub

- Gwiazdki GitHub: **8,230**
- Licencja: **Apache License 2.0**
- Tematy: `arp`, `bare-metal`, `bgp`, `frr`, `hacktoberfest`, `keepalived`, `kubernetes`, `load-balancer`, `vrrp`

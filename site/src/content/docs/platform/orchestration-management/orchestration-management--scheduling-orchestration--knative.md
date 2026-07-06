---
title: Knative
description: "Knative is a developer-focused serverless application layer which is a great complement to the existing Kubernetes application constructs. Knative consists of three components: an HTTP-triggered auto…"
domain: "platform"
category: "Orchestration & Management"
subcategory: "Scheduling & Orchestration"
project_id: "orchestration-management--scheduling-orchestration--knative"
maturity: "graduated"
openapi_status: todo
sidebar:
  badge:
    text: Graduated
    variant: success
---

# Knative

![Knative](/logos/6a1b7572490f95cada1836b3e0f932e5ff10c683bc1167b08ff868fb7867cfd5.svg)

**Domena:** [Platforma i infrastruktura](../index.md) · **Kategoria:** [Orchestration & Management](index.md) · Scheduling & Orchestration  
**Open source:** tak

## Opis

Knative is a developer-focused serverless application layer which is a great complement to the existing Kubernetes application constructs. Knative consists of three components: an HTTP-triggered autoscaling container runtime called “Knative Serving”, a CloudEvents-over-HTTP asynchronous routing layer called “Knative Eventing”, and a developer-focused function framework which leverages the Serving and Eventing components, called "Knative Functions".

## Use cases

- Knative: Knative is a developer-focused serverless application layer which is a great complement to the existing Kubernetes application constructs. Knative consists of three components: an HTTP-triggered autoscaling container runtime called “Knative Serving”, a CloudEvents-over-HTTP asynchronous routing layer called “Knative Eventing”, and a developer-focused function framework which leverages the Serving and Eventing components, called "Knative Functions"
- Orkiestracja kontenerów w skali produkcyjnej
- Autoscaling i self-healing workloadów
- Multi-tenant platformy wewnętrznego developer experience
- Zarządzanie cyklem życia aplikacji w klastrze

_Sekcja wygenerowana heurystycznie — popraw według własnego doświadczenia._

## Alternatywy

- [Kubernetes](/platform/orchestration-management/orchestration-management--scheduling-orchestration--kubernetes/) — Ta sama subkategoria: Scheduling & Orchestration · CNCF graduated · ⭐ 122,997
- [Crossplane](/platform/orchestration-management/orchestration-management--scheduling-orchestration--crossplane/) — Ta sama subkategoria: Scheduling & Orchestration · CNCF graduated · ⭐ 11,763
- [KEDA](/platform/orchestration-management/orchestration-management--scheduling-orchestration--keda/) — Ta sama subkategoria: Scheduling & Orchestration · CNCF graduated · ⭐ 10,283
- [Kubeflow](/platform/orchestration-management/orchestration-management--scheduling-orchestration--kubeflow/) — Ta sama subkategoria: Scheduling & Orchestration · CNCF incubating · ⭐ 15,721

## Dokumentacja

- [Strona główna](https://knative.dev)
- [DevStats CNCF](https://knative.devstats.cncf.io/)
- [Slack](https://slack.cncf.io)
- [Artwork](https://github.com/knative/docs/tree/main/docs/images/logo)

### Repozytoria

- [serving](https://github.com/knative/serving)

## OpenAPI

> **TODO:** Pełna specyfikacja w submodule `openapi/orchestration-management--scheduling-orchestration--knative` — aktualizacja przez CI/CD.

| | |
|---|---|
| Status | `todo` |
| Docelowy URL | [/openapi/orchestration-management--scheduling-orchestration--knative/](/openapi/orchestration-management--scheduling-orchestration--knative/) |
| Submodule | `openapi/orchestration-management--scheduling-orchestration--knative` |
| Szukaj w repo | [źródło](https://github.com/knative/serving/tree/HEAD) |

## Metadane CNCF

| Pole | Wartość |
|------|---------|
| Accepted | 2022-03-02 |
| Graduated | 2025-09-11 |
| Incubating | 2022-03-02 |
| Archived | — |
| CLOMonitor | knative |

## GitHub

- Gwiazdki GitHub: **6,057**
- Licencja: **Apache License 2.0**
- Tematy: `app`, `autoscaler`, `container`, `developer-productivity`, `function`, `knative`, `kubernetes`, `networking`, `scale`, `serverless`, `serverless-containers`

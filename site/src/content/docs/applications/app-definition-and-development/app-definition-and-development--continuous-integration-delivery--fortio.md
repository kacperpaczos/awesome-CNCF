---
title: Fortio
description: "Fortio is an open source load testing library, command-line tool, and server application written in Go. Originated as Istio's performance characterization tool (in particular proxy overhead), Fortio …"
domain: "applications"
category: "App Definition and Development"
subcategory: "Continuous Integration & Delivery"
project_id: "app-definition-and-development--continuous-integration-delivery--fortio"
maturity: null
openapi_status: todo
---

# Fortio

![Fortio](/logos/f2cbb9484bb193e51dd214344e1c3a2d1a21e0b320ca0765e0f2af6e6ae936ba.svg)

**Domena:** [Aplikacje i delivery](../index.md) · **Kategoria:** [App Definition and Development](index.md) · Continuous Integration & Delivery  
**Open source:** tak

## Opis

Fortio is an open source load testing library, command-line tool, and server application written in Go. Originated as Istio's performance characterization tool (in particular proxy overhead), Fortio has evolved into a versatile tool for load testing and performance benchmarking of HTTP, gRPC, and TCP services. Among other options it enables users to generate a specified query-per-second (QPS) load and records detailed latency histograms, facilitating the analysis of performance metrics. The server component offers a straightforward web UI and REST API, allowing users to initiate tests and visualize results through graphical representations. Beyond load testing, Fortio provides server-side features akin to httpbin, including request echoing with headers, configurable latency or error responses, TCP echoing and proxying, HTTP fan-out, and support for gRPC echo and health checks. These capabilities make Fortio a versatile tool for debugging and testing high-performance services in cloud-native environments. As an organization set of git repositories, is also a growing set of reusable libraries for writing Cloud Native Go code and CLIs.

## Use cases

- Fortio: Fortio is an open source load testing library, command-line tool, and server application written in Go. Originated as Istio's performance characterization tool (in particular proxy overhead), Fortio has evolved into a versatile tool for load testing and performance benchmarking of HTTP, gRPC, and TCP services. Among other options it enables users to generate a specified query-per-second (QPS) load and records detailed latency histograms, facilitating the analysis of performance metrics. The server component offers a straightforward web UI and REST API, allowing users to initiate tests and visualize results through graphical representations. Beyond load testing, Fortio provides server-side features akin to httpbin, including request echoing with headers, configurable latency or error responses, TCP echoing and proxying, HTTP fan-out, and support for gRPC echo and health checks. These capabilities make Fortio a versatile tool for debugging and testing high-performance services in cloud-native environments. As an organization set of git repositories, is also a growing set of reusable libraries for writing Cloud Native Go code and CLIs
- Definicja i pakowanie aplikacji cloud native
- Przyspieszenie developer loop (build, deploy, debug)
- Ekosystem / tag: `go` — typowe wdrożenia wokół Fortio
- Ekosystem / tag: `golang` — typowe wdrożenia wokół Fortio

_Sekcja wygenerowana heurystycznie — popraw według własnego doświadczenia._

## Alternatywy

- [Argo](/applications/app-definition-and-development/app-definition-and-development--continuous-integration-delivery--argo/) — Ta sama subkategoria: Continuous Integration & Delivery · CNCF graduated · ⭐ 23,124
- [Flux](/applications/app-definition-and-development/app-definition-and-development--continuous-integration-delivery--flux/) — Ta sama subkategoria: Continuous Integration & Delivery · CNCF graduated · ⭐ 8,185
- [OpenKruise](/applications/app-definition-and-development/app-definition-and-development--continuous-integration-delivery--openkruise/) — Ta sama subkategoria: Continuous Integration & Delivery · CNCF incubating · ⭐ 5,267
- [werf](/applications/app-definition-and-development/app-definition-and-development--continuous-integration-delivery--werf/) — Ta sama subkategoria: Continuous Integration & Delivery · CNCF sandbox · ⭐ 4,694

## Dokumentacja

- [Strona główna](https://fortio.org/)

### Repozytoria

- [fortio](https://github.com/fortio/fortio)

## OpenAPI

> **TODO:** Pełna specyfikacja w submodule `openapi/app-definition-and-development--continuous-integration-delivery--fortio` — aktualizacja przez CI/CD.

| | |
|---|---|
| Status | `todo` |
| Docelowy URL | [/openapi/app-definition-and-development--continuous-integration-delivery--fortio/](/openapi/app-definition-and-development--continuous-integration-delivery--fortio/) |
| Submodule | `openapi/app-definition-and-development--continuous-integration-delivery--fortio` |
| Szukaj w repo | [źródło](https://github.com/fortio/fortio/tree/HEAD) |

## Metadane CNCF

| Pole | Wartość |
|------|---------|
| Accepted | — |
| Graduated | — |
| Incubating | — |
| Archived | — |
| CLOMonitor | — |

## GitHub

- Gwiazdki GitHub: **3,700**
- Licencja: **Apache License 2.0**
- Tematy: `go`, `golang`, `golang-application`, `golang-library`, `grpc`, `http`, `performance`, `performance-testing`, `performance-visualization`, `proxy`, `stress-testing`

---
title: Pipelock
description: "Pipelock is an open-source AI agent firewall. It sits between AI agents and the internet and blocks secret leaks (DLP), SSRF, unsafe tool traffic, and prompt-injection content across HTTP, WebSocket,…"
domain: "platform"
category: "Provisioning"
subcategory: "Security & Compliance"
project_id: "provisioning--security-compliance--pipelock"
maturity: null
openapi_status: todo
---

# Pipelock

![Pipelock](/logos/0d291a4ab4c45d39ee04ff1b389d7f83ecf13c05bf739690b328d92ced99a2ee.svg)

**Domena:** [Platforma i infrastruktura](../index.md) · **Kategoria:** [Provisioning](index.md) · Security & Compliance  
**Open source:** tak

## Opis

Pipelock is an open-source AI agent firewall. It sits between AI agents and the internet and blocks secret leaks (DLP), SSRF, unsafe tool traffic, and prompt-injection content across HTTP, WebSocket, and MCP transports. It adds MCP-specific defenses for tool-baseline drift and rug-pull detection, and supports Ed25519-signed action receipts plus Audit Packet v0 bundles that can be verified offline with a standalone Go verifier and TypeScript, Rust, and Python verifier ports. Single Go binary, fail-closed defaults, Apache 2.0.

## Use cases

- Pipelock: Pipelock is an open-source AI agent firewall. It sits between AI agents and the internet and blocks secret leaks (DLP), SSRF, unsafe tool traffic, and prompt-injection content across HTTP, WebSocket, and MCP transports. It adds MCP-specific defenses for tool-baseline drift and rug-pull detection, and supports Ed25519-signed action receipts plus Audit Packet v0 bundles that can be verified offline with a standalone Go verifier and TypeScript, Rust, and Python verifier ports. Single Go binary, fail-closed defaults, Apache 2.0
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

- [Strona główna](https://pipelab.org)

### Repozytoria

- [pipelock](https://github.com/luckyPipewrench/pipelock)

## OpenAPI

> **TODO:** Pełna specyfikacja w submodule `openapi/provisioning--security-compliance--pipelock` — aktualizacja przez CI/CD.

| | |
|---|---|
| Status | `todo` |
| Docelowy URL | [/openapi/provisioning--security-compliance--pipelock/](/openapi/provisioning--security-compliance--pipelock/) |
| Submodule | `openapi/provisioning--security-compliance--pipelock` |
| Szukaj w repo | [źródło](https://github.com/luckyPipewrench/pipelock/tree/HEAD) |

## Metadane CNCF

| Pole | Wartość |
|------|---------|
| Accepted | — |
| Graduated | — |
| Incubating | — |
| Archived | — |
| CLOMonitor | — |

## GitHub

- Gwiazdki GitHub: **706**
- Licencja: **Apache License 2.0**
- Tematy: `agent-security`, `ai-agent-security`, `ai-agents`, `ai-firewall`, `ai-security`, `dlp`, `egress-proxy`, `fetch-proxy`, `github-action`, `golang`, `integrity-monitoring`, `llm-security`, `mcp`, `mcp-security`, `prompt-injection`, `security`, `security-scanning`, `security-tools`, `ssrf`, `ssrf-protection`

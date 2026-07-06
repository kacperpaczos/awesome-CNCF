---
title: Kubewarden
description: "Kubewarden is a Policy Engine powered by WebAssembly policies. Its policies can be written in CEL, Rego (OPA & Gatekeeper flavours), Rust, Go, YAML, and others. Kubewarden simplifies Policy-As-Code b…"
domain: "platform"
category: "Provisioning"
subcategory: "Security & Compliance"
project_id: "provisioning--security-compliance--kubewarden"
maturity: "sandbox"
openapi_status: todo
sidebar:
  badge:
    text: Sandbox
    variant: note
---

# Kubewarden

![Kubewarden](/logos/24207e926905a8f8a35dce3be43c4da4f8d9e8edea46b2beb3c319d6857b8e7a.svg)

**Domena:** [Platforma i infrastruktura](../index.md) · **Kategoria:** [Provisioning](index.md) · Security & Compliance  
**Open source:** tak

## Opis

Kubewarden is a Policy Engine powered by WebAssembly policies. Its policies can be written in CEL, Rego (OPA & Gatekeeper flavours), Rust, Go, YAML, and others. Kubewarden simplifies Policy-As-Code by allowing policy authors and consumers to use their preferred tooling and stack, develop and test policies out of cluster. 

## Use cases

- Kubewarden: Kubewarden is a Policy Engine powered by WebAssembly policies. Its policies can be written in CEL, Rego (OPA & Gatekeeper flavours), Rust, Go, YAML, and others. Kubewarden simplifies Policy-As-Code by allowing policy authors and consumers to use their preferred tooling and stack, develop and test policies out of cluster
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

- [Strona główna](https://www.kubewarden.io)
- [DevStats CNCF](https://kubewarden.devstats.cncf.io/)
- [Blog](https://kubewarden.io/blog)
- [Slack](https://kubernetes.slack.com/)
- [Artwork](https://github.com/cncf/artwork/tree/master/projects/kubewarden)

### Repozytoria

- [kubewarden-controller](https://github.com/kubewarden/kubewarden-controller)
- [policy-server](https://github.com/kubewarden/policy-server)
- [kwctl](https://github.com/kubewarden/kwctl)
- [audit-scanner](https://github.com/kubewarden/audit-scanner)
- [community](https://github.com/kubewarden/community)

## OpenAPI

> **TODO:** Pełna specyfikacja w submodule `openapi/provisioning--security-compliance--kubewarden` — aktualizacja przez CI/CD.

| | |
|---|---|
| Status | `todo` |
| Docelowy URL | [/openapi/provisioning--security-compliance--kubewarden/](/openapi/provisioning--security-compliance--kubewarden/) |
| Submodule | `openapi/provisioning--security-compliance--kubewarden` |
| Szukaj w repo | [źródło](https://github.com/kubewarden/kubewarden-controller/tree/HEAD) |

## Metadane CNCF

| Pole | Wartość |
|------|---------|
| Accepted | 2022-06-17 |
| Graduated | — |
| Incubating | — |
| Archived | — |
| CLOMonitor | kubewarden |

## GitHub

- Gwiazdki GitHub: **230**
- Licencja: **Apache License 2.0**
- Tematy: `hacktoberfest`, `kubernetes`, `kubernetes-security`, `policy-as-code`, `webassembly`

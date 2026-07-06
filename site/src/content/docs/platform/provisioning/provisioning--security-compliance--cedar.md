---
title: Cedar
description: "Cedar is an open source authorization policy language that enables developers to express fine-grained permissions as easy-to-understand policies enforced in their applications, and decouple access co…"
domain: "platform"
category: "Provisioning"
subcategory: "Security & Compliance"
project_id: "provisioning--security-compliance--cedar"
maturity: "sandbox"
openapi_status: todo
sidebar:
  badge:
    text: Sandbox
    variant: note
---

# Cedar

![Cedar](/logos/86477490a2670f3b7cb7e89ac64d76e66bf7c4516daf3e69c8cf742632d0f664.svg)

**Domena:** [Platforma i infrastruktura](../index.md) · **Kategoria:** [Provisioning](index.md) · Security & Compliance  
**Open source:** tak

## Opis

Cedar is an open source authorization policy language that enables developers to express fine-grained permissions as easy-to-understand policies enforced in their applications, and decouple access control from application logic. Cedar is designed to be ergonomic, fast, safe, and analyzable using automated reasoning. Cedar's simple and intuitive syntax supports common authorization use-cases with readable policies, naturally expressing concepts from role-based, attribute-based, and relation-based access control models. Cedar's policy structure enables authorization requests to be decided quickly. Its policy validator uses optional typing to help policy writers avoid mistakes, but not get in their way. Cedar's design has been finely balanced to allow for a sound, complete, and decidable logical encoding, which enables precise automated analysis of Cedar policies, e.g., to ensure that policy refactoring preserves existing permissions. Cedar's language specification has been formally verified using a theorem prover to satisfy key security properties like "deny trumps allow," and its implementation in Rust undergoes rigorous differential random testing against its formal specification. By combining mathematical rigor with developer-friendly design, Cedar offers a practical approach to secure, maintainable authorization for modern applications.

## Use cases

- Cedar: Cedar is an open source authorization policy language that enables developers to express fine-grained permissions as easy-to-understand policies enforced in their applications, and decouple access control from application logic. Cedar is designed to be ergonomic, fast, safe, and analyzable using automated reasoning. Cedar's simple and intuitive syntax supports common authorization use-cases with readable policies, naturally expressing concepts from role-based, attribute-based, and relation-based access control models. Cedar's policy structure enables authorization requests to be decided quickly. Its policy validator uses optional typing to help policy writers avoid mistakes, but not get in their way. Cedar's design has been finely balanced to allow for a sound, complete, and decidable logical encoding, which enables precise automated analysis of Cedar policies, e.g., to ensure that policy refactoring preserves existing permissions. Cedar's language specification has been formally verified using a theorem prover to satisfy key security properties like "deny trumps allow," and its implementation in Rust undergoes rigorous differential random testing against its formal specification. By combining mathematical rigor with developer-friendly design, Cedar offers a practical approach to secure, maintainable authorization for modern applications
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

- [Strona główna](https://cedarpolicy.com)

### Repozytoria

- [cedar](https://github.com/cedar-policy/cedar)
- [cedar-access-control-for-k8s](https://github.com/cedar-policy/cedar-access-control-for-k8s)

## OpenAPI

> **TODO:** Pełna specyfikacja w submodule `openapi/provisioning--security-compliance--cedar` — aktualizacja przez CI/CD.

| | |
|---|---|
| Status | `todo` |
| Docelowy URL | [/openapi/provisioning--security-compliance--cedar/](/openapi/provisioning--security-compliance--cedar/) |
| Submodule | `openapi/provisioning--security-compliance--cedar` |
| Szukaj w repo | [źródło](https://github.com/cedar-policy/cedar/tree/HEAD) |

## Metadane CNCF

| Pole | Wartość |
|------|---------|
| Accepted | 2025-10-08 |
| Graduated | — |
| Incubating | — |
| Archived | — |
| CLOMonitor | cedar |

## GitHub

- Gwiazdki GitHub: **1,546**
- Licencja: **Apache License 2.0**

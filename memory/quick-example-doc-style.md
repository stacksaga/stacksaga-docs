---
name: quick-example-doc-style
description: How the user wants StackSaga quick-example tutorial docs refined — structure, depth, and consistency checklist
metadata:
  type: feedback
---

When asked to "refine / make nicer" a StackSaga quick-example tutorial doc (under `docs/modules/demo/pages/.../*-quick-example.adoc`), the user wants it brought to a rich, consistent standard — not just light copy-editing.

**Why:** The user explicitly asked, on two separate docs (the Kafka/async and the synchronous MySQL quick examples), to turn "bit less described" docs into "the best one with good details," and to do the second "in the same way" as the first. They value depth, accuracy, and parity between the sync and Kafka variants.

**How to apply:**
- Add `:description:` / `:keywords:` attributes and verify the `= Title` is correct (these docs had **swapped sync/Kafka titles**; the nav uses empty `xref:...[]` link text, so the title is also the nav label).
- Add/expand an **Overview** with a table of the spans/executors (step → type Query/Command → target → compensation) and, for Kafka, a services-and-roles table + message-flow list.
- Add a Stage-1 **table of contents** (`. xref:#anchor[]`), adding any missing section anchors.
- Cross-link the sync and Kafka variants to each other; point "read more" xrefs at the matching engine's reference docs (sync→`stacksaga-sync/...`, Kafka→`stacksaga-kafka-implementation/...`).
- Prerequisites: Kafka example needs a broker; sync example needs only MySQL. Add a Docker tip.
- Add a runnable `curl` to the "Running" section and label outcomes "Happy path" / "Compensation path".
- **Verify example code against the reference docs and fix bugs** — the Kafka doc had real ones (missing `SagaPrimaryEventAction.complete()` branch in `onNext`; reading `"amount"` instead of `"total_amount"`; no failure simulation so compensation never fired). Flag dependency concerns (e.g. the non-existent `spring-boot-starter-kafka` artifact) rather than silently changing build files.
- Template class names: synchronous engine uses `SagaTemplate` / `ReactiveSagaTemplate`; Kafka uses `StackSagaKafkaTemplate`.

The two quick-example files are linked from [[stacksaga-docs-overview]]'s `docs/modules/demo/nav.adoc`.

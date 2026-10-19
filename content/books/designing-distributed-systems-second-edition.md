---
title: 'Designing Distributed Systems, Second Edition'
date: '2026-10-19T10:00:00+00:00'
draft: false
tags:
- Books
url: /books/designing-distributed-systems
cover:
  image: /images/designing-distributed-systems-second-edition/designing-distributed-systems-2nd-edition.jpg
  alt: 'Designing Distributed Systems, Second Edition'
  relative: true
---

[O'Reilly book page](https://www.oreilly.com/library/view/designing-distributed-systems/9781098156343/)

[Amazon](https://www.amazon.com/dp/1098156358)

[Designing Distributed Systems (first edition, available for free download by Microsoft)](https://info.microsoft.com/rs/157-GQE-382/images/EN-CNTNT-eBook-DesigningDistributedSystems.pdf)


## **"Designing Distributed Systems: Patterns and Paradigms for Scalable, Reliable Systems Using Kubernetes"** (2nd Edition) by Brendan Burns

Brendan Burns, co-founder of Kubernetes, argues that distributed systems should be built the way object-oriented software is: from **well-known, reusable patterns** instead of from scratch every time. Using containers and Kubernetes as the building blocks, the book gives developers and architects a shared vocabulary (sidecar, ambassador, sharding, scatter/gather, work queue...) to describe, design and reason about reliable systems. The second edition (O'Reilly, December 2024) updates the original material and adds new chapters on **AI inference and training**, **monitoring and observability**, and **common failure patterns** seen in real-world systems.

### Foundations

* **Introduction:** Why patterns matter. Just as design patterns standardized object-oriented programming, distributed system patterns let teams reuse proven solutions, share components and communicate designs quickly.
* **Important Distributed System Concepts:** The base vocabulary used through the book: APIs and RPC, latency, reliability and availability, idempotency, delivery semantics, data consistency and orchestration.

### Single-Node Patterns

Patterns for grouping multiple containers that are scheduled together on the same machine (a Kubernetes Pod).

* **The Sidecar Pattern:** A helper container that extends or enhances the main application without changing it, e.g. adding HTTPS, dynamic configuration or a management UI to a legacy service.
* **Ambassadors:** A container that proxies the communication between the application and the outside world. Used to hide sharding from the client, do service brokering, or run experiments and request splitting.
* **Adapters:** A container that transforms the application's output into a standard interface, e.g. normalizing metrics, logging and health monitoring so heterogeneous apps look the same to the rest of the system.

### Serving Patterns

Multi-node patterns for building long-running, scalable services.

* **Replicated Load-Balanced Services:** Stateless replicas behind a load balancer, readiness probes, session tracking, and adding a caching layer to improve performance.
* **Sharded Services:** Splitting state across shards when the data no longer fits on one node. Covers sharding functions, consistent hashing, hot shards and sharded, replicated serving.
* **Scatter/Gather:** Fan a request out to many leaves in parallel and merge the results (like a distributed search), and the trade-offs between parallelism, tail latency and the number of leaves.
* **Functions and Event-Driven Processing:** When FaaS/serverless fits (and when it doesn't), and patterns such as decorators, event handlers and event-based pipelines.
* **Ownership Election:** Leader election and distributed locks, how to implement them with consensus stores like etcd, and how to handle lease renewal and concurrent data manipulation safely.

### Batch Computational Patterns

* **Work Queue Systems:** A generic queue with pluggable source and worker containers, dynamic scaling of workers, and the multi-worker pattern.
* **Event-Driven Batch Processing:** Chaining work queues into workflows with patterns like copier, filter, splitter and sharder, often on top of a publish/subscribe infrastructure.
* **Coordinated Batch Processing:** Join (barrier synchronization) and reduce patterns, plus examples such as counting, summing and building histograms in a MapReduce style.

### New in the Second Edition

* **Monitoring and Observability Patterns:** Logging, metrics, alerting, distributed tracing and aggregation, and how to make a distributed system understandable when things go wrong.
* **AI Inference and Serving:** How the same patterns apply to modern AI workloads: serving model inference at scale, and the specific needs of training and serving AI models in a distributed environment.
* **Common Failure Patterns:** Building robust systems for the real world: recurring mistakes and failure modes seen in production distributed systems, and how to recognize and avoid them.

### Conclusion: A New Beginning?

Burns closes by stressing that these patterns are a starting point: by building on shared, reusable components, the industry can move from handcrafting every distributed system to assembling them from reliable, well-understood pieces.

This book is short, practical and easy to read. It is especially useful for engineers working with Kubernetes and microservices who want a clear mental catalog of patterns to apply when designing scalable and reliable systems.

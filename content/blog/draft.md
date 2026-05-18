---
date: '2026-05-18T09:07:11+00:00'
draft: true
---

# Reliable Micro-Services (and not micro) Communication

- How I'm sure inter-services communications always are properly handled (or at least, the error is escalated)?
- Happy path is Client -> Service A -> Service B. Done! Both services updated their DBs and are in sync.
- But what happens when there is an error in the middle?
- Let's talk about it!

## When this is important
- We need this depending on the app requirement
  - Example: when it is required, bank operation, booking system,...
  - Example: when it is not: live metric, streaming, etc...
 
## Protocols (service communication protocols)
- HTTP
- Async Messages (Pub-sub)
- 

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
  - Example: when it is not: live metric, streaming, etc..., or just the chances this to happen is so low that we can live with that and just looking at the logs and manual interventions (or reconciliation process is enough)
 
## Protocols (service communication protocols)
- Sync: HTTP, gRPC, Webhooks...
- Async: Queue Messages (Pub-sub), Webhooks, Pooling...
- Will be focusing in HTTP and MessageQueues...

## Idempotency
- It is a quality of an action or function. Given the same input the outcome is always the same.
- For example an update action is intrinsically, the same commando will update the record in the same way. (Unless there are side affects like DB triggers, saving update time,...)
- In distributed system it is important most actions be idempotent, because when error happen, usually the action is retried, and if it was already processed is skipped with no side-effects.
- For example, the action x+=1 is not idempotent. The output depends on the value of x at the moment of triggering the action.
- For example, we could send the message with a unique idempotency-id Action(510412323, x+=1) and the receiver need to save the id in a persistent storage and check if it was already inserted (for example unique constraint in database). Other option is to use a timestamp, and always check the previous latest update is older than the new action timestamp.

## Queues
- Sender -> Message Broker -> Listener
- What happen when error occurs in the Listener
  - There is a critical error and the service shutdown unexpectedly:
    - There is no ACK from the message consumer (Explain what is ACK)
    - There is timeout (for this message) in the message broker since it hasn't been processed
    - The message is available again so other consumer can take it
    - Important: Listener handler should be idempotent.
  - There is an application error:
    - For example calling Http service returns an error, saving to DB error, DB or service down, unexpected error.
    - The message is marked as failed to process. Typically something like a Deadletter Queue or something equivalent. This will require manual intervention, so we should have metrics and alerts to monitor the these deadletter queues, and send notification to the person in action.
    - After the situation is fixed, the message is sent back to the queue, notice idempotency importance.
- No errors. All good, the message is ACKed.

## Http
- Service A -> HTTP Message -> Service B
- What happens when an error occurs in Service B (It is down, error in dependant services, application error)
  - The Service A will get a HTTP error (not success response). It is the only option. Interesting here is what we can do with this error.
- What Service A we can do with the HTTP error:
  - It is an expected application error, and knows what to do (example, validation error, should trigger action)
  - It is an un-expected error (network issues, services down)
    - Retry. Some time it is just a transient issue, and just retrying it is enough. We need to define the amount of retries we usually need and the delay between each retry (for example use Fibonacci number)
    - Turn on circuit breaker. If we've got this error many time, it is a good idea stop sending request for a while and fail earlier.
    - Log and propagate back. This will depends on how the action in service A was started:
      - Queue message processor:
        - Deadletter
      - Http request handler:
        - Return http error response
      - Recurring background process:
        - Usually its an action that process records pending to process:
          - Let the record in a non-processed state
          - Or move the error to failed to process state.




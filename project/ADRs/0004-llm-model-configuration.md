# LLM-0004 LLM model configuration

## Context

In order to benchmark LLM models we need to standardize the configuration of an LLM model submission. To do this
effectively we need to standardize the benchmarks and LLM model submission.

## Assumptions

- We run the LLM in kubernetes
- Models are either API endpoints or Git repositories.

## Decision

We will create our own standard for configuring LLMs.

The reason for this is that the impact is relatively small if we abstract away the LLM config and allow for extension without
breaking backward compatibility.

## Consequences

If a standard rises for configuring LLMs we may need to break backward compatibility to adhere to the standard.

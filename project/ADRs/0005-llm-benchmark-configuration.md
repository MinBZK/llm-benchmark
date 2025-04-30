# LLM-0005 LLM benchmark configuration

## Context

In order to benchmark LLM models we need to standardize the configuration of running the benchmarks against the model.
To do this effectively we need to standardize the benchmarks configuration.

## Assumptions

* We run the LLM in kubernetes
* Benchmarks are stored in git
* LLM models are stored in git
* Contributors can add new benchmarks

## Decision

For a benchmarking configuration we can look at implementations of GLUE, SUPERGLUE and EXTREME frameworks. We will
create a standard schema based on these implementations.

## Consequences

Not all benchmarks will be runnable.

## More Information

OpenCompass.org.cn contains a nice reference.

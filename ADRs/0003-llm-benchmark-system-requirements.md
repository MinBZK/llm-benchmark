# LLM-0003 LLM Benchmark System Requirements

## Context

This document contains the design decisions behind the LLM Benchmarks and which greatly impact the solution of the LLM
Benchmarks Tool. It is closely related to the ADR about the 0002 LLM Runtime Framework.

## Assumptions

We assume:
- The LLM Runtime has been decided in ADR LLM-0002
- The main clients are (but not exclusive to) from the Dutch Government
- Open-source solutions are preferred to align with our principles.

## Decision

The requirements of the solution are:

- We should be able to version the model in consideration (be this through external repositories or taking hashes)
- We seek the collaboration with [DUMB](https://dumbench.nl/) as this is closely related to what we want
- The preferable entrance would be that people have their model versioned through version control and published via
the [Dutch Algorithm Register](https://algoritmes.overheid.nl/nl)
    - In this way people would only need to provide the link to the model on the register and our solution would do the
    rest, the results of the benchmarks would also be posted on the Algorithm Register
- There should be an online version hosted by the ai-validation team for easy access and to promote transparency
    - This should be scalable as downloading models and verifying them could take a long time especially when supplying
    many people
- An open LLM Benchmark dashboard like [Huggingface](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) 
should be part of the LLM Benchmark System
- The LLM Benchmark Should not only Benchmark Dutch LLMs but also state-of-the-art International LLMs for comparison
- People should be able to run the LLM Benchmark system on the company's (internal) organizational resources
    - When the BIO does not allow the model to leave the digital organizational boundary

## Consequences

The consequences of these decisions are that we have an architectural diagram as proposed in [system_diagram.mmd](..%2FDocs%2Fsystem_diagram.mmd)

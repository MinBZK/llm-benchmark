# LLM-0002 LLM serving framework

## Context

Various ML frameworks are utilized within the LLM community for training, with PyTorch and TensorFlow being the most
prevalent. Our infrastructure for LLM benchmarking is already established, employing Kubernetes for LLM execution
and FLUX for seamless deployment onto Kubernetes clusters. Containerization of LLMs is essential for their deployment
and operation within the Kubernetes environment. Their currently is no standard on how to serve LLMs. We want to
standardize our servings of LLM frameworks to make benchmarking easier.

## Assumptions

We assume:

- Open-source solutions are preferred to align with our principles.
- The ease of serving LLMs is a key consideration.
- REST APIs over HTTPS are preferred for communication.
- Three types of LLM submissions for serving: API, GitHub Repo, HuggingFace.
- Parallel Inference capabilities are essential
- Documentation must be provided in English

## Decision

We will use Langchain with FastAPI.

After evaluating several tools, including Tensorflow Serving, FastAPI, RayLLM, KServe, Kubeflow, Streamlit, Gradio,
LangChain, Mosec, Seldon, OpenLLM, UbiOps and vLLM, we have decided to use Langchain with FastAPI. This decision is
based on the robust community support and the right balance between flexibility and simplicity, which will enable us
to minimize development time for running models.

## Consequences

The consequence of this decision is that we are limited to Python for serving LLMs. This limitation may impact future
integration efforts with non-Python technologies.

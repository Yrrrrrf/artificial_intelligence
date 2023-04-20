# [Prompt Engineering](https://www.promptingguide.ai/introduction/elements)

Is the process of designing prompts to elicit a desired response from a model. This is a key part of the model development process, and is often the most time-consuming part of the process. The goal of prompt engineering is to create a prompt that will elicit a response that is useful for the task at hand. This can be a difficult task, and there is no one-size-fits-all approach. The following sections describe some of the considerations that should be taken into account when designing a prompt.


## Promts Structure

Prompts are structured as a sequence of tokens. The first token is always the prompt prefix, which is a special token that is used to indicate the start of the prompt. The prompt prefix is used to distinguish the prompt from the context, and is used to separate the prompt from the context when the model generates a response. The prompt prefix is always the same for a given model, and is not included in the prompt vocabulary. The prompt prefix for GPT-3 is `Prompt:`.

```mermaid
graph LR

A[Intruciton] --> B[Context]
B --> C[Inputs]
C --> D[Outputs]
```
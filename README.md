#Diffusion Steering via Reinforcement Learning for Improved Image Generation

---
 
## Motivation and Overview

Despite strong performance, open-source diffusion models often fail on tasks requiring fine-grained structural or semantic accuracy. Common failure modes include:
- anatomically incorrect hands and fingers,
- poor spatial reasoning in compositional prompts,
- and illegible or distorted text rendering.

These errors arise in part because diffusion models are trained with pixel- or latent-space objectives that do not directly optimize for downstream perceptual or task-specific correctness.

We propose using Diffusion Steering Reinforcement Learning (DSRL) to improve generation quality by learning a policy over the diffusion initialization process. Specifically, we optimize the starting noise using reward signals aligned with task-specific objectives.

While DSRL has primarily been explored in robotics for policy improvement, we investigate its application to diffusion models, demonstrating that it can improve performance on practical image generation tasks.

---
 
## Potential Target Tasks

### Text-in-Image Generation

We focus on the task of generating images containing legible text, a well-known weakness of diffusion models. Existing models frequently produce distorted, misspelled, or unreadable text even when the prompt specifies exact strings.

To address this, we define a reward function using an optical character recognition (OCR) model. Given a prompt specifying a target string, we:

1. Generate an image using the diffusion model.
2. Apply OCR to extract the predicted text.
3. Compute a reward based on similarity to the target string.

We experiment with reward formulations including:
- edit distance between predicted and target text,
- exact match accuracy,

This provides a dense, automatic supervision signal that directly reflects the model’s ability to render legible text, enabling reinforcement learning over the diffusion initialization process.

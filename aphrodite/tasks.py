from typing import Literal, get_args

GenerationTask = Literal["generate", "transcription"]
GENERATION_TASKS = get_args(GenerationTask)

PoolingTask = Literal["encode", "embed", "classify", "score"]
POOLING_TASKS = get_args(PoolingTask)

VAETask = Literal["vae_encode", "vae_decode"]
VAE_TASKS = get_args(VAETask)

SupportedTask = Literal[GenerationTask, PoolingTask, VAETask]

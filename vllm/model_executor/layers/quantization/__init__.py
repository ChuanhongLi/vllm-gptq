from typing import Type

from vllm.model_executor.layers.quantization.awq import AWQConfig
from vllm.model_executor.layers.quantization.base_config import (
    QuantizationConfig)
from vllm.model_executor.layers.quantization.awq import AWQConfig
from vllm.model_executor.layers.quantization.exl2 import Exl2Config
from vllm.model_executor.layers.quantization.gguf import GGUFConfig
from vllm.model_executor.layers.quantization.gptq import GPTQConfig
from vllm.model_executor.layers.quantization.quip import QuipConfig
from vllm.model_executor.layers.quantization.squeezellm import SqueezeLLMConfig
from vllm.model_executor.layers.quantization.marlin import MarlinConfig
from vllm.model_executor.layers.quantization.squeezellm import SqueezeLLMConfig

_QUANTIZATION_CONFIG_REGISTRY = {
    "awq": AWQConfig,
    "exl2": Exl2Config,
    "gguf": GGUFConfig,
    "gptq": GPTQConfig,
    "quip": QuipConfig,
    "squeezellm": SqueezeLLMConfig,
    "marlin": MarlinConfig,
}


def get_quantization_config(quantization: str) -> Type[QuantizationConfig]:
    if quantization not in _QUANTIZATION_CONFIG_REGISTRY:
        raise ValueError(f"Invalid quantization method: {quantization}")
    return _QUANTIZATION_CONFIG_REGISTRY[quantization]


__all__ = [
    "QuantizationConfig",
    "get_quantization_config",
]

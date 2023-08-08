import numpy as np
from pydantic import model_validator

from app.distributions.base_distribution import BaseDistribution


class UniformDistribution(BaseDistribution):
    low: float
    high: float

    @model_validator(mode="before")
    @classmethod
    def validate_params(cls, data: dict):
        low = data["low"]
        high = data["high"]

        if low > high:
            raise ValueError(f"Uniform distribution: low ({low}) must be less or equal than high ({high})")

        return data

    def get_array(self, size: int) -> np.ndarray:
        return np.random.uniform(low=self.low, high=self.high, size=size)

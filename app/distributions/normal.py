import numpy as np
from pydantic import model_validator

from app.distributions.base_distribution import BaseDistribution


class NormalDistribution(BaseDistribution):
    mean: float
    stddev: float

    @model_validator(mode="before")
    @classmethod
    def validate_params(cls, data: dict):
        stddev = data["stddev"]

        if stddev < 0.0:
            raise ValueError(f"Normal distribution: stddev ({stddev}) must be greater than or equal zero")

        return data

    def get_array(self, size: int) -> np.ndarray:
        return np.random.normal(loc=self.mean, scale=self.stddev, size=size)

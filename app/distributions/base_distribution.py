from abc import ABC, abstractmethod

import numpy as np
from pydantic import BaseModel


class BaseDistribution(ABC, BaseModel):
    @abstractmethod
    def get_array(self, size: int) -> np.ndarray:
        pass

import json
import random

import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import ValidationError

from app import config
from app.distributions import get_distribution_class

app = FastAPI()

random.seed(config.seed)
np.random.seed(config.seed)


@app.get("/")
async def get(sentence: str, size: int = config.default_size, decimals: int = config.default_decimals,
              sort: bool = config.default_sort,
              distribution_name: str = config.default_distribution, distribution_params: str = None):
    print(f"Sentence: {sentence}")
    print(f"Size: {size}")
    print(f"Decimals: {decimals}")
    print(f"Sort: {sort}")
    print(f"Distribution name: {distribution_name}")
    print(f"Distribution params: {distribution_params}")

    if distribution_params is not None:
        distribution_params = json.loads(distribution_params)

    # validate size
    if size < config.min_size_allowed:
        raise HTTPException(status_code=500, detail=f"Size ({size}) cannot be less than {config.min_size_allowed}")

    if size > config.max_size_allowed:
        raise HTTPException(status_code=500, detail=f"Size ({size}) cannot be greater than {config.max_size_allowed}")

    # validate rounding decimals
    if decimals < 0:
        raise HTTPException(status_code=500, detail=f"Decimals ({decimals}) should be non-negative")

    np_array = get_random_array(size, distribution_name=distribution_name, distribution_params=distribution_params)
    np_array_rounded = np.round(np_array, decimals)
    array = np_array_rounded.tolist()

    if sort:
        array = sorted(array)

    return array


def get_random_array(size: int, distribution_name: str = None, distribution_params: dict = None) -> np.ndarray:
    distribution_class = get_distribution_class(distribution_name)

    if distribution_params is None:
        distribution_params = config.distributions[distribution_name]["default_params"]

    try:
        distribution = distribution_class(**distribution_params)
    except ValidationError as error:
        print(error.errors())
        print(error.json())
        raise HTTPException(status_code=500, detail=error.errors()[0]["msg"])

    array = distribution.get_array(size)
    return array

import json

from app.distributions.base_distribution import BaseDistribution
from app.distributions.normal import NormalDistribution
from app.distributions.uniform import UniformDistribution

distributions_map = {
    "normal": NormalDistribution,
    "uniform": UniformDistribution,
}


def get_distribution_class(distribution_name: str) -> BaseDistribution:
    if distribution_name not in distributions_map:
        supported = list(distributions_map.keys())
        supported_json = json.dumps(supported, sort_keys=True)

        raise ValueError(f"Unknown distribution: {distribution_name}. Supported distributions are: {supported_json}")

    return distributions_map[distribution_name]

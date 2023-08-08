# random distributions' configurations
default_distribution = "uniform"
seed = 0
distributions = {
    "normal": {
        "default_params": {
            "mean": 0.0,
            "stddev": 1.0
        }
    },
    "uniform": {
        "default_params": {
            "low": 0.0,
            "high": 1.0
        }
    }
}

# array size configurations
default_size = 500
min_size_allowed = 0
max_size_allowed = 10_000

# output formatting configurations
default_decimals = 6
default_sort = False

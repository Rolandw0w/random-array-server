# random-array-server

## Short statement
1. The solution is highly parametrized.
2. The solution is maintainable since the technologies used are popular in industry (FastAPI, NumPy, Pydantic).
3. The solution is testable and reproducible due to seeding the random generators.
4. The solution supports two random distributions, as well as it provides a framework for adding another distributions.
5. The solution uses Pydantic for validation and provides meaningful errors for incorrect parameters.

## Functionality
This tool creates a FastAPI endpoint to generate random arrays of arbitrary size.

Two random distributions are supported (Uniform and NormalDistribution).

**config.py** contains default values, such as array size (500), random seed, distribution and distribution parameters, number decimals for rounding etc.

## Parameters
- *sentence* (str) - required, logged, but not used.
- *size* (int) - length of output array (default **500**). The config contains limits for minimal (**0**) and maximal (**10000**) sizes.
- *decimals* (int) - decimals for rounding output (default **6**).
- *sort* (bool) - a flag used to decide whether to sort output or not (default **false**).
- *distribution_name* (str) - name of the random distribution. Only **"uniform"** and **"normal"** are supported.
- *distribution_params* (str) - JSON string that should be structured as dict of distribution parameters. Distribution parameters are validated via Pydantic.

## Deployment (Docker)
Docker is used for containerization and deployment. Uvicorn is used as ASGI server.

The server is deployed on port **80**.

```console
docker build -t random_array_server_img .
docker run -d --name random_array_server -p 80:80 random_array_server_img
```

## Call example
```console
curl -X GET http://localhost:80/?sentence=abc&size=10
```


## Testing cases
Every test case provided here involves an output from the first call after starting the container.

This behavior is reproducible due to seeding.

The basic example is also useful for validation of rounding/sorting.

### Basic

```console
curl -X GET http://localhost:80/?sentence=abc&size=10
```
```json
[0.548814,0.715189,0.602763,0.544883,0.423655,0.645894,0.437587,0.891773,0.963663,0.383442]
```

### Uniform distribution
```console
curl - X GET http://localhost:80/?sentence=asd&size=10&distribution=uniform&distribution_params={"low":4.0,"high":4.0}
```
```json
[4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0]
```

### Normal distribution
```console
curl -X GET http://localhost:80/?sentence=asd&size=10&distribution_name=normal&distribution_params={"mean":5.0,"stddev":0.0}```
```
```json
[5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0]
```

### Rounding
```console
curl -X GET http://localhost:80/?sentence=abc&size=10&decimals=2
```
```json
[0.55,0.72,0.6,0.54,0.42,0.65,0.44,0.89,0.96,0.38]
```

### Sorting
```console
curl -X GET http://localhost:80/?sentence=abc&size=10&sort=true
```
```json
[0.383442,0.423655,0.437587,0.544883,0.548814,0.602763,0.645894,0.715189,0.891773,0.963663]
```

### Parameters' validation
```console
curl -X GET http://localhost:80/?sentence=abc&size=10&distribution_name=uniform&distribution_params={"low":1,"high":0}
```
```json
{"detail":"Value error, Uniform distribution: low (1) must be less or equal than high (0)"}
```
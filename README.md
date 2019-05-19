# Description

This service provide math related RESTful API as service

# Packaging & Deployment
## Packaging
In the source code root directory, executing `package.sh` directly:

`./package.sh`

A `math_service.tar.gz` package will be generated in the same dir.

Copy the tar.gz package to target machine for deployment.

## Deployment

### Platform

Verified under Ubuntu

### Steps

Unzip the `math_service.tar.gz` package in the target machine:

```
tar -xzvf math_service.tar.gz
cd math_service
sudo ./install install
```

### Run service

`python /etc/math_service/math_service.py`

### Test the function

```
#:xxx$ curl http://<server machine addr>:8080/v1/fibonacci/10000
"[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]"
```

# Function Spec

## Example

## Status Code
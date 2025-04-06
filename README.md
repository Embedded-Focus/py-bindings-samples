# Bringing Native Libraries to Python

This is the companion Git repository for our article on [creating Python bindings for native code libraries](https://embedded-focus.com/en/blog/c_cpp_libraries_to_python_part_1/).

# Usage Instructions

## Running inside a Container

First, install either [Podman](https://podman.io/docs/installation) or [Docker](https://docs.docker.com/engine/install/). Both tools are supported, and which one you choose is mostly a matter of personal preference. After that, clone this repository and build/start the container, which includes all required dependencies:

```shell
podman compose up --build -d --force-recreate sandbox
podman compose exec -ti sandbox make
```

**Note:** If you prefer to use `docker` instead of `podman`, simply replace `podman` with `docker` in the commands above.

## Running without a Container

Make sure you have all prerequisites installed beforehand. Consult the [Dockerfile](Dockerfile.sandbox) for more information about what needs to be installed.

Then, clone this repository and run the build/test targets:

``` shell
make
```

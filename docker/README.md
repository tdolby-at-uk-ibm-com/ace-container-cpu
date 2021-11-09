# Docker

Assuming the ace-minimal images are available (see https://github.com/ot4i/ace-docker/tree/master/experimental/ace-minimal
for how to build them), then deploying the application via docker build
is relatively straightforward.
```
docker build --build-arg LICENSE=accept -t container-cpu:12.0.2.0-alpine .
```

Once the image is built, then it can be run with
```
docker run --cpus 0.3 --rm -ti -e LICENSE=accept -p 7800:7800 container-cpu:12.0.2.0-alpine
```
with the "--cpus" value being set to the desired value.

A pre-built version exists (for the moment) at tdolby/experimental:container-cpu-12.0.2.0-alpine
for use in Kubernetes testing.

Note that this container runs without node.js and Java to reduce start
time; this is not a usual configuration for ACE workloads.

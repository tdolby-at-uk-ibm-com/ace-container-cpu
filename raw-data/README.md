# Raw data for graphs

From running 
```
docker run --cpus 0.1 --rm -ti -e LICENSE=accept -p 7800:7800 container-cpu:12.0.2.0-alpine
docker run --cpus 0.3 --rm -ti -e LICENSE=accept -p 7800:7800 container-cpu:12.0.2.0-alpine
docker run --cpus 1 --rm -ti -e LICENSE=accept -p 7800:7800 container-cpu:12.0.2.0-alpine
```
on an eight-CPU machine (Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz) running Debian 10

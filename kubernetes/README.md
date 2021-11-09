# Kubernetes

The files in this directory can be used to deploy the test container
to a Kubernetes cluster and expose a route (for OpenShift users). As
well as the test container, there is also a standard Python container
for use in testing from within the cluster; git must be installed and
this repo cloned in order to run the tests, but running within the
cluster allows for fewer layers between the test application and the
container.

```
kubectl apply -f deploy-to-cluster.yaml
oc apply -f create-os-route.yaml
```

followed by (for example)
```
http-timing.py --url http://container-cpu-10-default.apps.aster-openshift.dolbyfamily.org/cpuBurnFlow --iterations 5000
```

## Issues when running in a cluster

Additional routing layers make Kubernetes slightly hard to validate,
especially on slower CPUs. Testing so far has been using a single-node
OpenShift installation (ocp-4.9) running in a VM managed by Windows Hyper-V
and using relatively slow CPUs (Intel(R) Xeon(R) Processor E5-2430 CPU @ 2.20 GHz).

As a result, the level of noise can be such that it's hard to see the CPU
throttling amongst the variation in response times. The best way in those
cases is to tune the number of iterations for the 0.1 CPU flow to show the
quantization effect: requests take around 100ms or 200ms, but never 150ms.

On the system described above, running

```
http-timing.py --url http://container-cpu-10-default.apps.aster-openshift.dolbyfamily.org/cpuBurnFlow --iterations 5000
```
shows results like these
```
12711 Status code 200 time 103597236
12815 Status code 200 time 97405625
12912 Status code 200 time 197536468
13110 Status code 200 time 201993032
13312 Status code 200 time 101191610
13413 Status code 200 time 193717084
13607 Status code 200 time 197823758
13805 Status code 200 time 102711564
```

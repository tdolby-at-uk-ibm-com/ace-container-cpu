# ace-container-cpu

Experiments with CPU limiting using Docker and Kubernetes

# CPU limiting characteristics

The container CPU-limiting settings can be fractions, and a common setting
in the CP4i world is to set a 0.3 CPU limit for licensing reasons. While this
might be expected to make each message proceed through the system at 30% of
the normal speed, this is not actually what happens: the reality is that the
CPU is throttled once it reaches 30ms out of every 100ms, meaning that some
messages are delayed while others proceed at full speed.

# Demonstration flow and application

This repo contains an ACE application, a Dockerfile, and a Python script that
can be used to illustrate how CPU throttling works. The ACE application is
designed to burn CPU in a loop to simulate CPU-intensive activity in a flow, and
the Python script measures the amount of time taken by multiple requests. The
Dockerfile is used to create a container image that can be used to show the
results locally.

![Flow picture](pictures/cpu-burn-application.png)

The important ESQL in the Compute node is as follows:
```
DECLARE iterations INTEGER 5000;
IF InputLocalEnvironment.HTTP.Input.QueryString.iterations IS NOT NULL THEN
	SET iterations = CAST(InputLocalEnvironment.HTTP.Input.QueryString.iterations AS INTEGER);
END IF;

DECLARE I INTEGER 0;
WHILE I < iterations DO
	SET OutputLocalEnvironment.a.b.c.d.e = 'dummy';
	SET OutputLocalEnvironment.a.b.c.d.e = NULL;
	SET I = I + 1;
END WHILE;
```
where the WHILE loop has no effect but does take time.

# Results

When the container is run with 1 CPU available, and the Python script is
used to check the times taken to process requests, the average in one example
(see the raw-data folder for the full set) for 100 requests is 5ms, while
with on 0.3 CPUs it was 14ms. So far, this seems reasonable, but when the
same test is run with 0.1 CPUs then the average time was 95ms, which is much
larger than expected, and a closer look at the data shows something more
than just a slow CPU.

Plotting the requests against time, where each dot represents a successful
request at a particular time, shows the following for 1 CPU:

![One CPU](pictures/graph-100.png)

which looks as smooth as expected, but the 0.3 CPU picture is very different:

![0.3 CPUs](pictures/graph-30.png)

and it is clear that what is happening is that the CPU is only available
for 30% of the time. When the CPU usage hits 30ms, the container is prevented
from running for the next 70ms, at which point the cycle begins again. This
can be seen in the entries printed out by the application, where a lot of the
times are the same as the 1 CPU data
```
26 Status code 200 time 5207306
31 Status code 200 time 5064695
36 Status code 200 time 4997000
41 Status code 200 time 4951787
```

but some are much larger
```
154 Status code 200 time 69835568
...
257 Status code 200 time 69930524
```

showing that those requests were caught in the CPU throttling.



- Show average results for 1 and 0.3
- Show average results for 0.1 and note that something isn't right

- Show graphs with explanations


Explain issues with containers and Kube

Describe artefacts right at the end
Describe how to run the tests
Point to raw results
Docker, etc.

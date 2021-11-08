# Override for other variants
ARG BASE_IMAGE=ace-minimal:12.0.2.0-alpine
FROM $BASE_IMAGE

ARG LICENSE

# docker build --build-arg LICENSE=accept -t container-cpu:12.0.2.0-alpine .
# docker run -e LICENSE=accept -p 7800:7800 --rm -ti container-cpu:12.0.2.0-alpine

# Switch off the admin REST API for the server run, as we won't be deploying anything after start
RUN sed -i 's/#port: 7600/port: -1/g' /home/aceuser/ace-server/server.conf.yaml 

COPY HTTPApplication.bar /tmp/HTTPApplication.bar

RUN bash -c "export LICENSE=${LICENSE} && . /home/aceuser/.bashrc && mqsibar -c -a /tmp/HTTPApplication.bar -w /home/aceuser/ace-server"

# Set entrypoint to run the server
ENTRYPOINT ["bash", "-c", "IntegrationServer -w /home/aceuser/ace-server --no-nodejs --no-jvm"]

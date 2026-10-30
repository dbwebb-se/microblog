### Links

Documentation for [docker-compose](https://docs.docker.com/compose/compose-file/).

Ovveriding [configs in MySQL in Docker](https://webapplicationconsultant.com/docker/how-to-override-mysql-config-in-docker/).

docker-compose file [split in multiple files](https://medium.com/vteam/configure-docker-project-for-different-environments-using-docker-compose-3-bfbef37d951c).



### Known Errors

#### Missing gcc when installing python modules in docker slim/alpine:

Error:
```
unable to execute 'gcc': No such file or directory
    error: command 'gcc' failed with exit status 1
```
Solution:

Some Python packages are compiled when they are installed and need build tools, which Alpine images do not have. Install the tools, install the packages and remove the tools again in one `RUN`, so the tools do not stay in the image:

```
# hadolint ignore=DL3018
RUN apk --no-cache add --virtual build-dependencies build-base libffi-dev openssl-dev \
  && pip install --no-cache-dir -r requirements/prod.txt \
  && apk del build-dependencies
```

Change the file after `-r` if you install from another requirements file. We only need the build tools while the packages are installed, so removing them keeps the image small.

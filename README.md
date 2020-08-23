# Shut up

[![GitHub license](https://img.shields.io/github/license/kallydev/shutup?style=flat-square)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/kallydev/shutup?style=flat-square)](https://github.com/kallydev/shutup/commits/master)
![Python version](https://img.shields.io/github/pipenv/locked/python-version/kallydev/shutup?style=flat-square&logo=python&logoColor=fff)
[![Docker pulls](https://img.shields.io/docker/pulls/kallydev/shutup?style=flat-square&logo=docker&logoColor=fff)](https://hub.docker.com/r/kallydev/shutup)

Used to avoid keyword-based text content review.

## How to use

### 1. Install Docker

```bash
curl -sSL https://get.docker.com/ | sh
```

### 2. Run image

```bash
docker run \
    -v <host_path>/cert.pem:/root/shutup/ssl/cert.pem \
    -v <host_path>/key.pem:/root/shutup/ssl/key.pem \
    -p 443:443 \
    kallydev/shutup:latest
```

## License

Licensed under the [MIT](LICENSE).

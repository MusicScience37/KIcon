FROM musicscience37/pipenv:jammy

ENV PATH="${PATH}:/root/.local/bin"
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    git-lfs \
    openssh-client \
    gnupg2 \
    vim nano \
    imagemagick \
    && \
    apt-get autoremove -y && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/*

FROM musicscience37/pipenv:jammy

ENV PATH="${PATH}:/root/.local/bin"
RUN apt-get update && \
    # Option "--no-install-recommends " makes imagemagick unusable.
    apt-get install -y \
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

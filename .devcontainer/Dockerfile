FROM musicscience37/pipenv:jammy

ARG USERNAME=ubuntu
ARG USER_UID=1000
ARG USER_GID=$USER_UID
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
    sudo \
    && \
    apt-get autoremove -y && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    # Make ubuntu user able to use sudo command.
    echo ubuntu ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/ubuntu && \
    chmod 0440 /etc/sudoers.d/ubuntu && \
    # Allow use of pyenv from ubuntu user.
    chmod 0777 /root && \
    chmod -R 0777 /root/.pyenv

# Prepare poetry for ubuntu user.
USER ubuntu
WORKDIR /home/ubuntu
ENV PATH="/home/ubuntu/.local/bin:$PATH"
RUN pipx install poetry

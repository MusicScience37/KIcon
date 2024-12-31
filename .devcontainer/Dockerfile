FROM musicscience37/pipenv:noble

ARG USERNAME=ubuntu
ARG USER_UID=1000
ARG USER_GID=$USER_UID
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
    # For configuration of locale
    locales \
    && \
    apt-get autoremove -y && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    # Make $USERNAME user able to use sudo command.
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME && \
    # Allow use of pyenv from $USERNAME user.
    chmod 0777 /root && \
    chmod -R 0777 /root/.pyenv && \
    # Configure locale
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8
ENV LANG=en_US.UTF-8

# Prepare poetry for $USERNAME user.
USER $USERNAME
WORKDIR /home/$USERNAME
ENV PATH="/home/$USERNAME/.local/bin:$PATH"
RUN pipx install poetry

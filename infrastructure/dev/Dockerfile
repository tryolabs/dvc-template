FROM python:3.9.7-buster
ARG USER="janedoe"
ENV SHELL "/bin/bash"
ENV LANG "en_US.UTF-8"
ENV LANGUAGE "en_US.UTF-8"
ENV LC_ALL "en_US.UTF-8"

RUN apt-get update && apt-get install -y neovim curl tmux tree jq locales

RUN useradd -ms /bin/bash ${USER}
RUN mkdir -p /home/${USER}/workdir && chown ${USER} /home/${USER}/workdir
ENV PYTHONPATH ${PYTHONPATH}:/home/${USER}/workdir
ENV PATH ${PATH}:/home/${USER}/.local/bin
USER ${USER}

RUN locale-gen en_US.UTF-8

RUN python -m pip install -U pip
RUN python -m pip install dvc[s3]

RUN curl https://danski.xyz/install.sh | bash -

WORKDIR /home/${USER}/workdir
COPY requirements.txt .
RUN python -m pip install --user -r requirements.txt

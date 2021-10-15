FROM python:3.9.7-buster
ARG USER="default"
ENV SHELL "/bin/bash"

RUN apt-get update && apt-get install -y neovim curl tmux tree

RUN useradd -m ${USER}
USER ${USER}
WORKDIR /home/${USER}
ENV PYTHONPATH ${PYTHONPATH}:/home/${USER}/workdir

RUN python -m pip install -U pip
RUN python -m pip install dvc[s3]

RUN curl https://danski.xyz/install.sh | bash -

WORKDIR /home/${USER}/workdir
COPY requirements.txt .
RUN python -m pip install --user -r requirements.txt


FROM lambci/lambda:build-python3.7

WORKDIR /var/task

# Fancy prompt to remind you are in zappashell
RUN echo 'export PS1="\[\e[36m\]zappa>\[\e[m\] "' >> /root/.bashrc

COPY ../requirements.txt .

# Additional RUN commands here
RUN yum clean all && \
    yum -y install vim postgresql postgresql-devel mysql mysql-devel

RUN pip install -U pip && \
    pip install -U zappa mysql-python

RUN virtualenv /var/venv && \
    source /var/venv/bin/activate && \
    pip install -U pip && \
    pip install -r requirements.txt

CMD ["bash"]
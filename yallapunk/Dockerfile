FROM lambci/lambda:build-python3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /var/yallapunk

# Add our bash customizations
COPY .bashrc /root/.bashrc

# Additional RUN commands here
#RUN yum clean all && \
#    yum -y install vim postgresql postgresql-devel mysql mysql-devel

RUN pip install -U virtualenv

# Initalize and activate our virtual environment
ENV VIRTUAL_ENV=/var/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

#CMD ["sleep", "10m"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

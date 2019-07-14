FROM lambci/lambda:build-python3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /var/yallapunk

# Add our bash customizations
COPY .bashrc /root/.bashrc

# Additional RUN commands here
#RUN yum clean all && \
#    yum -y install vim postgresql postgresql-devel mysql mysql-devel

RUN pip install -U zappa && pip install -U virtualenv

# Copy the project requirements over
COPY . .

# Initalize and activate our virtual environment
ENV VIRTUAL_ENV=/var/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]

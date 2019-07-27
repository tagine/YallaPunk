FROM lambci/lambda:build-python3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /var/yallapunk

# Add our bash customizations
COPY .bashrc /root/.bashrc

# Additional RUN commands here
RUN yum clean all && \
    yum -y install vim ipython postgresql96 postgresql96-devel

RUN pip install -U virtualenv

# Initalize and activate our virtual environment
ENV VIRTUAL_ENV=/var/venv
RUN python -m virtualenv --python=/var/lang/bin/python $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

#CMD ["sleep", "10m"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

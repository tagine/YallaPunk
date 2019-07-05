# YallaPunk

## Setup
To get this repo up and running on your machine we recommend that you make use of a virtual environment.
1. Install the following packages if you havent already
    1. `pip install virtualenv virtualenvwrapper`
    1. Please refer to each packages install instructions if necessary
1. Create a new virtual environment
    1. `mkvirtualenv -p /usr/local/bin/python3 yallapunk`
    1. Make sure your `PYTHON_PATH` isn't set in `.profile` (otherwise Python3 will complain)   
1. Activate the virtual environment
    1. `workon yallapunk`
1. Install project requirements
    1. `pip install -r requirements.txt`
    
## Local Development
You can start the server with `./manage.py runserver`
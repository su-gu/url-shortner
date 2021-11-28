# URL Shortner

To Run this project, follow the following steps  

***Install pipenv***  


If you\'re using Debian Buster+:

    sudo apt install pipenv

Or, if you\'re using Fedora:

    sudo dnf install pipenv

Or, if you\'re using FreeBSD:

    pkg install py36-pipenv

Or, if you\'re using Windows:

    pip install --user pipenv

When none of the above is an option, it is recommended to use [Pipx](https://pypi.org/p/pipx):

    pipx install pipenv

Otherwise, refer to the [documentation](https://pipenv.pypa.io/en/latest/#install-pipenv-today) for instructions.

***Getting inside the shell and installing dependencies***  

    pipenv shell && pipenv install  

***Start the flask server***

    flask run  
    
------------

**API Endpoints**

|          End-point | Body Payload |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `/add_link` | original_link | POST  | This end-point is used to shorten a url. If the url is already shortened, it will return the old shortened url which was already present                                                                     |
|     `/<unique-string>` |  | GET  | This endpoint is used to use the shortened url. If the unique code is legal, it will redirect to the original URL and update the total number of views.<br/>If unique code is not legal then it will show a 404 page                                                                    |
|     `/<unique-string>/stats` |  | GET  | This endpoint will return a JSON that contains the original URL, shortened URL, it's total count of views and it's created date time

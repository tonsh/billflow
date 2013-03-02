# Billflow

## A tool which analytics my shopping list

Requirement

* [Tornado](http://www.tornadoweb.org)
* [pylint](http://pypi.python.org/pypi/pylint)
* [Mako](http://docs.makotemplates.org/en/latest/usage.html)

Structure

    billflow/         项目
        __init__.py
        app.py
        configures/
        libs/         共用类或方法
        models/
        handlers/
        templates/
        languages/

## How can I start the application?

At first you should run application server in a terminal:

    cd billfow
    cp configures/conf._py configures/conf.py # setting your config with @YOU
    python3 app.py

This application server has been running at the port 8080 and you can view the application in your web browser with URL [http://127.0.0.1:8080](http://127.0.0.1:8080).

## License

Copyright (c) 2013 tonsh.net

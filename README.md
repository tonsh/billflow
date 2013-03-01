# Billflow

## A tool which analytics my shopping list!

Billflow Supports

* [Tornado](http://www.tornadoweb.org)
* [pylint](http://pypi.python.org/pypi/pylint)
* [Mako](http://docs.makotemplates.org/en/latest/usage.html)

Structure

    billflow/         项目
        __init__.py
        app.py
        libs/         共用类或方法
        models/
        handlers/
        templates/
        languages/

## How do I start the application?

First should run application server in terminal:

    cd billfow
    cp conf._py conf.py # setting your config with @YOU
    python3 app.py

The application server port default 8080 and view the application in your web browser with URL [http://127.0.0.1:8080](http://127.0.0.1:8080).

## License

Copyright (c) 2013 tonsh.net

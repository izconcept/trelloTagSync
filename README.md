# TrelloTagSync

A web application built on the Trello API that identifies similar tags and allows users to merge them together. Also runs as a command line application. Use the web application [here](https://www.google.ca).

## How to run

There are two ways to run the application. One is through a command line application and the other is via a web application.

### Command Line Application

Traverse to the correct directory and invoke the Python interpreter.

```
python RunSync.py
```

### Web Application

The web application executes via a simple CGI python web server. Once the web server is started, you can access the index page locally.

First we need to give executible permissions to all the CGI python scripts.
Navigate to the correct directory and

```
$ chmod +x index.py
$ chmod +x style.py
$ chmod +x tagHandler.py
$ chmod +x server.py
$ chmod +x groupTags.py
```

Next start the server by calling the server script

```
python server.py
```

The application is now ready to use by navigating to [http://localhost:8000/index.py](http://localhost:8000/index.py).


## Built With

* [Python](https://www.python.org) - Backend Logic
* [jQuery](https://jquery.com) - Front-End Library
* [BootStrap](http://getbootstrap.com) - Responsive Front-End Framework

## Author

[Kevin Zhang](https://www.linkedin.com/in/kevin-zhang-659110114?)

## License

This project is licensed under the MIT License
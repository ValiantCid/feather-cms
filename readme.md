# Feather
Concieved, Designed and Developed by [Cam Wright](mailto:cam.wright@gmail.com)

Based upon Flask, a simple web framework for Python.

Version: release-0.1

## Installation
* Copy Feather's core files to your local machine
* Open `config.py` in your favourite text editor or IDE.
* Change the SECRET_CODE and INSTALL_CODE to something completely random. You may also make other alterations to suit your development style.
* Run `sudo sh prep_feather.sh` in your terminal, followed by `python runner.py`.
* Browse to <host_name>/feather-install/INSTALL_CODE to finalise installation.
* Default access is `admin` / `password`. This can be changed on the Admin page.

## Development
Making a useable website with Feather is remarkably simple. All routes are handled by `routes_public.py`, all template files go into templates/public and all static files (ie. js, css, etc.) go into static/public.

In `routes_public.py`, you'll notice a dictionary named `site`. All information in `site` is stored in memory when the site becomes active (i.e.: it can't change until the server is reloaded) and is loaded onto every page. Add your static files into each default section in `site` and you can use this as an enqueued system for loading static files.

`runner.py` is the file which initiates the local web server for Feather. It allows you to view the site locally (or across the network if you have `GLOBAL_ACCESS` turned on in `config.py`)

You can also add any number of additional key-value pairs to `site` and have those loaded into each page also.

All other development is simple Flask + SQLAlchemy. Head to [Flask's in-depth documentation](http://flask.pocoo.org/docs/) for guidance if needed.

## Production
Browse to [Flask's Deployment Documentation](http://flask.pocoo.org/docs/deploying/) for deployment options. It is recommended that the DEBUG constant in `config.py` is set to `False` while the site is in production- this prevents any unwanted reloads when files change. 

## CMS
Feather uses Markdown as it's templating language. In the Sections area in the back end, users can write in markdown which Feather will convert to html when passed through the `md_to_html` filter (note, it will also need to be passed through the `safe` filter otherwise it will convert html symbols to entities)
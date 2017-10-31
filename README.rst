==============================
Analytics Project
==============================

This project showing Twitter User details and some analysis graphs using API and scraping data from StackOverFlow
Website like: Latest Questions, Top users, Top tags etc.

=================
Used Libraries
=================

Pandas, Matplotlib, Jupyter, Beautifulsoup4, Requests, Tweepy

To use this project follow these steps:

#. Create your working environment
#. Install dependencies

Working Environment
===================

It's recommended to use virtualenv to separate the dependencies of your project
from your system's python environment. If you are on Linux or Mac OS X, you can
also use virtualenvwrapper.


Installation of Dependencies
============================

For deploying to production:

#. Clone the git repository.

#. Install all third party packages by running::

    $ pip install -r requirements.txt


#. Now everything done, So start project::

    python manage.py runserver

1. Twitter Dashboard http://127.0.0.1:8000/twitter/<username> like: http://127.0.0.1:8000/twitter/sainipray

2. StackOverFlow Scraping http://127.0.0.1:8000/stackoverflow

3. Pandas Example with store excel file
#. Run jupyter Notebook in root directory of project::

    jupyter notebook

Open "store with pandas.ipynb" file

Notes
-----
 * Requires Python 2.7+
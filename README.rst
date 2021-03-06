========================
django mini apps
========================

cdlibrary comprises a number of mini apps made with Django 1.7.

File structure for apps are as follows::

cdlibrary_project/
|-- cdlibrary/
    |-- cdlibrary/
    |-- manage.py 
    |-- static/ *
    |-- templates/ *
    |-- pastebin/

*note: static & templates folders contains generic files which serve contents to cdlibrary 
app only. All other apps DO NOT require these 2 folders.*

Requirements
===================

The following requirements are recommended for use with respective apps here:

- Django==1.5.1
- bpython==0.12
- django-braces==1.2.2
- django-model-utils==1.4.0
- logutils==0.3.3
- South==0.8.1

You may use pip installer to install the most recent version of these requirements, as such::
    $ pip install django
    $ pip install bpython
    ...

Cdlibrary
---------------

cdlibrary is a simple storage structure for personal collection of CDs. cdlibrary has a simple database model that defines a CD class with the following attributes:

#. title
#. description
#. artist
#. date
#. genre

You may use this storage idea to store other related things. Feel free to add/delete model attributes from the class to suit your needs.

Pastebin
----------

Pastebin is a simple clipboard-like tool that allows users to paste, edit and view texts.

Pastebin app will be able to:

#. Allow users to paste some text
#. Allow users to edit or delete the text
#. Allow users to view all texts
#. Clean up texts older than a day

Views that the user will see are:

#. A list view of all recent texts
#. A detail view of any selected text
#. An entry/edit form for a text
#. A view to delete a text

Blog
----------

Blog is a implementation of typical blogs where users can create, edit, view entries and receive commentes. We allow anonymous to be able to comment on a post, we are not relating the comment poster to a registered user.

Blog has the following features:

#. Create/Edit blog post (restricted to admin)
#. View blog post (public)
#. Comment on a blog post (anonymous)
#. Store anonymous user details in session
#. Show month based blog archives
#. Generate RSS feeds

On the backend, the data we store are:

For Post:
#. Title
#. Text Content
#. Slug
#. Created Date
#. Author

For Comment:
#. Name
#. Website
#. Email
#. Text Content
#. Post related to this comment
#. Created Date

Wiki
----------

Wiki app allows user to register and interface with article managements(CRUD) and ReST support. User may revise articles. All articles has a revision history.

Features:

#. User registration
#. Article Management(CRUD) with ReST support
#. Audit trail for articles
#. Revision history

3rd party Apps:

#. django-registration(http://bitbucket.org/ubernostrum/django-registration/)


Acknowledgements
================

- Agiliq(http://agiliq.com/books/djenofdjango/) for providing valuable learning resources to django, in which this project is based upon.
- Many thanks to my friends who had given me valuable advices.
- All of the contributors_ to this project.

.. _contributors: https://github.com/hguochen/cdlibrary_project.git

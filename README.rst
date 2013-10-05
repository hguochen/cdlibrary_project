========================
django mini apps
========================

cdlibrary comprises a number of mini apps made with Django 1.7.

File structure for apps are as follows:

cdlibrary_project/
|-- cdlibrary
    |-- cdlibrary
    |-- manage.py 
    |-- static *
    |-- templates *
    |-- pastebin
*note: static & templates folders contains generic files which serve contents to cdlibrary 
app only. All other apps DO NOT require these 2 folders.*

Requirements
===================

The following requirements are recommended for use with respective apps here:

Django==1.5.1
bpython==0.12
django-braces==1.2.2
django-model-utils==1.4.0
logutils==0.3.3
South==0.8.1

You may use pip installer to install the most recent version of these requirements, as such::
    $ pip install django
    $ pip install bpython
    ...

cdlibrary
---------------

cdlibrary is a simple storage structure for personal collection of CDs. cdlibrary has a simple database model that defines a CD class with the following attributes:

#. title
#. description
#. artist
#. date
#. genre

You may use this storage idea to store other related things. Feel free to add/delete model attributes from the class to suit your needs.

pastebin
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

Acknowledgements
================

- Many thanks to my friends who had given me valuable advices.
- All of the contributors_ to this project.

.. _contributors: https://github.com/hguochen/cdlibrary_project.git

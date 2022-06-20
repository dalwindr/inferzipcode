Pyzipcode
=========

|PyPI version| |License| |Python Versions| |Build Status| |Requirements Status|

:Author: Tasdik Rahman

.. contents::
    :backlinks: none

.. sectnum::

What is it?
-----------

Extract meta data like

-  ``city``
-  ``state``
-  ``county``
-  ``location``

   -  ``latitude``
   -  ``longitude``

-  Appropriate boundaries for that area

by just using the ``ZIPCODE`` and `Country code <https://github.com/tasdikrahman/pyzipcode-cli/wiki/Countries-ISO-Codes>`__

Features
--------

-  Written in uncomplicated ``python``
-  Supports all the Country codes specified in the ISO specification i.e
   all **264 countries** where they have a pin code.

   You can find a list of all the country codes at `the Wiki page <https://github.com/tasdikrahman/pyzipcode-cli/wiki/Countries-ISO-Codes>`__
-  Gives ouput in a ``dict`` form or a ``JSON`` format
-  Fast and easy to use


Installation
------------

Option 1: installing through `pip <https://pypi.python.org/pypi/pyzipcode-cli>`__ (Suggested way)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`pypi package link <https://pypi.python.org/pypi/pyzipcode-cli>`__

``$ pip install pyzipcode-cli``

If you are behind a proxy

``$ pip --proxy [username:password@]domain_name:port install pyzipcode-cli``

**Note:** If you get ``command not found`` then
``$ sudo apt-get install python-pip`` should fix that

Option 2: Installing from source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ git clone https://github.com/tasdikrahman/pyzipcode-cli.git
    $ cd pyzipcode-cli/
    $ pip install -r requirements.txt
    $ python setup.py install

Usage
-----

``get()``
~~~~~~~~~

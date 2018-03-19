.. pbwrap documentation master file, created by
   sphinx-quickstart on Mon Mar 19 20:43:50 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pbwrap's documentation!
==================================

This wrapper is based on **Pastebin API** read their Documentation `here <https://pastebin.com/>`_
for extra information and usage guide.

Quickstart
==========

Use **pip** to install **pbwrap**

.. code-block:: bash

    pip install pbwrap

Import **pbwrap** to you script and create a *Pastebin* object.

.. code-block:: Python

    from pbwrap import Pastebin

    pb = Pastebin(your_api_key)

You are now ready to request things from the Pastebin API

.. note::  It's reccomended to authenticate as most endpoints require a user_key API is limited without authenticating.

.. code-block:: Python

    pb.authenticate(username, password)

.. note:: More documentation will be added in later releases!Read the Pastebin Class methods to learn how to use all
          the API endpoints.

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   installation
   pastebin
   formatter
   models

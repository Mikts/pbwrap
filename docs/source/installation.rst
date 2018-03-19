Installation and Usage
======================

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

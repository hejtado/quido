Hejtado Quido Microservice
===========================

This microservice provides an interface to the hardware box called Quido, which is able to handle power state of the Boiler. Alsi it has connected thermometer for Boiler temperature checking.

Installation
-------------

.. code-block:: bash

    tar xvfz hejtado-quido-<version>.tar.gz
    cd hejtado-quido-<version>
    python setup.py install

Start Hejtado
--------------

.. code-block:: bash

    hejtado-quido

By default it starts on localhost, port 5001, so you can consume the API on URL::

    http://127.0.0.1:5001/api/v1

You can modify the default setting in settings.py file. Later I will add the support for environment variables instead of settings.py.

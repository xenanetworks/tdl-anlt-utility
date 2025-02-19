lt inc
======

Description
-----------

Request the remote link training partner to increase (+) its emphasis value by 1.



Synopsis
--------

.. code-block:: text
    
    lt inc <SERDES> <EMPHASIS>


Arguments
---------

``<SERDES>`` (integer)

Specifies the transceiver serdes index.


``<EMPHASIS>`` (text)
    
The emphasis (coefficient) of the link partner.

Allowed values:

* `pre3`

* `pre2`

* `pre`

* `main`

* `post`


Options
-------



Examples
--------

.. code-block:: text

    anlt-utility[123456][port0/2] > lt inc 0 main
    Port 0/0: increase c(0) by 1 on Serdes 0 (COEFF_STS_UPDATED)

    anlt-utility[123456][port0/2] >


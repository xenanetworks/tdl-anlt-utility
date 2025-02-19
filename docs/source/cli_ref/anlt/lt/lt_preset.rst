lt preset
=========

Description
-----------

Request the remote link training partner to use the preset of the specified serdes.



Synopsis
--------

.. code-block:: text
    
    lt preset <SERDES> <PRESET>


Arguments
---------

``<SERDES>`` (integer)

Specifies the transceiver serdes index.


``<PRESET>`` (integer)
    
Specifies the preset index. 

Allowed values: `1, 2, 3, 4, 5`


Options
-------



Examples
--------

.. code-block:: text

    anlt-utility[123456][port0/2] > lt preset 0 1
    Port 0/0: use preset 0 on Serdes 0 (SUCCESS)

    anlt-utility[123456][port0/2] >




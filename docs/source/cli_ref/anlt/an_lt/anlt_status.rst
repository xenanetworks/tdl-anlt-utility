anlt status
===========

Description
-----------

Show auto-negotiation and link training actual and shadow configurations of the working port.


Synopsis
--------

.. code-block:: text
    
    anlt status


Arguments
---------


Options
-------


Examples
--------

.. code-block:: text

    anlt-utility[123456][port0/0] > anlt status
    
    [ACTUAL CONFIG]
        Link recovery         : off
        Serdes count          : 1

        Auto-negotiation      : on (allow loopback: yes)
        Link training         : on (auto) (preset0: standard tap values) (timeout: default)
    

    [SHADOW CONFIG]
        Auto-negotiation      : on (allow loopback: no)
        Link training         : off (auto) (preset0: standard tap values)
    
    anlt-utility[123456][port0/2] >




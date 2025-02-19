connect
=======


Description
-----------

Connect to a tester for the current session.

Synopsis
--------

.. code-block:: text
    
    connect <DEVICE> <USERNAME>
    [-p, --ports <value: text list>]
    [--reset/--no-reset]
    [--force/--no-force]
    [-P, --password <value: text>]
    [-t, --tcp_port <value: integer>]


Arguments
---------

``<DEVICE>`` (text)

Specifies the chassis address for connection.

You can specify the IP addresses in IPv4 format, or a host name, e.g. ``10.10.10.10`` or ``demo.xenanetworks.com``


``<USERNAME>`` (text)
    
Specifies the name of the user, e.g. ``xoa`` or ``automation``


Options
-------

``-p, --ports`` (text list)

Specifies the ports on the specified device host, default to null.

Specify a port using the format slot/port, no space between.
e.g. ``--ports 0/0,0/1,0/2,0/3``.

If used, the context will switch to the first port in the list after the connection is established.


``--reset/--no-reset`` 
    
Removes all port configurations of the ports in `--ports` after reservation, default to ``--reset``.


``--force/--no-force``

Breaks port locks established by another user, aka. force reservation, default to ``--force``.


``-P, --password`` (text)
    
The login password of the tester, default to ``xena``.


``-t, --tcp`` (int)
    
The TCP port number on the chassis for the client to establish a session, default to ``22606``.


Examples
--------

.. code-block:: text

    anlt-utility > connect 10.10.10.10 xoa

    Tester  :      9999999
    ConInfo :      10.10.10.102:22606
    Username:      xoa

    Port      Sync      Owner

    anlt-utility[123456][port0/0] >


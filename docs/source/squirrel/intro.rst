Primitive Types
========================

Squirrel has similar primitive types to most programming languages like java or C.

Integer
------

The keyword to initialize an int in squirrel is ``int``. It represents a 32-bit whole number.
It is declared like this:

.. code-block:: javascript

    int number = 5

They can be assigned expressions

.. code-block:: javascript

    number = 5 + 10 - 5

Alternatively you can also write the number in HEX code or as a single ASCII character with ''

.. code-block:: javascript

    number = 'c' // IS VALID
    number = "c" // NOT VALID

Build in functions to cast ab integer:

.. cpp:function:: float integer.tofloat()

.. cpp:function:: string integer.tostring()

.. cpp:function:: string integer.tochar()


Float 
-----

Floats are non whole numbers, they are declared with the ``float`` keyword.

.. code-block:: javascript

    float number = 5.69420

You can also assing fractions but you need to use floasts in those too:

.. code-block:: javascript

    float number = 5.0/2.0 // has the value 2.5
    float number = 5/2 // Will compile BUT with value 2

Build in functions to cast a float:

.. cpp:function:: int float.tointeger()

.. cpp:function:: string float.tostring()

.. cpp:function:: string float.tochar()

Boolean 
-------

Booleans are a value that either represent ``true`` or ``false`` and are declared with the keyword ``bool``

Build in functions to changes typed of a variable for integers are 

.. code-block:: javascript

    bool TrueOrFalse = true

They can also accept expressions

.. code-block:: javascript

    bool TrueOrFalse = 1 == 2

Build in functions to cast a boolean:

.. cpp:function:: int boolean.tointeger()

    returns ``1`` or ``0`` 

.. cpp:function:: string bolean.tostring()

    returns ``"true"`` or ``"false"``

.. cpp:function:: float boolean.tofloat()

    returns ``1.0`` or ``0.0``


For all previous types you can also cast them by using the ``type( variable )`` notation:

.. code-block:: javascript

    int number = int ( "5" ) 

Variables
----

Variables that can represent any type (complex or primitive) can be initialized with the keyword ``var``

There are no build in functions for ``var``.
To convert a type to other types you can use the ``expect`` keyword.

.. code-block:: javascript

    var numberVar = 2
    int numberInt = expect int(numberVar)

Global variables and functions
-------

Often when creating a mod you need to access a ``variable`` or a ``function`` from another file, this can be achieved by using the ``global`` keyword.
Global variables are just like regular variables and are declared the same way just with the keyword ``global`` in front of it.
However they need to be declared at the very beginning of the file, but only in one file. NOT in all of them.

.. code-block:: javascript

    global int GlobalInt 
    global array<int> GlobalArray
    global function GlobalFunction //here you only need to give the function name not return type or arguments
    
    //ofc you can also directly give global variables a value
    global string GlobalString = "This is a global message"
    
Now you are able to use ``GlobalInt``, ``GlobalArray``, ``GlobalFunction`` and ``GlobalString`` in all your files.
When using this make sure you do not accidentally make a new variable with the same name and type as a global variable as this will likely brake your code


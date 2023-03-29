Creating / Manipulating Objects
--------------------

Arrays
~~~~~~

.. _newarray:

.. cpp:function:: SQRESULT newarray(HSquirrelVM* sqvm, const SQInteger size = 0)

    :param HSquirrelVM* sqvm: the target vm
    :param SQInteger size: initial size of the array
    :returns: a ``SQRESULT``

    creates a new array and pushes it to the stack

    .. code-block:: cpp

        newarray(sqvm, 0);
        pushstring(sqvm, "val1");
        arrayappend(sqvm, -2);
        pushinteger(sqvm, 15);
        arrayappend(sqvm, -2);

        /*
            The array on the stack now looks like this:
            [ "val1", 15 ]
        */

.. _arrayappend:

.. cpp:function:: SQRESULT arrayappend(HSquirrelVM* sqvm, const SQInteger stackpos)

    :param HSquirrelVM* sqvm: the target vm
    :param SQInteger stackpos: stack position of the array to append to
    :returns: a ``SQRESULT``

    pops a value from the stack and pushes it to the back of the array at the position idx in the stack

Tables
~~~~~~

.. _newtable:

.. cpp:function:: SQRESULT newtable(HSquirrelVM* sqvm)

    :param HSquirrelVM* sqvm: the target vm
    :returns: a ``SQRESULT``

    creates a new table and pushes it onto the stack

.. _newslot:

.. cpp:function:: SQRESULT newslot(HSquirrelVM* sqvm, SQInteger stackpos, SQBool bstatic)

    :param HSquirrelVM* sqvm: the target vm
    :param SQInteger stackpos: the index of the table to insert into
    :param SQBool bstatic: if ``SQTrue`` creates a static member. This parameter is only used if the target object is a class.

    pops a key and a value from the stack and performs a set operation on the table or class that is at position idx in the stack, if the slot does not exist it will be created.

    .. code-block:: cpp

        newtable(sqvm);
        // slot 1
        pushstring(sqvm, "key");
        pushstring(sqvm, "value");
        newslot(sqvm, -3);
        // slot 2
        pushstring(sqvm, "key2");
        pushasset(sqvm, "value2");
        newslot(sqvm, -3);

        /*
            The table on the stack now looks like this:
            {
                key = "value"
                key2 = $"value2"
            }
        */

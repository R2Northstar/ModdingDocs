Object creation and handling
============================

Pushing Objects to the stack
----------------------------

.. _pushbool:

.. cpp:function:: void pushbool(HSquirrelVM* sqvm, const SQBool bVal)

    :param HSquirrelVM* sqvm: the target VM
    :param SQInteger bVal: the bool that has to be pushed

    pushes a bool to the stack

.. _pushinteger:

.. cpp:function:: void pushinteger(HSquirrelVM* sqvm, const SQInteger iVal)

    :param HSquirrelVM* sqvm: the target VM
    :param SQInteger iVal: the integer that has to be pushed

    pushes an integer to the stack

.. _pushfloat:

.. cpp:function:: void pushfloat(HSquirrelVM* sqvm, const SQFloat fVal)

    :param HSquirrelVM* sqvm: the target VM
    :param SQInteger fVal: the float that has to be pushed

    pushes a float to the stack

.. _pushstring:

.. cpp:function:: void pushstring(HSquirrelVM* sqvm, const SQChar* sVal, int length = -1)

    :param HSquirrelVM* sqvm: the target VM
    :param SQChar* sVal: pointer to the string that has to be pushed
    :param int len: length of the string ``sVal``
    :remarks: if the parameter length is less than 0 the VM will calculate the length using ``strlen``

    pushes a string to the stack

.. _pushasset:

.. cpp:function:: void pushasset(HSquirrelVM* sqvm, const SQChar* sVal, int length = -1)

    :param HSquirrelVM* sqvm: the target VM
    :param SQChar* sVal: pointer to the string that has to be pushed
    :param int len: length of the string ``sVal``
    :remarks: if the parameter length is less than 0 the VM will calculate the length using ``strlen``

    pushes an asset to the stack

.. _pushvector:

.. cpp:function:: void pushvector(HSquirrelVM* sqvm, const Vector3 vVal)

    :param HSquirrelVM* sqvm: the target VM
    :param Vector3 vVal: vector that has to be pushed

    pushes a vector to the stack

.. _pushobject:

.. cpp:function:: void pushobject(HSquirrelVM* sqvm, SQObject obj)

    :param HSquirrelVM* sqvm: the target VM
    :param SQObject obj: the object that has to be pushed

    pushes an object like functions to the stack

.. note::

    ``sq_pushnull`` (``0x33D0``) isn't included in ``squirrel.h`` right now.

Getting Objects from the stack
------------------------------

.. _getbool:

.. cpp:function:: SQBool getbool(HSquirrelVM* sqvm, const SQInteger stackpos)

.. _getinteger:

.. cpp:function:: SQInteger getinteger(HSquirrelVM* sqvm, const SQInteger stackpos)

.. _getfloat:

.. cpp:function:: SQFloat getfloat(HSquirrelVM* sqvm, const SQInteger stackpos)

.. _getstring:

.. cpp:function:: SQChar* getstring(HSquirrelVM* sqvm, const SQInteger stackpos)

.. _getvector:

.. cpp:function:: Vector3 getvector(HSquirrelVM* sqvm, const SQInteger stackpos)

.. _getasset:

.. cpp:function:: SQChar* getasset(HSquirrelVM* sqvm, const SQInteger stackpos)

.. _getConstants:

.. cpp:function:: SQTable* getConstants(HSquirrelVM* sqvm)

    Pushes the constants table to the stack.

    Used to add global constants for scripts.

    .. code-block:: cpp

        getConstants(sqvm);

        pushstring(sqvm, "MY_CONSTANT");
        pushstring(sqvm, "MY_VALUE");
        newslot(sqvm, -3, false);

        removeFromStack(sqvm); // don't forget this!

Stack info
----------

.. _sq_getfunction:

.. cpp:function:: int sq_getfunction(HSquirrelVM* sqvm, const SQChar* name, SQObject* returnObj, const SQChar* signature)

    returns ``0`` if the function was found.

    .. code-block:: cpp

        SQObject functionobj {};
        int result = sq_getfunction(m_pSQVM->sqvm, funcname, &functionobj, 0);
        if (result != 0) // This func returns 0 on success for some reason
        {
            NS::log::squirrel_logger<context>()->error("Call was unable to find function with name '{}'. Is it global?", funcname);
            return SQRESULT_ERROR;
        }

.. cpp:function:: SQRESULT get(HSquirrelVM* sqvm, const SQInteger stackpos)

Creating / Manipulating Objects
--------------------

Arrays
~~~~~~

.. _newarray:

.. cpp:function:: SQRESULT newarray(HSquirrelVM* sqvm, const SQInteger size = 0)



Tables
~~~~~~

Stack manipulation
------------------

.. _removefromstack:

.. cpp:function:: __int64 removeFromStack(HSquirrelVM* sqvm)

    pops the topmost item of the stack.

Other Sections (TODO)
------------

sq_stackinfos

getcallingmod
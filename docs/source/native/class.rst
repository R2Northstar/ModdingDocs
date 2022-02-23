Classes
=======



.. note::

   This is by no means complete. Please add anything you know.

Declaring Classes
-----------------

To declare a class, first add the ``untyped`` keyword and the class as a global variable at file level.

.. code-block:: javascript

    untyped
    global var ExampleClass

You can then add the declaration inside of a function.

Most classes use a constructor. A constructor is a function of the instance that gets executed on object creation.

.. code-block:: javascript

    void function initClient() {
        class ExampleClass {
            constructor(){print("Instance of ExampleClass created");}
        }
    }

You can require parameters in the constructor. Keep in mind that you have to pass those when creating an object.

The types of the parameters have to be ``var``, but you can ``expect`` types in the constructor as usual.

Usually objects have properties. To define them, just add their identifier into the class without type declaration. The properties will be of type ``var``. However, you are required to set a default value of a property. This may be ``null``.

Every object has a reference to itself called ``this``. You can change parameters of an object by reference.

.. code-block:: javascript

    void function initClient() {
        class ExampleClass {
            property = null
            constructor( var parameter ) {
                this.property = expect int(parameter);
            }
        }
    }

You can't use the class name as a type. Instead use ``var`` instead. You can't ``expect`` them either.

To declare an object, do:

.. code-block:: javascript

    var exampleObject = ExampleClass(1);
    int n = exampleObject.property // n = 1
    exampleObject.property++;
    n = exampleObject.property // n = 2

Unlike other types, passing an object does not pass a copy of the object, but a reference to itself. This means that any modifications inside of a function are applied to the original object.

It's also possible to create an instance without calling the constructor.

.. code-block:: javascript

    var e = ExampleClass.instance()
    e.constructor(1) // Constructor is a normal function so you can call it manually.

Function of a class do not have a return type. Define them like this:

.. code-block:: javascript

    function func(){
        return var; // var can be of any type
    }

.. warning::

    Respawn's fork doesn't appear to support inheritance. Using the ``extend`` keyword won't compile.

    .. code-block:: javascript

        class Child extends Parent{}

Make sure you check out the squirrel documentation on `classes <http://www.squirrel-lang.org/squirreldoc/reference/language/classes.html>`_ and built in `class instance <http://www.squirrel-lang.org/squirreldoc/reference/language/builtin_functions.html#class-instance>`_ methods for more information.
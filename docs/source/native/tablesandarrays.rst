Tables, Arrays and storing values
=================================

Within squirrel there are many ways to store information, but when storing an unspecified ammount of information, or storing information on a player-by-player basis, you need to use ``arrays`` or ``tables``.

Arrays
------

Arrays can store large sets of data and are indexed using numbers, starting from 0, and are declared using ``array<type> arrayname`` the <type> identifier can be ignored but will result in the array being of the type ``var``.
  
.. code-block:: javascript

    array<int> numbers = [1,2,3,4,5,6,7,8,9,10]

    print(numbers[0])
    >>1
    print(numbers[5])
    >>6


adding and removing values from arrays can be done using ``.append(value)`` and ``.remove(index)``. 

additionally the index of values can be found using the ``.find`` function and the length by using the ``.len()`` function

.. code-block:: javascript

    array<int> numbers = [1,2,3,4,5,6,7,8,9,10]

    print(numbers.find(3))
    >>2
    print(numbers[5])
    >>6
    numbers.remove(5)
    print(numbers[5])
    >>7
    print(numbers.len())
    >>9
    array<int> empty = []
    empty.append(5)
    print(empty[0])
    >>5


Tables
------
Tables are similar to arrays but with one primary difference, rather than use a numerical index system tables allow you do define your own indexes, similar to pythons ``dict`` type.
Creation of a table is done in a similar way to arrays, however may have 2 types declared for the type of the index and the type of the content, much like arrays this will default to ``var`` if ignored

.. code-block:: javascript

    table<string, int> numberofletters = {"hello": 5}

unlike arrays however adding values to tables cannot be done using ``.append`` or similar means, as the index must also be declared, adding to tables is done using the ``<-`` operator like so.

.. code-block:: javascript

    table<entity, int> playerkills = {}
    foreach(entity player in GetPlayerArray())
        playerkills[player] <- 5


2D arrays and Tables of Arrays
------------------------------
Another attribute of tables and arrays is that they can store any value type, including tables and arrays themselves. this can be used to store an array within a table, useful if you want to store multiple values related to each index in a single variable

to create a 2d array you simply define the data type as beign an array of arrays like so.

.. code-block:: javascript

    array<array<int>> 2darray = [[1,2,3],[4,5,6],[7,8,9]]
    print(2darray[1][1])
    >>5
Structs
--------
Structs are a way of storing multiple variables in one object. To create a struct you just write

.. code-block:: javascript

    struct ExampleStruct {}
    
inside the brackets you can declare all the variables your struct should contain, you can also directly assing a standart value to a variable, if you dont override this value it will automatically be assinged.

You can not only pass variables but also functions with:``.*return type* functionref(*argument type*) *Name in the struct*``.

.. code-block:: javascript
  
    struct ExampleStruckt {
      int VariableInt
      string VariableString
      array<int> VariableArray
      int Optional = 1
      
      void functionref() ExampleVoidFuncton //you need to assing a function that returns nothing and takes no arguments
      string functionref(string) ExampleStringFunction //here you need to assing a function that returns a string and takes a string as an argument
    }
    
 You then need to creast instances of your struct to use it, like this:
.. code-block:: javascript

      void function VoidFuntion(){
        //do sth
        return
      }
      void function StringFunction(string s){
        return s
      }

      ExampleStruct structOne = {VariableInt = 1, VariableString = "Hello World", VariableArray = [1,2,3],
                                  ExampleVoidFunction = VoidFunction, ExampleStringFunction = StringFuntion, ... }
      ExampleStruct stuctTwo =  {VariableInt = 3, VariableString = "Hello Modders", VariableArray = [4,5,6],
                                  ExampleVoidFunction = VoidFunction, ExampleStringFunction = StringFuntion, Optional = 2}
      
      
Now that we have an instance we can get the values out of it like this:

.. code-block:: javascript

      print(structOne.VariableInt)
      >> 1
      print(structOne.VariableString)
      >> Hello World
      print(stuctOne.Optional)
      >> 1
      // here you can see that we did not specifically declare the variable but it still has a value that was assinged in the struct directly
      foreach(int a in structOne.VariableArray)
        print(a)
      >>1
      >>2
      >>3
      print(structOne.ExampleStringFunction("Hello"))
      >>Hello
      //in struct one we have defined that ``ExampleStringFunction`` is assinged to ``StringFunction`` so we get the output if that function as a retult
      
We can do the same thing for ``structTwo``


.. code-block:: javascript

      print(structTwo.VariableInt)
      >> 2
      print(structTwo.VariableString)
      >> Hello Modders
      print(stuctTwo.Optional)
      >> 2
      // Now that we gave Optional a value it the old one is overriten 
      foreach(int a in structTwo.VariableArray)
        print(a)
      >>4
      >>5
      >>6
      print(structTwo.ExampleStringFunction("Hello"))
      >>Hello
      //Since we gave it the same function the result is also the same

Now that we have a struct we can also pass it as an argument in functions or return the struct from a function:

.. code-block:: javascript 

    ExampleStruct function ChangeTheStruct(ExampleStruct struct){
        if(struct.VariableInt == 1)
            return struct
        else{
          struct.VariableInt = 1        
        }
        return struct
    }

In the same way you can also use it as a type for arrays or tables:

.. code-block:: javascript 

    array<ExampleStruct> StructArray = []
    StructArray.append structOne
    print(StructArray[0].VariableInt)
    >>1
    
    table<ExampleStruct, bool> StuctTable= {structOne: false}
    print(StuctTable[stuctOne])
    >>false

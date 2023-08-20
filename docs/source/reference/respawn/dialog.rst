Dialog
======

Dialogs are a way for a client to open a text window with up to 4 buttons.

Dialog struct
-------------

All the data in the struct that can be changed by the server.

===================================================       =========================================================================
Name of the struct content and standard value              description of the content
===================================================       =========================================================================
``var menu``                                              The instance of the menu
``string header``                                         The headline of the dialog
``string message``                                        The body of text under the headline, it supports newline with ``\n``
``DialogMessageRuiData &ruiMessage``                      Stores relevant RUI data
``array<int> messageColor = [161, 161, 161, 255]``        The colour of the message body, in the format of RGBA
``string image``                                          Path to the asset of the image displayed on the left of the text body
``string rightImage = $""``                               Path to the asset of the image displayed on the right of the text body
``bool forceChoice = false``                              unknown 
``bool noChoice = false``                                 unknown
``bool noChoiceWithNavigateBack = false``                 unknown
``bool showSpinner = false``                              Sets the left image as an animated spinner 
``bool showPCBackButton = false``                         Shows an additional button below all other buttons that closes the dialog for the client when pressed, works the same as pressing the ``esc`` button
``float inputDisableTime = 0``                            How long it takes before the client is able to press a button
``table<int,bool> coloredButton``                         The int is the index of the Button
``bool darkenBackground = false``                         Darkens the colour of the dialog window slightly
``bool useFullMessageHeight = false``                     Creates a larger dialog window even if there is no text or buttons to fill that space
``array<ServerDialogButtonData> buttonData``              Stores the information added by the ``AddDialogButton`` function
``array<DialogFooterData> footerData``                    Stores the information added by the ``AddDialogFooter`` function
===================================================       =========================================================================

Related structs 
---------------

DialogMessageRuiData:
^^^^^^^^^^^^^^^^^^^^^

    * string message = ""
    * vector style1Color = <1.0, 1.0, 1.0>
    * vector style2Color = <0.5, 0.5, 0.5>
    * vector style3Color = <0.5, 0.5, 0.5>
    * float style1FontScale = 1.0
    * float style2FontScale = 1.0
    * float style3FontScale = 1.0


DialogButtonData
^^^^^^^^^^^^^^^^

	* string label
	* void functionref() activateFunc
	* string focusMessage
	* bool startFocused



DialogFooterData
^^^^^^^^^^^^^^^^

	* string label
	* void functionref() activateFunc


Functions
---------

**Definition:**

.. cpp:function:: void OpenDialog( DialogData dialog )

    Shows the local player the dialog with the data from the struct.

    :param DialogData dialog: Instance of a DialogData struct

**Example:**

.. code-block::

    DialogData dialog
    dialog.message = "Hello there"
    OpenDialog( dialog )

**Definition:**

.. cpp:function:: void AddDialogButton( DialogData dialog, string text, void functionref() callback )

    Add one button to the given struct

    :param DialogData dialog: Instance of a DialogData struct

    :param string text: The Text that is shown on the button, supports some assets with ``%ASSET PATH%``

    :param void functionref() callback: Function that is executed when the button is pressed.

**Example:**

.. code-block::

    void function SendDialogWithButton()
    {
        DialogData dialog
        dialog.message = "Hello there"
        AddDialogButton(dialog, "Button 1 %%$r2_ui/menus/loadout_icons/primary_weapon/primary_kraber%%", void function():() {
            printt( "pressed button 1" )
        })
        OpenDialog( dialog )
    }

**Definition:**

.. cpp:function:: void AddDialogFooter( DialogData dialog, string text)

    Adds a footer to the dialog struct

    :param DialogData dialog: Instance of a DialogData struct

    :param string text: The Text that is shown on the button, supports some assets with ``%ASSET PATH%``


**Definition:**

.. cpp:function:: bool IsDialogActive( DialogData dialogData )

    :param DialogData dialog: Instance of a DialogData struct

    :returns: ``true`` if the dialog with that struct is currently open, otherwise it returns ``false``

Code example
------------

the folowing code produces this output: 

.. code-block::

    DialogData dialog
    dialog.header = "This is the header"
    dialog.message = "this is the body, it is green \n \n Hello There \n \n General Kenobi"
    dialog.messageColor = [0,200,0,100]
    dialog.showSpinner = true
    dialog.showPCBackButton = true
    AddDialogButton( dialog, "Button 1 %%$r2_ui/menus/loadout_icons/primary_weapon/primary_kraber%%", ButtonOnePressed )
    SendServerDialog( player, dialog )


.. figure:: /_static/serverdialog/dialogexample.png
  :align: center
  :class: screenshot

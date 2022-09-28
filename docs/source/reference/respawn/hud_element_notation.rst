.. _element-notation:

Element Notation
====

UI elements are created when a menu is initialized. References to the elements will stay the same, regardless if the menu is open or not.

It is not possible to create elements at runtime so you have to define all elements a menu or panel contains beforehand in appropriate files.

An Element is declared in the following way:

.. code-block::

    // please follow this structure
    ElementName
    {
        ControlName name
        // optional: classname, inheritance, ids ...

        // optional: other properties

        // optional: pinning
    }

If you're working on a **menu**, you need a ``menu`` object that contains all elements, for example like this:

.. code-block::

resource/ui/menus/profiles_menu.menu
{
	menu
	{
		ControlName Frame
		xpos 0
		ypos 0
		zpos 3
		wide f0
		tall f0
		autoResize 0
		visible 1
		enabled 1
		pinCorner 0
		PaintBackgroundType 0
		infocus_bgcolor_override "0 0 0 0"
		outoffocus_bgcolor_override "0 0 0 0"

        // elements
    }
}

It usually doesn't matter if you use quotation marks to assign string values to parameters.

.. cpp:data:: base

HUD & Panel files
----

The first line of a ``.menu`` or ``.res`` file needs to be the resource path to itself, starting from the resource folder.

It's not possible to load other files as menus or panels. A ``.menu`` represents an independant menu of the game, while ``.res`` files are "Panels" that can be loaded from other elements.

The rest of the file needs to be wrapped in curly brackets.

.. code-block::

    resource/ui/menus/more/folders/my_menu.menu
    {
        MyObject
        {
            // object properties go here
        }

        // more objects ...
    }

Properties
~~~~

Capitalization of the properties shouldn't matter.

.. cpp:data:: (ElementName)

    This isn't a regular property and comes **before** the opening bracket

    Unique string identifier used in scripts to look up an element. Every element is required to have a name.

Inheritance / Parenting
^^^^

.. cpp:data:: ControlName

    Controls what type of Component the element is and what parameters have an effect. Every element is required to have control name.

.. cpp:data:: InheritProperties

.. cpp:data:: controlSettingsFile

    Load a ``.res`` file. All elements in the settings file are instantiated and set as children of the element.

    ``Hud_GetChild`` only works if the parent element is (has the ``ControlName``) a **CNestedPanel**!

Identifying
^^^^
.. cpp:data:: classname

    Classname used for identifying groups of elements

.. cpp:data:: scriptID

    Set an unique integer id for this element that's retrievable in script.

Position
^^^^

.. cpp:data:: xpos

    Set the base x position relative to the element's sibling position.

    inverted when attached to the left corner or smth

.. cpp:data:: ypos

    Set the base y position relative to the element's sibling position.

    inverted when attached to the top corner or smth

.. cpp:data:: zpos

    The layer this element sits in. Elements with a higher z will be prioritized to be selected / focused. They are also drawn on top of elements with a lower z position.

Dimensions
^^^^

.. cpp:data:: wide

    Set the base width of this element.

.. cpp:data:: tall

    Set the base height of this element.

.. cpp:data:: scale

    Float that scales the element.

Text
^^^^

.. cpp:data:: labelText

    Set the label text of this element, if it is a Label.

.. cpp:data:: textAlignment

    Controls the element boundary point the element's text gets aligned with. ``east`` -> Left, ``north`` -> Top, ``west`` -> Right, ``south`` Bottom.

    You can also combine the directions like this: ``north-west``.

.. cpp:data:: allcaps

    Controls if the text of this element is rendered in all caps. Defaults to 0.

.. cpp:data:: font

    Set the text font of this element.

.. cpp:data:: textinsetx

.. cpp:data:: textinsety

.. cpp:data:: dulltext

.. cpp:data:: brighttext

.. cpp:data:: textalign

.. cpp:data:: NoWrap

    don't wrape text

.. cpp:data:: wrap

    wrap text from east

.. cpp:data:: centerwrap

    wrap text from center

.. cpp:data:: keyboardTitle

.. cpp:data:: keyboardDescription

.. cpp:data:: selectedFont

.. cpp:data:: text

.. cpp:data:: multiline

    Set if the text input supports multiline input.

.. cpp:data:: use_proportional_insets


Pinning
^^^^

.. cpp:data:: pin_to_sibling

    Controls the sibling this element will be pinned to. Takes an element's name as a parameter.

.. cpp:data:: pin_corner_to_sibling

    Sets which corner of this element is pinned to the sibling.

.. cpp:data:: pin_to_sibling_corner

    Set to which corner of the sibling this element is pinned to.

.. cpp:data:: pinCorner

Rui
^^^^

.. cpp:data:: rui

Images
^^^^

.. cpp:data:: image

.. cpp:data:: scaleImage

.. cpp:data:: fg_image

Navigation
^^^^

.. cpp:data:: navUp

.. cpp:data:: navDown

.. cpp:data:: navLeft

.. cpp:data:: navRight

Slider
^^^^

.. cpp:data:: stepSize

.. cpp:data:: isValueClampedToStepSize


Other
^^^^

.. cpp:data:: visible

    Controls if this element is rendered. Defaults to 1.

.. cpp:data:: enable

    Controls if this element starts enabled. Defaults to 1.

.. cpp:data:: auto_wide_to_contents

.. cpp:data:: auto_wide_tocontents

.. cpp:data:: auto_tall_tocontents

.. cpp:data:: drawColor

.. cpp:data:: enabled

    Controls if this element is enabled. Only enabled elements can be focused / selected. Defaults to 1.

.. cpp:data:: destination

.. cpp:data:: frame

.. cpp:data:: fieldName

.. cpp:data:: autoResize

.. cpp:data:: tabPosition

.. cpp:data:: barCount

.. cpp:data:: barSpacing

.. cpp:data:: dialogstyle

.. cpp:data:: style

.. cpp:data:: command

.. cpp:data:: ActivationType

.. cpp:data:: paintbackground

.. cpp:data:: tabposition

.. cpp:data:: activeInputExclusivePaint

.. cpp:data:: paintborder

.. cpp:data:: CircularEnabled

.. cpp:data:: CircularClockwise

.. cpp:data:: consoleStyle

.. cpp:data:: unicode

.. cpp:data:: Default

.. cpp:data:: selected

.. cpp:data:: maxchars

.. cpp:data:: listName

.. cpp:data:: arrowsVisible

.. cpp:data:: verifiedColumnWidth

.. cpp:data:: nameColumnWidth

.. cpp:data:: totalMembersColumnWidth

.. cpp:data:: centerWrap

.. cpp:data:: chatBorderThickness

.. cpp:data:: messageModeAlwaysOn

.. cpp:data:: interactive

.. cpp:data:: rowHeight

.. cpp:data:: nameSpaceX

.. cpp:data:: nameSpaceY

.. cpp:data:: micWide

.. cpp:data:: micTall

.. cpp:data:: micSpaceX

.. cpp:data:: micOffsetY

.. cpp:data:: textHidden

.. cpp:data:: editable

.. cpp:data:: NumericInputOnly

.. cpp:data:: allowRightClickMenu

.. cpp:data:: allowSpecialCharacters

.. cpp:data:: Command

.. cpp:data:: SelectedTextColor

.. cpp:data:: SelectedBgColor

.. cpp:data:: clip

.. cpp:data:: teamRelationshipFilter

.. cpp:data:: activeColumnWidth

.. cpp:data:: happyHourColumnWidth

.. cpp:data:: onlinePlayersColumnWidth

.. cpp:data:: PaintBackgroundType

    // 0 for normal(opaque), 1 for single texture from Texture1, and 2 for rounded box w/ four corner textures

.. cpp:data:: ConVar

.. cpp:data:: alpha

.. cpp:data:: conCommand

.. cpp:data:: minValue

.. cpp:data:: maxValue

.. cpp:data:: inverseFill

.. cpp:data:: syncedConVar

.. cpp:data:: showConVarAsFloat

.. cpp:data:: modal

.. cpp:data:: headerHeight

.. cpp:data:: panelBorder

.. cpp:data:: linespacing

.. cpp:data:: rightClickEvents

.. cpp:data:: conCommandDefault

Conditional Properties
~~~~

You can declare properties for specific conditions by adding ``[CONDITION]`` after the property value.

Usable conditions are:

* $WIN32

    game is running on 32 bit windows

* $WINDOWS

    game is running on windows

* $DURANGO

    game is running on xbox

* $PS4

    game is running on a PS4

* $GAMECONSOLE

* $WIDESCREEN_16_9

    game resolution is 16/9

* $any language ...

    the game's language.

On top of that, logical operators like ``!``, ``&&`` and ``||`` are available as well.

Example:
^^^^

    .. code-block::

        LoadingTip
        {
            ControlName				Label
            ypos					10
            wide					1630 [$WIDESCREEN_16_9]
            wide					1441 [!$WIDESCREEN_16_9]
            auto_tall_tocontents	1
            labelText				""
            textalign				"north-west"
            font					Default_28
            wrap 					1
            fgcolor_override 		"217 170 75 255"
            visible					0

            pin_to_sibling			LoadingGameMode
            pin_corner_to_sibling	TOP_LEFT
            pin_to_sibling_corner	BOTTOM_LEFT
        }

Pinning
~~~~

* ``CENTER``

    The calculated center of the element

* ``TOP``

    Element's top y bounds, x axis center.

* ``BOTTOM``

    Element's lowest y bounds, x axis center.

* ``LEFT``

    Element's lowest x bounds, y axis center.

* ``RIGHT``

    Element's highest x bounds, y axis center.

* ``TOP_LEFT``

    Top left corner

* ``TOP_RIGHT``

    Top right corner

* ``BOTTOM_LEFT``

    Bottom left corner

* ``BOTTOM_RIGHT``

    Bottom right corner

Units
^^^^

You can calculate the position or dimensions etc. with different units. If you provide no extra unit, the game uses pixels.

* %x

    x percent of the screen.

    .. code:block::

        // cover the entire screen
        width   %100
        height  %100

* fx

    use 100%

* c+/-x

    something with the screen edges not exactly sure how positions get calculated
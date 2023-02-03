Rst Help
=====

Documentation on rst can be difficult for many reasons. 
So this page to help smooth the entry difficulty curve so enable more contributions.
You will still need to read rst external documentation, but this page holds useful links, resources, code blocks, and explanations.


..  note:: The ``.rst`` files can be found in the ``docs/source`` directory. If you're adding a new file, make sure to link it in ``index.rst``

External Rst Documentation:
^^^^

Take links rankings lightly as every rst documentation provides value and presents information differently.

.. note:: Rst syntax and capability can change depending on extensions the documentation has.

1. Docutil: `https://docutils.sourceforge.io/docs/ref/rst/directives.html <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_
2. Spinx Documentation: `https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
3. Thomas Cokelaer: `https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.htmlr <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_
4. Python DevGuide: `https://devguide.python.org/documentation/markup/ <https://devguide.python.org/documentation/markup/>`_
5. GDAL: `https://gdal.org/contributing/rst_style.html <https://gdal.org/contributing/rst_style.html>`_
6. Spinx-RTD-Theme: `https://sphinx-rtd-theme.readthedocs.io/en/stable/demo/demo.html#paragraph-level-markup <https://sphinx-rtd-theme.readthedocs.io/en/stable/demo/demo.html#paragraph-level-markup>`_
7. Anaconda: `https://docs.anaconda.com/restructuredtext/detailed/ <https://docs.anaconda.com/restructuredtext/detailed/>`_

Headers, Sections, Subsections, Subsubsections:
----

.. important:: You need 5 specific symbols in a row to indicate a header type. 

Standard and always applicable headers:
#####

1. ``=`` Title
2. ``^`` Subsection
3. ``-`` Subsubsection

Headers work much like a hierarchy. Having multiple Header 1's (``=``) on one page will likely break other headers, applicable to other headers.

**Examples:**

The example below is a screenshot. This removes their hyperlinks, removing some functionality through this example.
Should be of similar size though.

.. figure:: /_static/rsthelp/staticHeaders.png
    :width: 220
    :align: left
    :figwidth: 220

::

    Title
    =====

    Subsection
    ^^^^^

    Subsubsection
    -----


Based off reference:
#####

These headers all indicate a header style with no specific size. 
The initial use of them will indicate their size for the rest of the page.
Depending on the header previous used before them, they will auto-scale to a sub version. 

Recommended order:
*****

- ``#``
- ``*``
- ``~``
- ``+``

**Examples:**

Subsubsection = Sub^2
-----

Sub^3
#####

Sub^4
*****

Sub^5
~~~~~

Sub^6
+++++

::

    Subsubsection = Sub^2
    -----

    Sub^3
    #####

    Sub^4
    *****

    Sub^5
    ~~~~~

    Sub^6
    +++++

Sources: `https://gdal.org/contributing/rst_style.html#sections <https://gdal.org/contributing/rst_style.html#sections>`_, 

Links:
-----

TODO - Single use, and Indexed links.

Figures and Images:
-----

.. important:: Resize images and images within figures with ``:width:``, ``:height:``, or ``:scale:``.

Figures are kind of like their own section/area on the page. 
Blah Blah Blah, we can do more with figures, basically whatever you can do with images but a little more.
Figures support captions.

Captions:
#####

Figures:
*****

.. figure:: /_static/rsthelp/cutecat1x1.png
    :width: 250
    :figwidth: 250

    hello i'm a caption.

Images attempting:
#####

.. image:: /_static/rsthelp/cutecat1x1.png
    :height: 250
    :align: center

no captions

Syntax:
#####

Figure:

::

    .. figure:: /_static/folder/image.ext
        :width: int or px
        :height: int or px
        :figwidth: int, px, or percent
        :scale: int or percent

        Caption?

        :: 

            or even other crazy stuff (this is a codeblock)

Image:

::

    .. image:: /_static/folder/image.ext
        :width: int or px
        :height: int or px
        :scale: int or percent

Figures doing a little more:
#####

This single figure is holding an image, codeblock, text, and even a table.

.. figure:: /_static/rsthelp/cutecat1x1.png
    :width: 250
    :figwidth: 250

    Caption with~

    :: 

        a code block!!!

    even another image!!! (nested)

    .. figure:: /_static/rsthelp/cutecat1x1.png
        :scale: 20

    also tables.

    +---------+---------+---------+
    | isn't   | that    |   cool? |
    +---------+---------+---------+

Aligning is weird:
#####

See this aligned image?

.. image:: /_static/rsthelp/cutecat1x1.png
    :align: right
    :width: 250px

It seems nice because it causes all the text to bundle up here to the left or right.
This could improve readability but aligned content can make writing the documentation more difficult.
The text and content may be misaligned so you just end desyncing up your documentation for the reader.

Like now. The previous text has nothing to do with the cute cat. Now that we're talking about the cat though.
Isn't that cat cute? Imagine sleeping that good. Maybe it's napping.
I wonder if the ratio of cute sleeper are higher for cats than for humans.

Anyways.

.. important:: You can align with ``:align: <parameter>``, available parameters are ``right``, ``left``, ``center``, ``top``, ``middle`` or ``bottom``.

Sources: `https://docutils.sourceforge.io/docs/ref/rst/directives.html#images <https://docutils.sourceforge.io/docs/ref/rst/directives.html#images>`_, `https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#images-and-figures <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#images-and-figures>`_

Admonitions:
-----

These are warnings or hazard statements.

Examples:
#####

.. attention:: This is done ``.. attention:: YOUR_TEXT HERE``
.. danger:: This is done ``.. danger:: YOUR_TEXT HERE``
.. error:: This is done ``.. error:: YOUR_TEXT HERE``
.. caution:: This is done ``.. caution:: YOUR_TEXT HERE``
.. warning:: This is done ``.. warning:: YOUR_TEXT HERE``
.. note:: This is done ``.. note:: YOUR_TEXT HERE``
.. important:: This is done ``.. important:: YOUR_TEXT HERE```
.. hint:: This is done ``.. hint:: YOUR_TEXT HERE``
.. tip:: This is done ``.. tip:: YOUR_TEXT HERE``
or topics which are very similar to admonitions.

.. topic:: Topic/Title

    Description

Source: `https://docutils.sourceforge.io/docs/ref/rst/directives.html#admonitions <https://docutils.sourceforge.io/docs/ref/rst/directives.html#admonitions>`_

References:
-----

TODO - REALLY great for tables. Basically text links (i haven't done much testing).

Example:
::

    .. |title| replace::
        This is realllllly useful for tables. This is reference usage.

This is used right now. Check below for usage in example tables.

.. |title| replace::
        This is realllllly useful for tables. This is reference usage.

Tables:
-----

TODO - Tables. Before learning tables. Learn References.

Types: 
#####

Simple Simple:
::

    ====== ====== ============================
     hi     elo      IM A Table
    ====== ====== ============================

====== ====== ============================
 hi     elo      IM A Table
====== ====== ============================

Simple: 
:: 

    ====== ====== ============================
    hi     elo     Titles
    ====== ====== ============================
    hi     elo      |title|
    ====== ====== ============================

====== ====== ============================
 hi     elo     Titles
====== ====== ============================
  hi     elo      |title|
====== ====== ============================

Complex Complex:

TODO

Complex:

TODO

Complex Easiest:

TODO

.. image:: /_static/rsthelp/mpt.png
    :height: 40
.. danger:: **DANGER ZONE BELOW**
.. danger:: **DANGER ZONE BELOW**
.. danger:: **DANGER ZONE BELOW**
.. danger:: **DANGER ZONE BELOW**
.. danger:: **DANGER ZONE BELOW**
.. image:: /_static/rsthelp/mpt.png
    :height: 40

DANGER ZONE
^^^^^

.. sidebar:: Sidebar Title
    :subtitle: Optional Sidebar Subtitle

    Subsequent indented lines comprise
    the body of the sidebar, and are
    interpreted as body elements.

Titles, Sections, and Header being funny:
----

.. sidebar:: My preferred order
    
    ::

        Subsubsection = Sub^2
        -----

        Sub^3
        #####

        Sub^4
        *****

        Sub^5
        ~~~~~

        Sub^6
        +++++

My preferred order:
^^^^^

The problem is that these secondary subtitles change depends on when they are placed according to previous titles and sections.

Subsubsection = Sub^2
-----

Sub^3
#####

Sub^4
*****

Sub^5
~~~~~

Sub^6
+++++

.. image:: /_static/rsthelp/mpt.png
    :height: 60

WHAT???? FORCED INDENTS?????

No. Just a blank png resized accordingly.

.. sidebar:: Breaking my order
    
    ::

        Subsubsection = Sub^2
        -----

        Sub^3
        *****

        Sub^4
        ~~~~~

        Sub^5
        #####

        Sub^6
        +++++

Breaking my order:
^^^^^

They also carry their perspective size throughout your one page. So if you don't remember your order then your titles and headers will break moving forward.
As you can see below. I break the order. Which you can see I broke according the sidebars (the bars on the side of the page).

Subsubsection = Sub^2
-----

Sub^3
*****

Sub^4
~~~~~

Sub^5
#####

Sub^6
+++++

.. image:: /_static/rsthelp/mpt.png
    :height: 20

See? It's broken. Doesn't work if you try to break the trend you created in the page.

.. image:: /_static/rsthelp/mpt.png
    :height: 50

Tables :O
^^^^^

========================== ======================                           
Text Format                Rst Format                         
========================== ======================                         
Subsubsection = Sub^2      Subsubsection = Sub^   
a                                                
a                                                  
========================== ======================     

====================== =
Title                  a
====================== =
Desc                   a
====================== =




+----------------------+------------+
| Symbol               | Meaning    |
+======================+============+
| Title                | Campground |
+----------------------+------------+
|  complex             | Lake       |
+----------------------+------------+
|   table struct       | Mountain   |
+----------------------+------------+

+---------+-----------+
| |cat|   | |title|   |
+---------+-----------+

.. |title| replace::
    This is realllllly useful for tables. This is reference usage.

.. |cat| replace::
    see?

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
=====  =====  ======
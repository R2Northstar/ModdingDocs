Contributing to ModdingDocs
===========================

All contributions to ModdingDocs are welcome. To add a change simply make a pull request to the `ModdingDocs repo <https://github.com/R2Northstar/ModdingDocs/>`_.

ModdingDocs uses `reStructuredText <https://en.wikipedia.org/wiki/ReStructuredText>`_.

A cheatsheet for reStructuredText syntax can be found here: https://docs.generic-mapping-tools.org/6.2/rst-cheatsheet.html

The ``.rst`` files can be found in the ``docs/source`` directory. If you're adding a new file, make sure to link it in ``index.rst``

Contributing without a local build
^^^^^
You don't necessarily need to set up a local build environment.

To contribute without doing so, you can just edit the files in an editor of your choice and create a GitHub pull request from them.

There will be a test-build done for each PR, which you can find on your PR as a "Check" by clicking ``show all checks`` and ``details``.

This should take you to a online version of the docs with your PRs changes. 


Building locally
^^^^^

First, you need to have a relatively recent version of Python installed - 3.8 or higher. `Download here <https://www.python.org/downloads/>`_

tl:dr;
-----

.. tabs::

    .. code-tab:: powershell Windows

        git clone https://github.com/R2Northstar/ModdingDocs/
        cd ModdingDocs
        py -m pip install poetry
        py -m poetry install
        py -m poetry run build
    
    .. code-tab:: bash Linux

        git clone https://github.com/R2Northstar/ModdingDocs/
        cd ModdingDocs
        python3 -m pip install poetry
        python3 -m poetry install
        python3 -m poetry run build

Explanation
-----

Open a terminal wherever you want the files to end up and clone the `ModdingDocs repo <https://github.com/R2Northstar/ModdingDocs/>`_, e.g.


.. code:: bash

    git clone https://github.com/R2Northstar/ModdingDocs/
    cd ModdingDocs

Your terminal should now be open in the ModdingDocs folder.

Next, you need to install `Poetry <https://python-poetry.org/docs/cli/>`_, the dependency management and build tool used:

.. tabs::

    .. code-tab:: powershell Windows
        
        py -m pip install poetry
        
    .. code-tab:: bash Linux

        python3 -m pip install poetry

Now, tell poetry to install this project and its dependencies.

.. tabs::

    .. code-tab:: powershell Windows
        
        py -m poetry install
        
    .. code-tab:: bash Linux

        python3 -m poetry install


After this is done downloading and setting up all the dependencies, you can build it with:


.. tabs::

    .. code-tab:: powershell Windows
        
        py -m poetry run build
        
    .. code-tab:: bash Linux

        python3 -m poetry run build


This should rebuild the docs on changes and open them in your default browser with live reloading.


VSCode
^^^^^

If you're using `Visual Studio Code <https://code.visualstudio.com/>`_, the following extensions might be of interest:


- `snekvik.simple-rst <https://marketplace.visualstudio.com/items?itemName=trond-snekvik.simple-rst>`_: for syntax highlighting
- `lextudio.restructuredtext <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_: for autocompletion and syntax checks.

.. note::
    To get the ReStructuredText support working, you will likely need to tell VSCode to use the Poetry environment.

    To do so, open one of the .py files, which should make the python version appear in the bottom right of VSCode.

    Click on it, and select the version with ``(moddingdocs`` after it.

    Then, when looking at a ReStructuredText file there should be ``esbonio:`` in the bottom right.

    Click that to restart the ReStructuredText support. This allows it to see all the dependencies Poetry installed.

Rst Help
^^^^^

Documentation on rst can be difficult for many reasons. 
So this page to help smooth the entry difficulty curve so enable more contributions.
You will still need to read rst external documentation, but this page holds useful links, resources, code blocks, and explanations.

.. note:: 
    Rst syntax and capability can change depending on extensions the documentation has.

External Rst Documentation:
-----

Take links rankings lightly as every rst documentation provides value and presents information differently. 

1. Docutil: `https://docutils.sourceforge.io/docs/ref/rst/directives.html <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_
2. Spinx Documentation: `https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
3. Thomas Cokelaer: `https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.htmlr <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_
4. Python DevGuide: `https://devguide.python.org/documentation/markup/ <https://devguide.python.org/documentation/markup/>`_
5. GDAL: `https://gdal.org/contributing/rst_style.html <https://gdal.org/contributing/rst_style.html>`_

.. note:: 
    Newlines and Indent less so, are very important when writing documentation in rst (You'll be hitting enter a lot).

Headers, Sections, Subsections, Subsubsections:
----

You need 5 specific symbols in a row to indicate a header type. 


Standard and always applicable headers:
#####

1. ``=`` Title
2. ``^`` Subsection
3. ``-`` Subsubsection

**Examples:**

Title
=====

Subsection
^^^^^

Subsubsection
-----

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
Depending on the header previous used before them, they will auto-scale to a sub version.

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

Figures and Images:
-----

.. important:: Resize images and images within figures with ``:width:``, ``:height:``, or ``:scale:``.

Figures are kind of like their own section/area on the page. 
Blah Blah Blah, we can do more with figures, basically whatever you can do with images but a little more.
Figures support captions.

Figures with captions:
#####

.. figure:: /_static/contributing/cutecat1x1.jpg
    :width: 250
    :figwidth: 250

    hello i'm a caption.

Images attempting captions:
#####

.. image:: /_static/contributing/cutecat1x1.jpg
    :height: 250
    :align: center

no captions

Aligning is weird:
#####

This aligned image

.. image:: /_static/contributing/cutecat1x1.jpg
    :align: right
    :width: 200px

It seems nice but it causes all the text to bundle up here to the left or right.
Still workable just causes unnecessary confusion because the documentation you're writing.
May not go along with the image it's right beside.

Like now. The previous text has nothing to do with the cute cat here to the right.
Isn't that cat cute? Imagine sleeping that good. Maybe it's napping.
I wonder if the ratio of cute sleeper are higher for cats than for humans.

Anyways: 

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


Source: `https://docutils.sourceforge.io/docs/ref/rst/directives.html#admonitions <https://docutils.sourceforge.io/docs/ref/rst/directives.html#admonitions>`_




.. danger:: TEST RST STUFF BELOW
.. danger:: TEST RST STUFF BELOW
.. danger:: TEST RST STUFF BELOW
.. danger:: TEST RST STUFF BELOW
.. danger:: TEST RST STUFF BELOW
.. danger:: TEST RST STUFF BELOW

.. sidebar:: Example
    
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

Example
-----

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

.. figure:: nope

not a side bar

:: 

    code Example

.. sidebar:: Sidebar Title
    :subtitle: Optional Sidebar Subtitle

    Subsequent indented lines comprise
    the body of the sidebar, and are
    interpreted as body elements.

+----------------------+------------+
| Symbol               | Meaning    |
+======================+============+
| Title                | Campground |
+----------------------+------------+
| .. image:: waves.png | Lake       |
+----------------------+------------+
| .. image:: peak.png  | Mountain   |
+----------------------+------------+

+---------+-----------+
| |cat|   | |title|   |
+---------+-----------+

.. |title| replace::
    This is wacky

+---------+-----------+
| |cat|   | |title0|  |
+---------+-----------+

.. |title0| replace::
    shitty walks


`<https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_

.. sidebar:: Sidebar Title
    :subtitle: Optional Sidebar Subtitle

    Subsequent indented lines comprise
    the body of the sidebar, and are
    interpreted as body elements.

    |cat|

    :: 

        please works things

.. sidebar:: Example

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


Title Text lol get super duper awesome funny man Title Text lol get super duper awesome funny man Title Text lol get super duper awesome funny man

Title
-----

so a longer thing to do about the funny this anand i'm just trying to type and say things.

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
=====  =====  ======

.. _Title: what the flip
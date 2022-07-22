Contributing to ModdingDocs
===========================

All contributions to ModdingDocs are welcome. To add a change simply make a pull request to the `ModdingDocs repo <https://github.com/R2Northstar/ModdingDocs/>`_.

ModdingDocs uses `reStructuredText <https://en.wikipedia.org/wiki/ReStructuredText>`_.

A cheatsheet for reStructuredText syntax can be found here: https://docs.generic-mapping-tools.org/6.2/rst-cheatsheet.html

Contributing without a local build
----------------------------------
You don't necessarily need to set up a local build environment.

To contribute without doing so, you cant just edit the files in an editor of your choice and create a github PR from them.

There will be a test-build done for each PR, which you can find on your PR as a "Check" by clicking ``show all checks`` and ``details``.

This should take you to a online version of the docs with your PRs changes. 


Setting up the build environment for docs
-----------------------------------------


First, you need to have a relatively recent version of Python installed - 3.8 or higher. `Download here <https://www.python.org/downloads/>`_

Clone the `ModdingDocs repo <https://github.com/R2Northstar/ModdingDocs/>`_, e.g.


.. code:: bash

    git clone https://github.com/R2Northstar/ModdingDocs/


Opened the clone repo.

(on Windows, replace `python3` with `py`)


.. code:: bash

    # Install Poetry, the build tool used by ModdingDocs
    python3 -m pip install poetry


Then all you need to do is tell poetry to run the build script. This will run a local webserver and open the docs in your default browser.


.. code:: bash

    # let poetry take care of it!
    poetry run build


Tips and tricks
---------------

If you're using `Visual Studio Code <https://code.visualstudio.com/>`_, the following extensions might be of interest:


- `snekvik.simple-rst <https://marketplace.visualstudio.com/items?itemName=trond-snekvik.simple-rst>`_: for syntax highlighting
- `lextudio.restructuredtext <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_: for autocompletion and syntax checks.

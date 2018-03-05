==============
My Toy Package
==============


.. image:: https://img.shields.io/pypi/v/my_toy_package.svg
        :target: https://pypi.python.org/pypi/my_toy_package

.. image:: https://img.shields.io/travis/francois-durand/my_toy_package.svg
        :target: https://travis-ci.org/francois-durand/my_toy_package

.. image:: https://readthedocs.org/projects/my-toy-package/badge/?version=latest
        :target: https://my-toy-package.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/francois-durand/my_toy_package/shield.svg
     :target: https://pyup.io/repos/github/francois-durand/my_toy_package/
     :alt: Updates

My Toy Package shows how to use Cookiecutter.

* Free software: GNU General Public License v3
* Documentation: https://my-toy-package.readthedocs.io.

The following walk-through is a checklist of how to create and maintain your Python package, especially relying on
Cookiecutter, by Audrey Roy Greenfeld, and PyCharm.

-------------------
Create your package
-------------------

This section is adapted from: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html .

Preliminaries
=============

Ensure that you have accounts (preferably with the same login) on:

* GitHub_,
* ReadTheDocs_,
* PyPI_,
* Travis-CI_,
* Pyup_.

.. _GitHub: https://github.com
.. _ReadTheDocs: https://readthedocs.org
.. _PyPI: https://pypi.python.org/pypi
.. _Travis-CI: https://travis-ci.org
.. _Pyup: https://pyup.io

Install Cookiecutter
====================

In a terminal (e.g. Anaconda Prompt)::

    pip install cookiecutter

Or, if you prefer::

    easy_install cookiecutter

Generate Your Package
=====================

#. Your project will need a project name (e.g. *My Toy Package*) and a project slug (typically ``my_toy_package``).
   Before starting, check that your project slug is not used in PyPI.
#. In a terminal (e.g. Anaconda Prompt):

   #. Go to your GitHub directory, e.g. ``D:\GitHub\``.
   #. ``cookiecutter https://github.com/audreyr/cookiecutter-pypackage.git``
   #. Answer the questions. Here is an example (some explanations follow)::

        full_name [Audrey Roy Greenfeld]: François Durand
        email [aroy@alum.mit.edu]: fradurand@gmail.com
        github_username [audreyr]: francois-durand
        project_name [Python Boilerplate]: My Toy Package
        project_slug [my_toy_package]:
        project_short_description [Python Boilerplate contains all the boilerplate
        you need to create a Python package.]: My Toy Package shows how to use
        Cookiecutter.
        pypi_username [francois-durand]:
        version [0.1.0]:
        use_pytest [n]: y
        use_pypi_deployment_with_travis [y]:
        add_pyup_badge [n]: y
        Select command_line_interface:
        1 - Click
        2 - No command-line interface
        Choose from 1, 2 [1]:
        create_author_file [y]:
        Select open_source_license:
        1 - MIT license
        2 - BSD license
        3 - ISC license
        4 - Apache Software License 2.0
        5 - GNU General Public License v3
        6 - Not open source
        Choose from 1, 2, 3, 4, 5, 6 [1]: 5

Some explanations now:

* ``use_pytest``: there are essentially three ways to do unit tests in Python: unittest (the standard solution),
  pytest (another test package) and doctest (where tests are integrated in the docstrings). If you are new to
  testing, I suggest using doctest. But even so, pytest is useful to configure your tests (as we will do a bit
  later). For this reason, my advice is to answer yes.
* ``use_pypi_deployment_with_travis``: when you will do a *release* in GitHub, Travis will automatically release
  your package on PyPI.
* ``add_pyup_badge``: a pyup badge will appear in the readme of your package.
* ``Click``: this allows you to easily call your program with unix-style command, e.g. ``python my_program.py --help``
  You can answer yes, even if you do not use it for the moment.
* ``create_author_file``: I suggest to answer yes.

Create the PyCharm Project
==========================

In PyCharm:

#. Create new project.
#. In ``Location'', fetch the directory of your project, e.g. ``D:\GitHub\my_toy_package``. Validate.
#. Warning that the directory is not empty: validate.
#. Menu File -> Settings -> Project -> Project Interpreter.
#. Click on the gear -> Add local
#. Fill in the form: New environment using Virtualenv. This directory proposed is just fine. Validate.
#. Open the file ``.gitignore`` (you can do so in PyCharm).

    #. Add these lines (e.g. at the end of the file)::

        # PyCharm project settings
        .idea

    #. Check that ``venv`` is also excluded.

-------
Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage


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

* Free software: GNU General Public License v3.
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
#. In *Location*, fetch the directory of your project, e.g. ``D:\GitHub\my_toy_package``. Validate.
#. Warning that the directory is not empty: validate.
#. Menu File → Settings → Project → Project Interpreter.
#. Click on the gear → Add local.
#. Fill in the form: New environment using Virtualenv. This directory proposed is just fine. Validate.
#. Open the file ``.gitignore`` (you can do so in PyCharm).

   #. Add these lines (e.g. at the end of the file)::

         # PyCharm project settings
         .idea

   #. Check that ``venv`` is also excluded.

Create the GitHub Repo
======================

In PyCharm:

#. If it is not already done, register your GitHub account in PyCharm:

   #. Menu File → Settings → Version Control → GitHub.
   #. Choose Auth type → password.
   #. Fill in the form and validate.

#. Menu VCS → Import into version control → Share project on GitHub.

#. Fill in the form and validate, e.g.::

      New repository name: my_toy_package
      Remote name: origin
      Description: My Toy Package shows how to use cookiecutter.

In a browser, you can go to your GitHub account to check that everything is there.

Install Dev Requirements
========================

In the PyCharm terminal:

#. Ensure you are in the directory of your package (e.g. ``D:\GitHub\my_toy_package``).
#. Ensure that your virtual environment is activated: there should be ``(venv)`` at the beginning of the line. If not::

      venv\Scripts\activate

#. ``pip install -r requirements_dev.txt``

Install Your Package in "Development Mode"
==========================================

This way, your package behaves as if it were installed, but any change you make will have effect immediately.
In the PyCharm terminal, you should still be in the directory of your package, with your virtual environment activated.
Do::

   python setup.py develop

Set Up Travis CI
================

Ensure that Travis CLI is installed on your computer.

* Under Windows:

   #. Install Ruby (https://rubyinstaller.org/ ).
   #. In PyCharm terminal, do: ``gem install -V travis --no-rdoc --no-ri``.

* Under Debian, run as root::

   apt-get update
   apt-get install cookie-cutter ruby ruby-dev gcc
   gem install -V travis --no-rdoc --no-ri

If you experience troubles installing travis, cf. https://github.com/travis-ci/travis.rb#installation.

Once Travis CLI is installed:

#. On Travis website:

   #. Login using your Github credentials.
   #. It may take a few minutes for Travis CI to load up a list of all your GitHub repos. They will be listed with
      boxes to the left of the repo name, where the boxes have an X in them, meaning it is not connected to Travis CI.
      Add the public repo to your Travis CI account by clicking the X to switch it “on” in the box next to the
      ``my_toy_package`` repo. Do not try to follow the other instructions, that will be taken care of next.

#. In PyCharm terminal, ensure that you are in the directory of your project and::

      travis encrypt --add deploy.password "My PyPI password"

   (replace with your actual password, in quotation marks).

#. Open the file ``.travis.yml`` (you can do so in PyCharm).

   #. Check that ``deploy.password.secure`` is encoded.
   #. Suppress the line ``- 2.7`` (unless you plan to write code that is compatible with Python 2.7).

Set Up ReadTheDocs
==================

#. On ReadTheDocs website:

   #. Paramètres → Comptes liés. Check that your GitHub account is listed here.
   #. Go to “My Projects”. Import a Project → Importer manuellement. Fill in the form and validate, e.g.::

         my_toy_package
         https://github.com/francois-durand/my_toy_package
         Git

   #. Admin → Advanced settings.

      #. Check "Installer votre projet dans un virtualenv via setup.py install".
      #. In "Python interpreter", choose "CPython 3.x".

#. In PyCharm, commit/push, i.e.:

   #. Menu VCS → Commit.
   #. Enter a commit message, e.g. ``Initial settings``.
   #. Commit → Commit and push.
   #. Push.

Set Up Pyup
===========

#. On Pyup website:

   #. Click on the green *Add Repo* button and select the repo you created.
   #. A pop up appears. Personally, I checked the first item and unchecked the two others.

   Within a few minutes, you will probably receive a pull request in GitHub (and in your email).

#. On GitHub website:

   #. Accept merge.
   #. Delete branch.

#. In PyCharm, menu VCS → Update project. This does a git update (to get the modifications done by Pyup).

Add the Example Files
=====================

#. On GitHub website, download `My Toy Package`_.
#. In a terminal or file explorer:

   #. Move the directories ``my_toy_package\my_toy_package\SubPackage1`` and ``my_toy_package\my_toy_package\SubPackage2``
      into the corresponding places of your project.
   #. Move the file ``my_toy_package\docs\reference`` into the corresponding place of your project.
   #. You can throw away the other files you downloaded.

#. In PyCharm:

   #. Right-click on the files you added. Git → Add.
   #. In the file ``MyClass1``, replace ``my_toy_package`` with the name of your package.
   #. Manually modify the copyright statement in files ``MyClass1``, ``MyClass2`` and ``MyClass3``.
   #. In the file ``reference``, replace ``my_toy_package`` with the name of your package.
   #. In the file ``index.rst``, just after the line ``usage``, add ``reference``.
   #. In the file ``__init__.py``, add the following shortcuts::

         from .SubPackage1.MyClass1 import MyClass1
         from .SubPackage2.MyClass2 import MyClass2
         from .SubPackage2.MyClass3 import MyClass3

   #. In the file ``setup.py``, remove the two lines about Python 2 (unless you plan to write code that is compatible
      with Python 2).

.. _`My Toy Package`: https://github.com/francois-durand/my_toy_package


Add a Run Configuration for Doctest
===================================

In PyCharm:

#. Menu Run → Edit Configurations.
#. Add a new configuration by clicking the + button → Python tests → py.test.
#. Give a name to the configuration, e.g. ``All tests``.
#. In *Additional Arguments* field, add ``--doctest-modules``.
#. Ignore the warning and validate.

Run this configuration: normally, it runs all the tests of the project.

Check that Everything is Working
================================

#. In PyCharm: commit/push.
#. In Travis CI: go to Current. The build should be a success (it may take several minutes).
#. In ReadTheDocs:

   #. In *Compilations*, the doc should be *transmis*.
   #. Open the documentation.
   #. In the table of contents, click on the first page (e.g. *My Toy Package*). You should have four *badges*:

      #. PyPI: invalid (there will be the version number after your first release).
      #. Build: passing.
      #. Docs: passing.
      #. Pyup: up-to-date.

   #. In the table of contents, click on *Reference*. You should see the doc of your functions.

If you wish, you are now ready to release your first version (cf. below).

-------------------------------
During the Life of Your Package
-------------------------------

Release a Version
=================

In PyCharm:

#. Update the file ``HISTORY.rst``.
#. In PyCharm terminal, do one of the following:

   * ``bumpversion patch`` (version x.y.z → x.y.(z+1)) when you made a backwards-compatible modification (such as a
     bug fix).
   * ``bumpversion minor`` (version x.y.z → x.(y+1).0) when you added a functionality.
   * ``bumpversion major`` (version x.y.z → x+1.0.0) when you changed the API. Note: in versions 0.y.z, the API is not
     expected to be stable anyway.

#. Commit.
#. Menu VCS → Git → Tag. Add a tag name (e.g. ``v0.1.0``) and a message (e.g. ``First stable version``).
#. Push. The box *Push tags* must be ticked.

After a few minutes, Travis CI has finished the built and it is deployed on PyPI.

Add a Module (= a File)
=======================

Typically, this is a file ``SubPackage\MyClass``, containing class ``MyClass``.

#. In the file ``__init__.py``: add the shortcut.
#. In the file ``reference.rst``: add the auto-documentation.

Use a Third-Party Package
=========================

For example, you want to use Numpy in your module.

In the file ``setup.py``, in the list ``requirements``, add the name of the package (e.g. ``'numpy``).

When You Receive a Pull Request from Pyup
=========================================

#. In GitHub website:

   #. Open the pull request.
   #. If necessary, wait until Travis CI has finished the build, so that you know there is no problem.
   #. Merge pull request.
   #. Confirm merge.
   #. Delete branch.
   #. In the front page, you Pyup badge should be up-to-date. If not, this is probably just a matter of time.
      You can go to the Pyup website, click on the gear → reload.

#. In PyCharm, Menu VCS → Update project.

-------
Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

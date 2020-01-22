========
Tutorial
========

In the end, here is how it will work.

* You use the PyCharm IDE. It is configured to run tests and generate the documentation of your package locally.

* Your project is on GitHub. When you push modifications to GitHub:

    * Travis CI automatically runs all the tests and checks that everything is working on several versions of Python
      (e.g. 3.5, 3.6, 3.7)
    * Codecov enables you to see what parts of your code are covered or not by your tests.
    * ReadTheDocs automatically generates the documentation and publishes it online.

* When you "tag" a version on GitHub, in other words when you "draft a release": Travis CI not only performs
  the tests but also generates the distribution files of your package and publishes them on PyPI. As a consequence,
  any Python user will be able to install you package via ``pip install the_name_of_your_package``.

* Generally, you use some external packages during the development process of your own package, for example ``sphinx``,
  ``pytest``, etc. These packages and their versions are listed in the file ``requirements_dev.txt`` of your package, so
  that each member of your team know which version is used. PyUp informs you when a new version of these
  third-party packages are released: you receive a pull request in GitHub and you just have to accept it.

-------------
Preliminaries
-------------

Create accounts on the websites
===============================

Ensure that you have accounts (preferably with the same login) on:

* GitHub_,
* ReadTheDocs_,
* PyPI_,
* Travis-CI_,
* Codecov_,
* Pyup_.

.. _GitHub: https://github.com
.. _ReadTheDocs: https://readthedocs.org
.. _PyPI: https://pypi.python.org/pypi
.. _Travis-CI: https://travis-ci.org
.. _Codecov: https://codecov.io
.. _Pyup: https://pyup.io

Install Cookiecutter
====================

In a terminal (e.g. Anaconda Prompt)::

   pip install cookiecutter

Install Git
===========

If necessary, install git: https://git-scm.com/downloads . You may need to restart your computer.

Change the documentation style in PyCharm
=========================================

Do this if you want to use Numpy style of documentation. In the "Welcome to PyCharm" window (before you open a
project): Configure → Settings → Tools → Python Integrated Tools → Docstrings → Docstring format → NumPy.

Register your GitHub account in PyCharm
=======================================

In PyCharm:

#. Menu File → Settings → Version Control → GitHub.
#. Click on the "+" icon.
#. Fill in the form and validate.

Register your GitHub account in ReadTheDocs
===========================================

On ReadTheDocs website: Paramètres → Comptes liés. Check that your GitHub account is listed here.

Install Travis Client on your computer
======================================

* Under Windows:

  #. Install Ruby (https://rubyinstaller.org/ ).
  #. Run PyCharm as Administrator.
  #. In PyCharm terminal, do: ``gem install -V travis``. If it does not work, restart your computer
     and try again.

* Under Debian, run as root::

   apt-get update
   apt-get install cookie-cutter ruby ruby-dev gcc
   gem install -V travis

* Under Ubuntu 16, run::

    sudo apt-get install ruby-dev
    sudo gem install -V travis

If you experience troubles installing travis, cf. https://github.com/travis-ci/travis.rb#installation.

-------------------
Create your package
-------------------

This section is adapted from: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html .

Generate Your Package
=====================

#. Your project will need a project name (e.g. *My Toy Package*) and a project slug (typically ``my_toy_package``).
   Before starting, check that your project slug is not used in PyPI.
#. In a terminal (e.g. Anaconda Prompt):

   #. Go to the parent directory of where you want to put the directory of your package, e.g. ``D:\GitHub\``.
   #. ``cookiecutter https://github.com/francois-durand/cookiecutter-my_toy_package.git``
   #. Answer the questions. Here is an example (some explanations follow)::

         full_name [F. Durand]: François Durand
         email [fradurand@gmail.com]: fradurand@gmail.com
         github_username [francois-durand]: francois-durand
         project_name [Python Boilerplate]: My Toy Package
         project_slug [my_toy_package]:
         project_short_description [Python Boilerplate contains all the boilerplate
         you need to create a Python package.]: My Toy Package shows how to
         create and maintain a package.
         pypi_username [francois-durand]:
         version [0.1.0]:
         use_pytest [y]:
         use_codecov [y]:
         use_pypi_deployment_with_travis [y]:
         add_pyup_badge [n]:
         Select command_line_interface:
         1 - No command-line interface
         2 - Click
         3 - Argparse
         Choose from 1, 2, 3 (1, 2, 3) [1]:
         create_author_file [y]:
         Select open_source_license:
         1 - GNU General Public License v3
         2 - MIT license
         3 - BSD license
         4 - ISC license
         5 - Apache Software License 2.0
         6 - Not open source
         Choose from 1, 2, 3, 4, 5, 6 (1, 2, 3, 4, 5, 6) [1]:

Some explanations now:

* ``use_pytest``: there are essentially three ways to do unit tests in Python: unittest (the standard solution),
  pytest (the recommended test package) and doctest (where tests are integrated in the docstrings). If you are new to
  testing, I suggest using doctest. But even so, pytest is useful to configure your tests (as we will do a bit
  later). For this reason, in all cases, my advice is to answer yes.
* ``use_codecov``: you will use Codecov to assess the coverage of your code by your tests.
* ``use_pypi_deployment_with_travis``: when you will do a *release* in GitHub, Travis will automatically release
  your package on PyPI.
* ``add_pyup_badge``: a pyup badge will appear in the readme of your package. I suggest to answer no.
* ``Click``: this allows you to easily call your program with unix-style command, e.g. ``python my_program.py --help``.
  ``Argparse`` provides the same kind of feature. You can choose either of them, even if you do not use it for the
  moment. But personally, I answer no.
* ``create_author_file``: I suggest to answer yes.

Create the PyCharm Project
==========================

In PyCharm:

#. Create new project.
#. In *Location*, fetch the directory of your project, e.g. ``D:\GitHub\my_toy_package``. Validate.
#. Warning that the directory is not empty: validate.

Create the GitHub Repo
======================

In PyCharm:

#. Menu VCS → Import into version control → Share project on GitHub.

#. Fill in the form and validate, e.g.::

      New repository name: my_toy_package
      Remote name: origin
      Description: My Toy Package shows how to create and maintain a package.

In a browser, you can go to your GitHub account to check that everything is there.

N.B.: if you use a public GitHub repository, using PyPI is free (but not for a private repository).

Create a virtual environment
============================

A virtual environment is essentially a Python installation dedicated to your project, with its own versions
of the third-party packages. It ensures that if you reuse this project several months later, it will still work...
This is not mandatory, but I suggest it especially if you use a third-party package that is still in
a 0.x.x release (which means that its API is not considered stable yet).

#. Menu File → Settings → Project → Project Interpreter. (For Apple users: PyCharm → Preferences → Project →
   Project Interpreter.)
#. Click on the gear-shaped icon → Add.
#. Fill in the form: New environment using Virtualenv. This directory proposed is just fine. Validate.

Install Dev Requirements
========================

In the PyCharm terminal:

#. Ensure you are in the directory of your package (e.g. ``D:\GitHub\my_toy_package``).
#. If you have set a virtual environment, ensure that it is activated: there should be ``(venv)`` at the beginning of
   the line. If not::

      Windows: venv\Scripts\activate
      Linux:   source venv/bin/activate

#. ``pip install -r requirements_dev.txt``

Install Your Package in "Development Mode"
==========================================

This way, your package behaves as if it were installed, but any change you make will have effect immediately.
In the PyCharm terminal, you should still be in the directory of your package, with your virtual environment activated.
Do::

   python setup.py develop

Add a Run Configuration for Doctest
===================================

In PyCharm:

#. Menu Run → Edit Configurations.
#. Add a new configuration by clicking the + button → Python tests → pytest.
#. Give a name to the configuration, e.g. ``All tests``.
#. Ignore the warning and validate.

Run this configuration: normally, it runs all the tests of the project.

Add a Run Configuration for Sphinx
==================================

In PyCharm:

#. In the root of your project, add a directory named ``build``.
#. Menu Run → Edit Configurations.
#. Plus icon (top left) → Python docs → Sphinx task.
#. Give a name to the configuration, e.g. ``Generate docs``.
#. Input: the "docs" directory of your project.
#. Output: the "build" directory of your project.
#. OK.

Run this configuration: you should have a warning "Title underline too short". Go to the mentioned file
and correct the problem. Then run the configuration again: normally, it generates the documentation. To
check the result, you can open the file ``build/index.html``.

Set Up ReadTheDocs
==================

#. On ReadTheDocs website:

   #. Go to “My Projects”. Import a Project → Importer manuellement. Fill in the form and validate, e.g.::

         my_toy_package
         https://github.com/francois-durand/my_toy_package
         Git

   #. Admin → Advanced settings. Check "Installer votre projet dans un virtualenv via setup.py install".

Set Up Pyup
===========

If you work on a "small" project, I suggest that you do not use pyup: it will just generate a lot of spam in your email
inbox. However, for a more ambitious project, it may be useful.

#. On Pyup website:

   #. Click on the green *Add Repo* button and select the repo you created.
   #. A pop up appears. Personally, I checked the first item and unchecked the two others.

   Within a few minutes, you will probably receive a pull request in GitHub (and in your email).

#. On GitHub website, open the pull request and:

   #. Merge pull request.
   #. Accept merge.
   #. Delete branch.

#. In PyCharm, menu VCS → Update project. This does a git update (to get the modifications done by Pyup).

Set Up Travis CI
================

#. On Travis website:

   #. Login using your Github credentials.
   #. It may take a few minutes for Travis CI to load up a list of all your GitHub repos. If you do not see your
      new repo, log out and log in again.
   #. Click on your new repo.
   #. Click on "Activate repository".

#. In PyCharm terminal, ensure that you are in the directory of your project and::

      travis encrypt --add deploy.password "My PyPI password"

   (replace with your actual password, in quotation marks).

#. Open the file ``.travis.yml``, which is in the root of your project (you can do so in PyCharm). Check that
   ``deploy.password.secure`` is encoded.

Check that Everything is Working
================================

#. In PyCharm: commit/push if necessary, i.e.:

   #. Menu VCS → Commit.
   #. Enter a commit message.
   #. Commit → Commit and push.
   #. Push.

#. In Travis CI website: go to Build History. The build should be a success (it may take several minutes).
#. In Codecov website: once Travis has finished building, you can navigate in your project to see what parts
   of the code are covered by the tests.
#. In ReadTheDocs website:

   #. In *Compilations*, the doc should be *transmis*.
   #. Open the documentation.
   #. In the table of contents, click on the first page (e.g. *My Toy Package*). Depending on your initial
      choice of options, you should have three to five *badges*:

      #. PyPI: invalid (there will be the version number after your first release).
      #. Build: passing.
      #. Docs: passing.
      #. Codecov (optional): with a percentage.
      #. Pyup (optional): up-to-date.

   #. In the table of contents, click on *Reference*. You should see the doc of your functions.

If you wish, you are now ready to release your first version (cf. below).

-------------------------------
During the Life of Your Package
-------------------------------

Release a Version
=================

In PyCharm:

#. Run the tests.
#. Generate the documentation locally in order to check that it is working.
#. Update the file ``HISTORY.rst``.
#. Check that the readme will be correctly rendered on PyPI. In a terminal::

      python setup.py bdist
      twine check dist/the_name_of_the_file.zip

   where ``the_name_of_the_file`` must be replaced by the relevant file name.

#. Commit/push.
#. In PyCharm terminal, do one of the following:

   * ``bumpversion patch`` (version x.y.z → x.y.(z+1)) when you made a backwards-compatible modification (such as a
     bug fix).
   * ``bumpversion minor`` (version x.y.z → x.(y+1).0) when you added a functionality.
   * ``bumpversion major`` (version x.y.z → (x+1).0.0) when you changed the API. Note: in versions 0.y.z, the API is
     not expected to be stable anyway.

If you were working on a secondary branch, do what you have to (pull request to master, etc).

On Github website, go to "releases". Select "Draft a new release", add a tag name (e.g. ``v0.1.0``) and a message
(e.g. ``First stable version``). Select "Publish release".

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

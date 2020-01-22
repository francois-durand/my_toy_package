=======
History
=======

------------------
0.9.0 (2020-01-22)
------------------

* The cookiecutter now features a pytest configuration in ``tox.ini`` and a file ``.coveragerc``.
* As a consequence, it is not necessary anymore to add ``--doctest-modules`` when configuring the tests in PyCharm.

------------------
0.8.0 (2020-01-19)
------------------

* Create our own cookiecutter: ``francois-durand/cookiecutter-my_toy_package``.
* In the tutorial:

  * Remove the steps that are now unnecessary, because they are included in the cookiecutter.
  * Create a section "Preliminaries" for the steps that are needed only once, not for every package creation.
  * Reorganize the order of the steps into a more natural course of action.
  * In PyCharm, change the documentation style to NumPy for all future package creations.

------------------
0.7.0 (2020-01-16)
------------------

* Configure Codecov and add a Codecov badge.
* Reach 100% of code coverage.
* In the tutorial, explain how to configure Codecov.

------------------
0.6.1 (2019-12-20)
------------------

* Add ``long_description_content_type`` in ``setup.py`` to avoid a warning in PyPI.

------------------
0.6.0 (2019-12-20)
------------------

* You may need to restart your computer after installing git.
* Cookiecutter now proposes argparse in addition to Click.
* It is not necessary to add twine to ``requirements_dev.txt`` (cookiecutter now does it).
* Update the procedure to install travis.
* It is not necessary anymore to remove mentions of Python 2.7 (cookiecutter has removed them).
* Remove the line ``modules`` from ``reference.rst``.
* Add ReadTheDocs theme in ``conf.py``.
* Create the directory ``build`` before setting up sphinx locally.

------------------
0.5.0 (2019-12-19)
------------------

* Explain how to indicate the type of an argument in the docstring when it is an object of one of your classes.

------------------
0.4.3 (2019-12-19)
------------------

* Correct the format of titles in ``HISTORY.rst`` to comply with PyPI's demands.

------------------
0.4.2 (2019-12-19)
------------------

* Separate the tutorial from the readme file, in the hope that it will solve the deployment problem on PyPI.

------------------
0.4.1 (2019-12-19)
------------------

* Use numpy style of documentation instead of sphinx basic style.
* In the readme, correct the explanations about Pyup.
* Say more explicitly that some steps are optional, like setting a virtual environment or using pyup.
* Added how to make travis run the doctests (thanks to Quentin Lutz).
* Remove the version numbers from the dev requirements.

------------------
0.3.2 (2019-06-27)
------------------

* Try to deploy again on PyPI.

------------------
0.3.1 (2019-06-27)
------------------

* Try to deploy again on PyPI.

------------------
0.3.0 (2019-06-26)
------------------

* Try to change the minor version number to solve deployment problem on PyPI.

------------------
0.2.5 (2019-06-26)
------------------

* Downgrade dev requirements to try to solve deployment problem on PyPI.

------------------
0.2.4 (2019-06-26)
------------------

* Try to tackle deployment problem on PyPI.

------------------
0.2.3 (2019-06-26)
------------------

* Correct the procedure for version release.

------------------
0.2.2 (2019-04-03)
------------------

* Minor updates in documentation.

------------------
0.2.1 (2019-03-27)
------------------

* Update flake.

------------------
0.2.0 (2019-03-27)
------------------

* Configuration for local build of documentation with Sphinx.
* Release a version directly on Github's website.
* Minor edits in documentation.

------------------
0.1.6 (2018-03-06)
------------------

* Minor edit in documentation.

------------------
0.1.5 (2018-03-06)
------------------

* Patch upload subpackages.

------------------
0.1.0 (2018-03-06)
------------------

* First release on PyPI.

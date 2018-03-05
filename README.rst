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

#. Your project will need a project name (e.g. *My Toy Package*) and a project slug (typically `my_toy_package`).
   Before starting, check that your project slug is not used in PyPI.
#. In a terminal (e.g. Anaconda Prompt):

   #. Go to your GitHub directory, e.g. `D:\GitHub\`.
   #. :: cookiecutter https://github.com/audreyr/cookiecutter-pypackage.git
   #. Answer the questions. Here is an example (some explanations follow).


-------
Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage


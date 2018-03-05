

\begin{verbatim}
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
\end{verbatim}

\begin{enumerate}
\item \verb|use_pytest|: answer yes, even if you plan to use doctest.
\item \verb|use_pypi_deployment_with_travis|: answer yes.
\item \verb|add_pyup_badge|: answer yes.
\item \verb|Click|: this allows you to easily call your program with unix-style command, e.g. \verb|python my_program.py --help|. I'd say yes (even if you do not use it for the moment).
\item \verb|create_author_file|: answer yes.
\end{enumerate}



\subsection{Create the PyCharm Project}

Open PyCharm.

\begin{enumerate}
\item Create new project.
\item In ``Location'', fetch the directory of your project. Fill in the form:
\begin{center}
\includegraphics[width=13cm]{pycharm_new_project}
\end{center}
\item Warning that the directory is not empty: validate.
\item Menu File $\to$ Settings $\to$ Project $\to$ Project Interpreter. Check that your virtual environment is here. If not, click on the gear $\to$ Add local, and fill in the form.
\item In the file \verb|.gitignore|:
\begin{enumerate}
\item Add these lines:
\begin{verbatim}
# PyCharm project settings
.idea
\end{verbatim}
\item Check that \verb|venv| is also excluded.
\end{enumerate}
\end{enumerate}

\subsection{Create the GitHub Repo}

\begin{enumerate}
\item Register your GitHub account in PyCharm: Menu File $\to$ Settings $\to$ Version Control $\to$ GitHub. Choose Auth type $\to$ password. Fill in the form and validate.
\item Menu VCS $\to$ Import into version control $\to$ Share project on GitHub. Fill in the form and validate, e.g.:
\begin{center}
\includegraphics[width=7cm]{share_on_github}
\end{center}
\end{enumerate}

In a browser, you can go to your GitHub account to check that everything is there.

\subsection{Install Dev Requirements}

\begin{enumerate}
\item Open the PyCharm terminal and ensure you are in the directory of your package (e.g. \verb|D:\GitHub\my_toy_package|).
\item Ensure that your virtual environment is activated: there should be \verb|(venv)| at the beginning of the line. If not:
\begin{verbatim}
venv\Scripts\activate
\end{verbatim}
%\item \verb|pip install cryptography| (apparently, this step is not necessary anymore)
\item \verb|pip install -r requirements_dev.txt|
\end{enumerate}

\subsection{Install Your Package in "Development Mode"}

This way, your package behaves as if it were installed, but any change you make will have effect immediately.

In PyCharm terminal, ensure that your virtual environment is still activated and that you are in the main directory of your project. Then:
\begin{center}
\verb|python setup.py develop|
\end{center}

\subsection{Set Up Travis CI}

Ensure that Travis CLI is installed on your computer. If not, cf. \url{https://github.com/travis-ci/travis.rb#installation}. On Windows:
\begin{enumerate}
\item Install Ruby (\url{https://rubyinstaller.org/}).
\item In PyCharm terminal:
\begin{verbatim}
gem install -V travis --no-rdoc --no-ri
\end{verbatim}
\end{enumerate}

Once Travis CLI is installed:
\begin{enumerate}
\item On Travis website:
\begin{enumerate}
\item Login using your Github credentials.
\item It may take a few minutes for Travis CI to load up a list of all your GitHub repos. They will be listed with boxes to the left of the repo name, where the boxes have an X in them, meaning it is not connected to Travis CI. Add the public repo to your Travis CI account by clicking the X to switch it “on” in the box next to the \verb|my_toy_package| repo. Do not try to follow the other instructions, that will be taken care of next.
\end{enumerate}
\item In PyCharm terminal, ensure that you are in the directory of your project and :
\begin{verbatim}
travis encrypt --add deploy.password "My PyPI password"
\end{verbatim}
(replace with your actual password, in quotation marks).
\item In the file \verb|.travis.yml|:
\begin{enumerate}
\item Check that \verb|deploy.password.secure| is encoded.
\item Suppress the line \verb|  - 2.7| (unless you plan to write code that is compatible with Python 2.7).
\end{enumerate}
\end{enumerate}





\subsection{Set Up ReadTheDocs}

Log into your account at ReadTheDocs.

\begin{enumerate}
\item Paramètres $\to$ Comptes liés. Check that your GitHub account is listed here.
\item Go to “My Projects”. Import a Project $\to$ Importer manuellement. Fill in the form and validate, e.g.:
\begin{verbatim}
my_toy_package
https://github.com/francois-durand/my_toy_package
Git
\end{verbatim}
\item Admin $\to$ Advanced settings.
\begin{enumerate}
\item Check "Installer votre projet dans un virtualenv via setup.py install".
\item In "Python interpreter", choose "CPython 3.x"
\end{enumerate}
\item In PyCharm, do a commit/push:
\begin{enumerate}
\item Menu VCS $\to$ Commit.
\item Enter a commit message, e.g. \verb|Initial settings|.
\item Commit $\to$ Commit and push.
\item Push.
\end{enumerate}
\end{enumerate}

\subsection{Set Up Pyup}

Log into your account at pyup.io.

\begin{enumerate}
\item Click on the green Add Repo button and select the repo you created.
\item A pop up appears. Personally, I checked the first item and unchecked the two others.
\item Within a few minutes, you will probably receive a pull request in GitHub (and in your email). Follow the link, accept merge and delete branch.
\item In PyCharm, do a git update (to get the modifications done by Pyup): VCS $\to$ Update project.
\end{enumerate}

\subsection{Add the Example Files}

\begin{enumerate}
\item Copy the contents of the directory \verb|myproject| (provided with this tutorial) into e.g. \verb|my_toy_package\my_toy_package|. % Two directories MySubPackage1 and MySubPackage2
\begin{enumerate}
\item Manually modify the copyright statement in each file.
\item In \verb|MyClass1|, replace \verb|my_toy_package| with the name of your package.
\end{enumerate}
\item Copy the contents of the directory \verb|docs| (provided with this tutorial) into e.g. \verb|my_toy_package\docs|. In the file \verb|reference|, replace \verb|my_toy_project| with the name of your package.% File reference
\item In the file \verb|index.rst|, add \verb|reference|, for example just after the line \verb|usage|.
\item In the file \verb|my_toy_package\my_toy_package\__init__.py|, add the following shortcuts:
\begin{verbatim}
from .SubPackage1.MyClass1 import MyClass1
from .SubPackage2.MyClass2 import MyClass2
from .SubPackage2.MyClass3 import MyClass3
\end{verbatim}
\item In the file \verb|setup.py|, remove the lines about Python 2 (unless you plan to write code that is compatible with Python 2).
\end{enumerate}

\subsection{Add a Run Configuration for Doctest}

In PyCharm:
\begin{enumerate}
%\item pip install -U pytest  % Necessary?
\item Menu Run $\to$ Edit Configurations.
\item Add a new configuration by clicking the + button $\to$ Python tests $\to$ py.test.
\item Give a name to the configuration, e.g. \verb|All tests| .
\item In ``Additional Arguments field'', add \verb|--doctest-modules| .
\item Ignore the warning and validate.
\end{enumerate}

Run this configuration: normally, it runs all the doctests of the project.

\subsection{Check that Everything is Working}

\begin{enumerate}
\item Commit/push.
\item Travis CI $\to$ Current. The build should be a success (it may take several minutes).
\item In ReadTheDocs:
\begin{enumerate}
\item In ``Compilations'', the doc should be ``transmis''.
\item In the first page of the documentation (e.g. "My Toy Package"), you should have four "badges":
\begin{enumerate}
\item PyPI: invalid (there will be the version number after your first release).
\item Build: passing.
\item Docs: passing.
\item Pyup: up-to-date.
\end{enumerate}
\item In ``Reference'', you should see the doc of your functions.
\end{enumerate}
\end{enumerate}













\section{During the Life of Your Package}


\subsection{Add a Module (= a File)}

Typically, this is a file \verb|SubPackage\MyClass|, containing class \verb|MyClass|.

\begin{enumerate}
\item In \verb|__init__.py|: add the shortcut.
\item In \verb|reference.rst|: add the auto-documentation.
\end{enumerate}

\subsection{Use a Third-Party Package}

For example, you want to use Numpy in your module.

\begin{enumerate}
\item In \verb|setup.py|, in the list \verb|requirements|, add the name of the package (e.g. \verb|'numpy'|).
\end{enumerate}

\subsection{Release a Version}

\begin{enumerate}
\item Update \verb|HISTORY.rst|.
\item In PyCharm terminal, do one of the following:
\begin{itemize}
\item \verb|bumpversion patch| (version $x.y.z \to x.y.(z+1)$),
\item \verb|bumpversion minor| (version $x.y.z \to x.(y+1).0$),
\item \verb|bumpversion major| (version $x.y.z \to (x+1).0.0$).
\end{itemize}
\item Commit/push.
\item In GitHub website, create a "release" with this version number.
\end{enumerate}

After a few minutes, Travis CI has finished the built and it is deployed on PyPI.




















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



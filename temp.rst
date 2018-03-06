



















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



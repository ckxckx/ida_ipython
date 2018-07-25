# What's New
- Pure Python

# What and Why?
This is a plugin to embed an IPython kernel in IDA Pro. The Python ecosystem has amazing libraries (and communities) for scientific computing. IPython itself is great for exploratory data analysis. Using tools such as the IPython notebook make it easy to share code and explanations with rich media. IPython makes using IDAPython and interacting with IDA programmatically really fun and easy.

## Example Uses
## QT Console
You can just use IPython qtconsole for a better interactive python shell for IDA.

![Image of Basic QT Usage](qtbasic.gif)


You can also use the QT console to graph things. This is an example creating a bar chart for the occurrences of each instruction mnemonic in a function (in notepad.exe).

![Image of QT with graph](qtwithgraph.gif)

### Notebooks

Another useful case is using IPython notebooks.

- [Function Entropy](http://nbviewer.ipython.org/github/james91b/ida_ipython/blob/master/notebook/examples/Function%20Entropy.ipynb) - Here is an example where we compute the entropy (using scipy stats module) of each function in notepad.exe and graph the result.
- [Cython and IDA](http://nbviewer.ipython.org/github/james91b/ida_ipython/blob/master/notebook/examples/Cython%20and%20IDA.ipynb) - Here is an example where we use the cython cell magic to call IDA Api's that are not exposed via IDAPython.
- [Sark Snapshots](http://nbviewer.ipython.org/github/james91b/ida_ipython/blob/master/notebook/examples/Sark%20Snapshots.ipynb) - Example of screen snapshots using Sark.

More examples..soon...

# How the plugin works
IDA is predominantly single threaded application, so we cannot safely run the kernel in a separate thread.
So instead of using another thread, a timer is registered via IDAPython and the `do_one_iteration` method of the ipython kernel is executed each frame.

# Installation
I suggest using the [Anaconda](http://continuum.io/downloads) distribution of Python as it comes with all the required python libraries pre-built and installed. To get IDA to use Anaconda, simply set the PYTHONHOME enviroment variable. Alternatively you can install IPython and the dependencies separately.

This plugin should work on all 6.X x86 QT versions of IDA on Windows, Linux, and OSX (only tested on Windows).

## Basic Installation and QTConsole
1. Download and extract the [release](/../../releases/latest)
2. Copy `ida_ipython.py` into IDA's `plugins` directory
4. Launch IDA
5. Under the `View` menu, click `IDAIPython QtConsole` or
6. At the command line, start an IPython qtconsole with the kernel instance (outputted in the IDA console) e.g `jupyter qtconsole --existing kernel-4264.json`

## Using the Notebook
1. Change the paths to the `idaq.exe` and `idaq64.exe` executables in the `kernel.json` under the `notebook-kernels\ida32`
    and `notebook-kernels\ida64` directories respectively (the default is IDA 7.1 on Windows)
1. Install the kernels using `jupyter-kernelspec install` (e.g. `jupyter-kernelspec install --user notebook-kernels\ida64`)
1. When starting a notebook, choose the `IDA32` or `IDA64` kernels, depending on your desired IDA version.

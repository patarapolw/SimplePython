# SimplePython

Using simple Python scripts and REPL without an IDE.

## Setting up

### Managing Python verions on MacOS

An important concept in Python is virtual environment. The tool I am going to use is [poetry](https://github.com/sdispater/poetry). [The reasons?](https://github.com/sdispater/poetry#why) Mainly because of [setup.py](https://github.com/kennethreitz/setup.py) replacement. Another option is [pipenv](https://pipenv.readthedocs.io/en/latest/). Anyway, if you are using an IDE, like [PyCharm](https://www.jetbrains.com/pycharm/), the IDE can help automate this for you.

- Download and install the latest Python 3 at [https://www.python.org](https://www.python.org).
- Choose Python 3 with Poetry.

```commandline
which python3
# /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
unlink /usr/local/bin/python
ln -s /Library/Frameworks/Python.framework/Versions/3.7/bin/python3 /usr/local/bin/python
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
```

### Creating a project

- Create the folder you want your project, optionally (i.e. you don't have to) with `poetry new my-package`. And the via command line, navigate to your folder.

```commandline
poetry init
```

### Creating a REPL, and running a script

You can do it via

```commandline
poetry run python           // Create a REPL session
poetry run python script.py // Run script.py
```

### Load the script into the REPL

```python
>>> import script           // or
>>> with open('script.py') as f: exec(f.read()) // or
>>> from pathlib import Path
>>> exec(Path('script.py').readtext())
```

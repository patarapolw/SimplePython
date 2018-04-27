# PyPI

`.pypirc` is to be put at `$HOME/.pypirc`

## Markdown support

Requirements:

- `setuptools>=38.6.0`
- `twine>=1.11.0`
- ? But I need this one. `wheel>=0.31.0` and `python setup.py bdist_wheel`

https://dustingram.com/articles/2018/03/16/markdown-descriptions-on-pypi

## In case Twine fails

Use `python setup.py bdist_wheel --universal upload`

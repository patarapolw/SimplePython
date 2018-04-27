# Testing

Rely on `pip install pytest`

## Some useful pytest extensions

```python
pytest_requires = ['xdist', 'repeat', 'timeout', 'doctestplus']
tests_require = ['pytest'] + ['pytest-{}'.format(req) for req in pytest_requires]
```

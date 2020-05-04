Setup
=======

```
virtualenv --python=python3 .venv
source .venv/bin/activate
pip install -e .
pip install pyodbc
```

Change the content of variables `server` and `database` in `package/__init__.py`.

Reproduce the issue
===================
```
python test.py
```

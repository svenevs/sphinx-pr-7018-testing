# Sphinx PR 7018 Supplemental Napolean Code Testing

Simple set of code with associated docs folders ready to go for testing the
napoleon NumPy and Google docstring variants.  Only differences between the
two folders are the change in docstring format in ``some_code/a_module.py``
and config vars for napoleon in ``docs/conf.py``.

Make sure to install the right thing...

```console
# Clone this repo
$ git clone https://github.com/svenevs/sphinx-pr-7018-testing.git
$ cd sphinx-pr-7018-testing/

# Make sure you test in a virtual environment of some kind
# (don't break your local sphinx install xD)
$ python -m venv venv
$ source venv/bin/activate

# Option 1: just want to test
$ pip install -r requirements.txt

# Option 2: you are wanting to try and make changes
# clone sphinx and checkout PR
$ git clone https://github.com/sphinx-doc/sphinx.git
$ cd sphinx/
$ git fetch origin pull/7018/head:pull/7018
$ git checkout pull/7018

# do editable install so that changes you make in sphinx
# directory get reflected as you test
$ pip install -e .
$ cd ..  # [ go back to repo root ]

# -----------------------------

# go build whichever version you want
$ cd numpy/docs && make html
# ... or ...
$ cd google/docs && make html
```

What is being investigated here is how to manipulate the napoleon
extension to allow automatic return type injection (thanks to PR 7018)
without needing to manually specify things.  This just needs to be done
with the `Returns` clause at the end of the docstring in `some_code/a_module.py`
somehow.

```diff
  Return
  ------
+ A path is returned
- pathlib.Path
-     A path is returned.
```

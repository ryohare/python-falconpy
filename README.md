# python-falconpy

This is just a packager for [falconpy](https://github.com/CrowdStrike/falconpy) so it can be on PyPI to ease usage in python tools.

## API Information
[Main README](https://github.com/CrowdStrike/falconpy/blob/main/README.md)

[Services README](https://github.com/CrowdStrike/falconpy/blob/main/services/README.MD)

## Updating on PyPI
Falconpy as added as a git submodule. For updates to this package, it will have to be updated first via the submodule. as below.

```bash
git submodule update --init --recursive
```

Verify that there are not dependecy changes in src/falconpy/requirements.txt. These would need to be added to setup.py for the packaging.

It can then be released to PyPI with twine
```bash
# sanity checks
tox
tox -e check

# set the current version in src/falconpy/__init__ for bump version
VER=`cat setup.py | grep version=\' | cut -d \' -f 2`
echo "__VERSION__ = '$VER'" > src/falconpy/__init__.py

# bump the version based. Not really managed by CS, so IDK, do patches?
# Allow ditry needed because we dirty up CS's falconpy with a version
bumpversion minor --allow-dirty

# create package
python setup.py clean --all sdist --formats=gztar,zip bdist_wheel

# send to pypi with twine
twine upload --skip-existing dist/*.whl dist/*.gz dist/*.zip
```

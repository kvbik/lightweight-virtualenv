note
----

this repository is much more a playgroung for something that is used
in rvirtualenv package. if you want to try relocatable virtual environment
please follow the other project: `rvirtualevn`_.

.. _rvirtualevn: http://github.com/kvbik/rvirtualenv

lightweight python virtual environment
--------------------------------------

this directory structure is trying to be a relocatable virtual python environment

it is inspired by virtulenv package a lot, and uses its activate_this.py command

if you want to try this, clone it (fork me) and just define PYTHONPATH env
variable pointing at subdir py of this repository, or call directly {{ REPO }}/py/bin/python -
- which is a shell script or try {{ REPO }}/py/bin/python.py directly.
there is {{ REPO }}/py/bin/python.bat for windows convenient usage as well.
python* files are just wrappers, that sets environment variable for you
and passes same arguments to system installed python


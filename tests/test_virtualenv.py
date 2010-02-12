
import sys, os
from os import path
from shutil import rmtree, copytree
from unittest import TestCase
from tempfile import mkdtemp
from subprocess import Popen, PIPE


class TestRunCase(TestCase):
    def setUp(self):
        # store curr path
        self.oldcwd = os.getcwd()

        # create test dir structure
        self.directory = mkdtemp(prefix='test_virtualenv_')
        self.virtualenv = path.join(self.directory, 'PY')
        self.python = path.join(self.virtualenv, 'bin', 'python.py')

        # copy virtualenv there
        copytree('.', self.virtualenv)

        # test modules
        self.imported = []

    def run_command(self, cmd):
        shell = sys.platform != 'win32'
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=shell)
        return p.communicate()

    def test_python_itself(self):
        cmd = '%s -c "print 128"' % self.python
        stdout, stderr = self.run_command(cmd)
        self.failUnlessEqual('128\n', stdout)

    def test_run_python_script(self):
        script = path.join(self.oldcwd, 'tests', 'scripts','print.py')
        cmd = '%s %s' % (self.python, script)
        stdout, stderr = self.run_command(cmd)
        self.failUnlessEqual('', stdout)

    def test_run_python_script_with_args(self):
        script = path.join(self.oldcwd, 'tests', 'scripts','print.py')
        cmd = '%s %s a b c' % (self.python, script)
        stdout, stderr = self.run_command(cmd)
        self.failUnlessEqual("['a', 'b', 'c']\n", stdout)

    def install_some_way(self, inst_type, inst_command='install'):
        os.chdir(path.join(self.oldcwd, 'tests', 'installs', 'venvtest-%s' % inst_type))
        inst = '%s setup.py %s' % (self.python, inst_command)
        stdout, stderr = self.run_command(inst)

        cmd = '%s -c "import venvtest; print venvtest.__versionstr__"' % self.python
        stdout, stderr = self.run_command(cmd)

        self.failUnlessEqual('0.1.0\n', stdout)

    def test_install_distutils_way(self):
        self.install_some_way('distutils')

    def test_install_setuptools_way(self):
        self.install_some_way('setuptools')

    def tearDown(self):
        # go back
        os.chdir(self.oldcwd)

        # dir cleanup
        rmtree(self.directory)

        # clear imported module
        for i in self.imported:
            if sys.modules.has_key(i):
                del sys.modules[i]


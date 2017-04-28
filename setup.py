from sys import version_info
import os
# Prevent spurious errors during `python setup.py test` in 2.6, a la
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html:
try:
    import multiprocessing
    # silence pyflakes
    assert multiprocessing
except ImportError:
    pass

from setuptools import setup, find_packages

def read(fname):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
    name='exlink',
    version='0.0.1',
    description='Control your Samsung TV using a serial port',
    long_description=read('README.md'),
    author='Paul D.Smith',
    author_email='paul.d.smith@metaswitch.com',
    license='proprietary',
    packages=['Exlink'],
    url='https://github.com/papadeltasierra/exlink',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Development Status :: 2 - Pre-Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Text Processing :: General'],
    keywords=['samsung', 'exlink', 'serial'],
    use_2to3=version_info >= (3,)
)

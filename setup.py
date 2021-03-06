import os
import re

from functools import partial

from setuptools import setup, find_packages


# NOTE: http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing
except ImportError:
    pass


get_path = partial(os.path.join,  os.path.dirname(os.path.abspath(__file__)))


def get_version(path):
    version = None
    try:
        version =  re.search(r'__version__\s*=\s*[\'"]([\d.]+)[\'"]',
                             open(path).read()).group(1)
    except (IOError, AttributeError):
        pass
    return version


setup(name='mongodrums',
      author='Greg Banks',
      author_email='quaid@kuatowares.com',
      description='pymongo instrumentation for hippies',
      setup_requires=['rexparse'],
      dependency_links=['https://github.com/gregbanks/rexparse/archive/master.zip#egg=rexparse'],
      rexparse={'requirements_path': get_path('requirements.txt')},
      version=get_version(get_path('mongodrums/_version.py')),
      test_suite='nose.collector',
      scripts=[get_path('scripts/run_dex.py'),
               get_path('scripts/run_collector.py'),
               get_path('scripts/update_indexes.py'),
               get_path('scripts/report.py')],
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*",
                                      "tests"]))


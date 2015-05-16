#! python
#

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

"""
    Make sure you read the documentation for distutils:
        http://docs.python.org/distutils/setupscript.html.
"""

config = {
          'description': 'LPtHW, Exc. 47',
          'author': 'Marcin Szarek',
          'url': 'https://github.com/marcinshk/Python-projects.git',
          'download_url': 'https://github.com/marcinshk/Python-projects.git',
          'author_email': 'marcinshk@gmail.com',
          'version': '0.1',
          'install_requires': ['nose', 'setuptools', 'virtualenv'],
          'packages': ['ex47-pkg'],
          'scripts': [],
          'name': 'ex47'
    }

setup(**config)

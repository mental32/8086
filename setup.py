import re
from setuptools import setup

requirements = [
  'pygame'
]

with open('README.md') as inf:
  long_description = inf.read()

def get_version():
  with open('_8086/__init__.py') as inf:
      match = re.search(r"((\d\.){2,5}\d)", inf.read(), re.MULTILINE)

      if match is None:
          raise RuntimeError('Version could not be found.')

      return match.groups()[0]

setup(name='_8086_GAME',
      author='mental',
      url='https://github.com/mental32/8086',
      version=get_version(),
      packages=['_8086'],
      license='MIT',
      description='A puzzle based programming video game.',
      long_description=long_description,
      include_package_data=True,
      install_requires=requirements,
      python_requires='>=3.6',
      classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
      ]
)

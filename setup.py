from distutils.core import setup
import setuptools

console_scripts = """
[console_scripts]
doommoses=doommoses.cli:cli
"""

setup(
  name = 'doommoses',
  packages = ['doommoses'],
  version = '0.0.43',
  description = 'DoomMoses',
  long_description = 'MosesTokenizer in Python',
  author = '',
  package_data={'doommoses': ['data/perluniprops/*.txt', 'data/nonbreaking_prefixes/nonbreaking_prefix.*']},
  url = 'https://github.com/sortiz/doommoses',
  keywords = [],
  classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  install_requires = ['regex', 'six', 'click', 'joblib', 'tqdm'],
  entry_points=console_scripts,
)

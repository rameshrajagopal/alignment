try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
      name = "alignment", version = '0.1', 
      description = "Small commandline utility to setup aribitory solar system",
      author = "Ramesh R",
      author_email ="mail2.rameshr@gmail.com",
      packages = [
                   'alignment',
                   'alignment/plugins', 
                   'alignment/unittest',
                 ],
      install_requires = ['pyyaml',]
      )

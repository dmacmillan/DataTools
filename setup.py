from setuptools import setup, find_packages

setup(name='Data Tools',
      author='Daniel MacMillan',
      author_email='drm5@sfu.ca',
      version='v1.0.0',
      packages=find_packages(),
      install_requires=['pytest'],
      python_requires='>=3.6',
      entry_points={'console_scripts': ['datatools = datatools.main:main']})
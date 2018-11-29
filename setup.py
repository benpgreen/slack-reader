from setuptools import setup, find_packages

setup(
      name='slackreader',
      version='0.0.1',
      description='A slack reader',
      url='https://github.com/benpgreen/slack-reader',
      author='Ben Green',
      license='Ben Green',
      packages=find_packages(),
      install_requires=['requests'],
      zip_safe=False
      )

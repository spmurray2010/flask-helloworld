from setuptools import setup

setup(
  name='helloworld',
  packages=['helloworld'],
  include_package_data=True,
  install_requires=['helloworld',],
  setup_requires=['pytest-runner',],
  tests_require=['pytest',],
)

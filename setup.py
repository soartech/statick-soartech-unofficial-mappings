"""Setup."""

try:
    from setuptools import setup
except:  # pylint: disable=bare-except # noqa: E722 # NOLINT
    from distutils.core import setup  # pylint: disable=wrong-import-order

with open('README.md') as f:
    long_description = f.read()  # pylint: disable=invalid-name

VERSION='0.1.0'

setup(
    author='Soar Technology, Inc.',
    name='statick-soartech-unofficial-mappings',
    description='Statick extension to add unofficial CMU SEI rule mappings.',
    version=VERSION,
    packages=['statick_tool'],
    package_dir={'statick_tool': '.'},
    package_data={'statick_tool': ['rsc/plugin_mapping/*']},
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['statick'],
    url='https://github.com/soartech/statick-soartech-rule-mappings',
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Testing",
    ],
)

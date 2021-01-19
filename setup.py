#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['requests', 'dataclasses', 'fhir.resources==6.0.0']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', 'responses']

setup(
    author="WalkIT",
    author_email='code@walkit.nl',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description=" Health IT starter kit providing auditing, authn and authz using FHIR and OpenID Connect",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='hit_starter_on_fhir',
    name='hit_starter_on_fhir',
    packages=find_packages(include=['hit_starter_on_fhir', 'hit_starter_on_fhir.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/walkIT-nl/hit_starter_on_fhir',
    version='0.1.0',
    zip_safe=False,
)

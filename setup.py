import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-broab',
    version='0.1',
    requires=[
        # 'djorm-ext-pgarray>=0.6',
        # 'django-model-utils',
        ],
    packages=['broab'],
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to maintain objects from Python-Neo.',
    long_description=README,
    url='https://github.com/gentnerlab/django-mr-anderson',
    author='Justin Kiggins',
    author_email='justin.kiggins@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
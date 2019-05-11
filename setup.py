from setuptools import setup, find_packages

from typed_environ import __version__

setup(
    name='typed-environ',
    version=__version__,
    description='Load environment variables with types',
    url='https://github.com/MichaelKim0407/typed-environ',
    license='MIT',
    author='Michael Kim',
    author_email='mkim0470@gmail.com',

    packages=find_packages(),

    classifiers=[
        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',

        'Topic :: Software Development :: Libraries',
    ],
)

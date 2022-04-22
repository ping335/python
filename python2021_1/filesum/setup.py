from setuptools import setup


setup(
    name='filesum',
    version='0.1.0',
    description='Console utility for generating and checking the hash sum of a file.',
    license='MIT',
    py_modules=['filesum'],
    entry_points={
        'console_scripts': [
            'filesum = filesum:cli',
        ],
    },
    install_requires=[
        'Click>=7.1',
        'colorama>=0.4',
    ]
)

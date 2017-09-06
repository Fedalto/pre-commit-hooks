from setuptools import setup

setup(
    name='pre-commit-hooks',
    version='0.2',
    url='https://github.com/Fedalto/pre-commit-hooks',
    license='MIT',
    author='Leonardo Fedalto',
    author_email='lfedalto@gmail.com',
    description='pre-commit hooks',

    install_requires=[
        'mypy'
    ],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

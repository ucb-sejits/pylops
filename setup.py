from distutils.core import setup

setup(
    name='pylops',
    version='0.1.0',
    url='github.com/ucb-sejits/pylops',
    license='B',
    author='Nathan Zhang',
    author_email='nzhang32@berkeley.edu',
    description='Python List Operations',

    packages=[
        'pylops'
    ],

    install_requires=[
        'ctree',
        'numpy'
    ]
)

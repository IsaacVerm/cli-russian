from setuptools import setup

setup(
    name='annotate',
    version='0.1',
    py_modules=['annotate'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        annotate_noun=annotate:annotate_noun
    ''',
)

from setuptools import setup, find_packages

setup(
    name='Linus',
    version='0.1.0',
    description='Various data wrangling utilities',
    author='Dominic Fitzgerald',
    author_email='dominicfitzgerald11@gmail.com',
    url='https://github.com/djf604/linus',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['linus = linus:execute_from_command_line']
    }
)

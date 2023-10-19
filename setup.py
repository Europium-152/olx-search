from setuptools import setup, find_packages

setup(
    name='olx-search',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'typer',
    ],
    entry_points={
        'console_scripts': [
            'olx-search=source.main:start',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for searching OLX listings',
    url='https://github.com/yourusername/olx-search',
)

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'Pranit Sah'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='pranit1606@gmail.com',
    description='A small example for movie recommendation ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[SRC_REPO],  # Change 'package' to 'packages'
    python_requires='>=3.11.7',
    install_requires=LIST_OF_REQUIREMENTS,
)

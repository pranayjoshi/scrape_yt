from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="scrape_yt", # Replace with your own username
    version="0.0.1",
    author="Pranay Joshi",
    author_email="pranayjoshi4466@gmail.com",
    description="A simple youtube video and playlist downloader.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pranayteaches/scrape_yt",
    packages=find_packages(),
    license= "MIT",
    install_requires=['pytube3','pytube'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
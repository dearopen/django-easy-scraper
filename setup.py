import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-easy-scraper",
    version="0.0.4",
    author="dearopen",
    author_email="",
    description="Dango app to scrape web page",
    long_description='A full featured djagno app to scrape web page, it can scrape multiple site together and single details page too',
    long_description_content_type="text/markdown",
    url="https://github.com/dearopen/django-easy-scraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
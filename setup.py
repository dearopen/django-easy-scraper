import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-easy-scraper",
    version="1.0.0",
    author="dearopen",
    author_email="",
    description="Dango app to scrape web page",
    long_description=long_description,
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
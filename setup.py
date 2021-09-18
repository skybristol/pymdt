import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymdt",
    version="0.0.1",
    author="Sky Bristol",
    author_email="skybristol@gmail.com",
    description="A Python package for working with messy data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skybristol/pymdt",
    project_urls={
        "Bug Tracker": "https://github.com/skybristol/pymdt/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
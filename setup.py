import setuptools

# Get long description from the README.rst
with open("README.md") as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setuptools.setup(
    name="pbwrap",
    version="1.1.0",
    description="A Pastebin API Wrapper for Python",
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/Mikts/pbwrap",
    author="Michael Tsoukatos",
    author_email="mikts94@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development",
        "Topic :: Utilities",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires=">=3",
    keywords="wrapper pastebin api development utility",
    packages=setuptools.find_packages(exclude=["docs", "tests"]),
    install_requires=["requests"],
    extras_require={"test": ["pytest"]},
    project_urls={"Bug Reports": "https://github.com/Mikts/pbwrap/issues"},
)

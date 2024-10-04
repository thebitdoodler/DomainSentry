from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="domainsentry",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for bulk WHOIS extraction and threat intelligence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thebitdoodler/domainsentry",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",


    ],
    python_requires=">=3.7",
    install_requires=[
        "python-whois",
        "tldextract",
        "colorama",
        "streamlit",
    ],
    entry_points={
        "console_scripts": [
            "domainsentry=domainsentry.cli:main",
        ],
    },
)
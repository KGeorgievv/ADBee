from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="adbee",
    version="0.1.0",
    author="KGeorgievv",
    description="A lightweight Python utility to fetch Android device information via ADB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KGeorgievv/ADBee",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Debug Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
)

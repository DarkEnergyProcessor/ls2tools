import os
import re
import setuptools

INSTALL_DIR = os.path.dirname(os.path.realpath(__file__))

def read(file):
    with open(file, "r", encoding="UTF-8") as f:
        return f.read()

version = re.search(r"VERSION = \"([^\"]+)\"", read(os.path.join(INSTALL_DIR, "ls2tools", "__init__.py"))).group(1)

if __name__ == "__main__":
    setuptools.setup(
        name="ls2tools",
        version=version,
        description="LS2-related Tooling",
        long_description=read("README.md"),
        author="Miku AuahDark",
        license="zlib/libpng",
        python_requires=">=3.10",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "License :: OSI Approved :: zlib/libpng License",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.10",
            "Topic :: Utilities"
        ],
        keywords=["python3", "ls2"],
        packages=setuptools.find_packages(),
        entry_points={
            "console_scripts": [
                "ls2tools = ls2tools:main"
            ]
        }
    )

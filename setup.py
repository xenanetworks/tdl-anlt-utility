import setuptools


def main():
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="tdl-anlt-utility",
        entry_points={
            "console_scripts": [
                "tdl-anlt-utility = xoa_utils.entry:main",
            ]
        },
        description=(
            "Xena ANLT Utility provides a shell-like command-line interface for users to do"
            " ANLT tests interactively."
        ),
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Leonard Yu",
        author_email="leonard.yu@teledyne.com",
        maintainer="Teledyne LeCroy Xena",
        maintainer_email="support@xenanetworks.com",
        url="https://github.com/xenanetworks/tld-anlt-utility",
        packages=setuptools.find_packages(),
        license="Apache 2.0",
        install_requires=[
            "typing_extensions>=4.4.0",
            "cffi>=1.15.1",
            "cryptography>=39.0.0",
            "pycparser>=2.21",
            "colorama>=0.4.6",
            "idna>=3.4",
            "asyncssh>=2.13.0",
            "asyncclick>=8.1.3.4",
            "anyio>=3.6.2",
            "loguru>=0.6.0",
            "pdoc>=12.3.1",
            "pytest>=7.2.1",
            "psutil>=5.9.4",
            "tdl-xoa-driver>=1.1.0",
            "pydantic>=2.6.4",
        ],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3.13",
        ],
        python_requires=">=3.9",
    )


if __name__ == "__main__":
    main()

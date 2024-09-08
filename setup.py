from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="TraceNinja",
    version="1.0.3",
    description="""TraceNinja is a subdomain enumeration tool for Python that allows you to enumerate domains and gather information about them. And much much more on the future ^_^. It's currently under development.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mohamed",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'traceninja=TraceNinja.traceninja:main',
        ],
    },
    install_requires=required,
    license="MIT",
    url="https://github.com/mohdh34m/TraceNinja",
    python_requires=">=3.10",
)
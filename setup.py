from setuptools import setup, find_packages

setup(
    name="logger-utils",
    version="1.0.0",
    description="An advanced color-coded JSON logger for Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ruhiddin",
    author_email="your-email@example.com",
    url="https://github.com/yourusername/logger-utils",  # Replace with your GitHub repo URL
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "termcolor",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

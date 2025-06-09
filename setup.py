from setuptools import setup, find_packages

setup(
    name="apartment-analysis",
    version="1.0.0",
    description="CIND830 Assignment 2: Apartment Rental Data Analysis",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "jupyter>=1.0.0",
        "notebook>=6.4.0"
    ],
    python_requires=">=3.7",
    author="CIND830 Student",
    author_email="student@example.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
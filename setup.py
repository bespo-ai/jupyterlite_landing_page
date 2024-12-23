from setuptools import setup, find_packages

setup(
    name="vincent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "ipython",
    ],
    package_data={
        'vincent': ['data/*'],
    },
    include_package_data=True,
    author="Bespo AI",
    author_email="support@bespo.ai",
    description="Vincent - A Jupyter notebook assistant",
)
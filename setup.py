import setuptools

dependencies = [
    "pyyaml",
    "boto3",
]

setuptools.setup(
    name="pybackup",
    version="0.0.1",
    author="Jacob Hernandez",
    author_email="hakube@outlook.com",
    description="Simple backup utility for databases",
    packages=["pybackup"],
    install_requires=dependencies,
    entry_points={
        "console_scripts": [
            "pybackup = pybackup.__main__:main",
        ]
    },
)
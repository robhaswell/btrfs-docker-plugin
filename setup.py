from setuptools import setup

setup(
    name="BTRFS Docker Plugin",
    version="0.1",
    author="Rob Haswell",
    author_email="rob@clusterhq.com",
    url="https://github.com/robhaswell/btrfs-docker-plugin",
    license="Apache License, Version 2.0",
    packages=[
        "btrfs_docker",
    ],
    entry_points={
        "console_scripts": [
            "btrfs-docker-plugin = btrfs_docker.plugin:main",
        ],
    },
    install_requires=[
        "flask",
        "simplejson",
    ],
)


from setuptools import setup


setup(
    name="advantechiot",
    version="0.1.67",
    author='Keng Wei Li',
    author_email='Kengwei.Li@advantech.com.tw',
    packages=["advantechiot"],
    package_data={
        "advantechiot": [
            "Driver_x86/*",
            "Driver_arm/*",
        ],
    },
    include_package_data=True,
    install_requires=["setuptools"],
    entry_points={},
)

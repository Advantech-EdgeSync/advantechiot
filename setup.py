
from setuptools import setup


setup(
    name="advantechiot",
    version="0.1.45",
    author='Keng Wei Li',
    author_email = 'Kengwei.Li@advantech.com.tw',
    packages=["advantechiot"],
    package_data={
        "advantechiot": [
            "Driver_x86/*.sh",
            "Driver_arm/*.sh",
            "Driver_x86/*.so",
            "Driver_arm/*.so",
            "Driver_x86/*.ini",
            "Driver_arm/*.ini"
        ],
    },
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "advantechiot-install=advantechiot.installation:install",
        ],
    },
)

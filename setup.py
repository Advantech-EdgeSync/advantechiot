from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import os

class CustomInstall(install):
    def run(self):
        # 先執行標準安裝
        install.run(self)

        # 確保 script 存在
        script_dir = os.path.join(os.path.dirname(__file__), "scripts")

        # 執行 install.sh（安裝 .so）
        install_script = os.path.join(script_dir, "install.sh")
        if os.path.exists(install_script):
            print("執行 install.sh 安裝 .so 檔案...")
            subprocess.call(["sh", install_script])

        # 執行 build_python.sh（編譯 Python）
        build_script = os.path.join(script_dir, "build_python.sh")
        if os.path.exists(build_script):
            print("執行 build_python.sh 編譯 Python 程式...")
            subprocess.call(["sh", build_script])

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],  # 這裡填入所需的 pip 依賴
    cmdclass={
        "install": CustomInstall,  # 使用自訂安裝類別
    },
)

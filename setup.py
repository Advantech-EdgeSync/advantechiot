import os
from setuptools import setup
from setuptools.command.install import install
import shutil


class CustomInstall(install):
    def run(self):
        # 執行標準安裝過程
        install.run(self)

        # 安裝完成後的訊息
        print("\n⚠️  安裝完成！請手動執行以下指令來完成設定：")
        print("\n    sudo cp /path/to/mylib.so /usr/lib/\n")
        print("    或者您可以執行以下指令手動完成設定：")
        print("\n    sudo python3 -m mypackage.post_install\n")

        # 額外的檔案處理邏輯（如果有需要）
        # source_dir_arm = os.path.join(os.path.dirname(__file__), 'Driver_arm')
        # source_dir_x86 = os.path.join(os.path.dirname(__file__), 'Driver_x86')
        # `advantechiot` 會在安裝目錄下
        # target_dir = os.path.join(self.install_lib, 'advantechiot')

        # 複製 Driver_arm 資料夾
        # if os.path.exists(source_dir_arm):
        #     shutil.copytree(source_dir_arm, os.path.join(
        #         target_dir, 'Driver_arm'))
        #     print(f'已將 Driver_arm 複製到 {os.path.join(target_dir, "Driver_arm")}')
        # else:
        #     print('找不到 Driver_arm 資料夾')

        # 複製 Driver_x86 資料夾
        # if os.path.exists(source_dir_x86):
        #     shutil.copytree(source_dir_x86, os.path.join(
        #         target_dir, 'Driver_x86'))
        #     print(f'已將 Driver_x86 複製到 {os.path.join(target_dir, "Driver_x86")}')
        # else:
        #     print('找不到 Driver_x86 資料夾')


setup(
    name="advantechiot",
    version="0.1.20",
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
    include_package_data=True,  # 確保其他非程式碼檔案被包含
    install_requires=[],  # 這裡填入所需的 pip 依賴
    cmdclass={
        "install": CustomInstall,  # 使用自訂安裝類別
    },
)

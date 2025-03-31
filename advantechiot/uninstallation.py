import os
import sys
import shutil
import platform


def is_in_container():
    if shutil.which("systemd") is None:
        return True
    return False


def uninstall():
    architecture = platform.machine()
    os_name = platform.system()
    susi_iot_install_path = ""
    if os_name == "Linux" and 'aarch64' in architecture.lower():
        susi_iot_install_path = "Driver_arm/install.sh"

    elif os_name == "Linux" and 'x86' in architecture.lower() and not is_in_container():
        susi_iot_install_path = "Driver_x86/install.sh"

    elif os_name == "Linux" and 'x86' in architecture.lower() and is_in_container():
        susi_iot_install_path = "Driver_x86/install_susi_iot_in_container.sh"

    elif os_name == "Windows" and 'x86' in architecture.lower():
        pass

    elif os_name == "Windows" and 'aarch64' in architecture.lower():
        pass

    else:
        sys.exit(
            f"disable to import library, architechture:{architecture.lower()}, os:{os_name}")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    susi_iot_install_path= os.path.join(current_dir, susi_iot_install_path)
    exit_code = os.system(f"{susi_iot_install_path} u")
    if exit_code == 0:
        print("uninstall advanteck iot SDK successfully")
    else:
        sys.exit(f"fail to install advanteck iot SDK：{exit_code}")
    

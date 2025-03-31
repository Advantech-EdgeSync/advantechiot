import os
import sys
import shutil
import platform
import py_compile


def compile_python_execute_file():
    os.system('sudo rm -rf __pycache__/')
    py_compile.compile("susiiot.py", cfile="__pycache__/susiiot.pyc")
    os.system('sudo mv __pycache__/susiiot.pyc .')
    os.system('sudo chmod 777 susiiot.pyc')


def compile_python_execute_file_in_container():
    os.system('pwd')
    os.system('rm -rf __pycache__/*.pyc')
    py_compile.compile("susiiot.py", cfile="__pycache__/susiiot.pyc")
    os.system('mv __pycache__/susiiot.pyc .')
    os.system('chmod 777 susiiot.pyc')


def is_in_container():
    if shutil.which("systemd") is None:
        return True
    return False


def delete_dynamic_links(target_folder="./Driver_x86/"):
    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        if os.path.islink(file_path):
            try:
                os.remove(file_path)
                print(f"Deleted symlink: {file_path}")
            except Exception as e:
                print(f"Failed to delete symlink: {file_path}, Error: {e}")


def set_x86_dynamic_links():
    dynamic_links = {
        "libEApi.so": "libEApi.so.1.0.0",
        "libEApi.so.1": "libEApi.so.1.0.0",
        "libSUSI-3.02.so": "libSUSI-3.02.so.1.0.8",
        "libSUSI-3.02.so.1": "libSUSI-3.02.so.1.0.8",
        "libSUSI-4.00.so": "libSUSI-4.00.so.1.0.0",
        "libSUSI-4.00.so.1": "libSUSI-4.00.so.1.0.0",
        "libSUSIAI.so": "libSUSIAI.so.1.0.0",
        "libSUSIDevice.so": "libSUSIDevice.so.1.0.0",
        "libSusiIoT.so": "libSusiIoT.so.1.0.0",
        "libjansson.so": "libjansson.so.4.11.0",
        "libjansson.so.4": "libjansson.so.4.11.0",
    }

    target_folder = "./Driver_x86/"

    for source, target in dynamic_links.items():
        source_path = os.path.join(target_folder, source)
        target_path = target

        if os.path.exists(source_path):
            os.remove(source_path)

        try:
            os.symlink(target_path, source_path)
            print(f"Created symlink: {source_path} -> {target_path}")
        except Exception as e:
            pass
            # print(f"Failed to create symlink: {source_path} -> {target_path}, Error: {e}")


def set_arm_dynamic_links():
    dynamic_link_table = {
        "Driver_arm/libjansson.so.4.11.0": "./Driver_arm/libjansson.so",
        "Driver_arm/libjansson.so.4.11.0": "./Driver_arm/libjansson.so.4",
        "Driver_arm/libSUSI-4.00.so.1.0.0": "./Driver_arm/libSUSI-4.00.so",
        "Driver_arm/libSUSI-4.00.so.1.0.0": "./Driver_arm/libSUSI-4.00.so.1",
        "Driver_arm/libSusiIoT.so.1.0.0": "./Driver_arm/libSusiIoT.so"
    }
    for source, target in dynamic_link_table.items():
        try:
            os.symlink(source, target)
        except:
            pass


def install():
    architecture = platform.machine()
    os_name = platform.system()
    susi_iot_install_path = ""
    if os_name == "Linux" and 'aarch64' in architecture.lower():
        set_arm_dynamic_links()
        susi_iot_install_path = "Driver_arm/install.sh"
        compile_python_execute_file_in_container()

    elif os_name == "Linux" and 'x86' in architecture.lower() and not is_in_container():
        set_x86_dynamic_links()
        susi_iot_install_path = "Driver_x86/install.sh"
        compile_python_execute_file()

    elif os_name == "Linux" and 'x86' in architecture.lower() and is_in_container():
        set_x86_dynamic_links()
        susi_iot_install_path = "Driver_x86/install_susi_iot_in_container.sh"
        compile_python_execute_file_in_container()

    elif os_name == "Windows" and 'x86' in architecture.lower():
        pass

    elif os_name == "Windows" and 'aarch64' in architecture.lower():
        pass

    else:
        sys.exit(
            f"disable to import library, architechture:{architecture.lower()}, os:{os_name}")

    exit_code = os.system(susi_iot_install_path)
    if exit_code == 0:
        print("install advanteck iot SDK successfully")
    else:
        sys.exit(f"fail to install advanteck iot SDK：{exit_code}")

install()
import os
import requests
import subprocess

# URL for the AyaanScript file
ayaan_script_url = "https://raw.githubusercontent.com/ayaan511/python-installer-config/refs/heads/main/ayaan.py?token=GHSAT0AAAAAAC4KQGIAWRLOVGF4C44HCQH4Z3KF5VA"

# Paths
install_dir = r"C:\AyaanScript"
ayaan_script_path = os.path.join(install_dir, "ayaan.py")

def download_script():
    # Ensure the installation directory exists
    if not os.path.exists(install_dir):
        os.makedirs(install_dir)

    print("Downloading AyaanScript...")
    response = requests.get(ayaan_script_url)
    if response.status_code == 200:
        with open(ayaan_script_path, "wb") as f:
            f.write(response.content)
        print(f"AyaanScript downloaded to: {ayaan_script_path}")
    else:
        print(f"Failed to download AyaanScript. HTTP Status: {response.status_code}")

def add_to_path():
    # Add the installation directory to the system PATH
    print("Adding AyaanScript to PATH...")
    path_var = os.environ.get("Path", "")
    if install_dir not in path_var:
        subprocess.run(
            f'setx PATH "%PATH%;{install_dir}"',
            shell=True,
            check=True
        )
    print("AyaanScript is now globally accessible!")

def main():
    print("Starting AyaanScript installer...")
    download_script()
    add_to_path()
    print("Installation complete! You can now use `ayaan` in the terminal.")

if __name__ == "__main__":
    main()

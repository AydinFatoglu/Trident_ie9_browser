import os
import random
import argparse
import subprocess
import shutil
import time
import sys

def generate_random_number():
    return random.randint(1000, 9999)

def create_directory_structure(base_path, app_number):
    app_folder = f"app_{app_number}"
    app_path = os.path.join(base_path, "apps", app_folder)
    os.makedirs(app_path, exist_ok=True)
    return app_path

def create_ini_file(app_path, url):
    ini_content = f"""
[Main]
url={url}

[Wnd]
Pos=2C0000000000000001000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF810000002B000000FF060000DD030000AE
"""
    ini_path = os.path.join(app_path, "WebApp.ini")
    with open(ini_path, "w") as ini_file:
        ini_file.write(ini_content)
    return ini_path

def main():
    parser = argparse.ArgumentParser(description="Generate WebApp.ini and folder structure")
    parser.add_argument("-url", required=True, help="Full path of the HTML file")
    args = parser.parse_args()

    base_path = os.path.dirname(os.path.abspath(sys.argv[0]))  # Directory of the script/executable
    random_number = generate_random_number()
    app_path = create_directory_structure(base_path, random_number)

    ini_path = create_ini_file(app_path, args.url)
    
    print(f"Directory and INI file created at: {app_path}")

    # Path to webapp.exe
    exe_path = os.path.join(base_path, "webapp.exe")

    # Check if the executable exists
    if not os.path.isfile(exe_path):
        print(f"Error: {exe_path} not found. Ensure that 'webapp.exe' is in the same directory as this script.")
        return

    # Running the original webapp.exe with the newly created ini file
    process = subprocess.Popen([exe_path, f"/app:{random_number}"])

    # Wait for 2 seconds before deleting the apps folder
    time.sleep(2)
    
    # Deleting the apps folder after 2 seconds
    apps_folder = os.path.join(base_path, "apps")
    shutil.rmtree(apps_folder)
    print(f"Deleted the apps folder: {apps_folder}")

if __name__ == "__main__":
    main()

"""Functions for PyBuildJ subcommands

It contains function to be invoked when the subcommands for
the application is invoked
"""

import json
import os
import urllib.request
import sys
from termcolor import colored
from shutil import rmtree
# from pybuildj import project_data

repo_url = "https://repo1.maven.org/maven2/"
build_dir = "build"
class_path = "lib/"
src_dir = "src"
success_color = "green"
fail_color = "red"

#temp code
# dependencies = {
#     "com.google.guava:guava:20.0": "guava-20.0.jar",
#     "junit:junit:4.12": "junit-4.12.jar",
# }
# main_class = "com.myproject.Main"


def pbj_print(args, color="green"):
    print(colored(args, color))


def coordinate_to_path(coordinate):
    parts = coordinate.split(":")
    return "/".join(parts[0].split(".")) + "/"+parts[1] + "/"+parts[2] + "/"+parts[1]+"-"+parts[2]+".jar"

#TODO
#1.To implement a compiler function
def compile():
    pbj_print('Compiling', color="yellow")
    project_data = read_json_config()
    dependencies = project_data.get("dependencies")
    dep_download_status = download_dependencies()
    main_meth_data = project_data.get("main")
    main_meth_path = "/".join(main_meth_data.split("."))
        
    # if dep_download_status:
    if True: #deb code 
        depends = []
        local_class_path = ""
        for coordinate, filename in dependencies.items():
            depends.append(class_path + filename)
        local_class_path = ";".join(depends)
        os.system(f"javac -d {build_dir}/classes/ -cp {local_class_path};src/*.java;  {src_dir}/{main_meth_path}.java") 
        print(f"javac -d {build_dir}/classes/ -cp {local_class_path};src/app/*.java;  {src_dir}/{main_meth_path}.java")
        pbj_print("Compilation complete!")
    else:
        pbj_print("Compilation falied", color="red")

#2.To implement a function to download all the dependencies specified in project.json
def download_dependencies():
    # try:
    #     print("Downloading dependencies")
    #     project_data = read_json_config()
    #     dependencies = project_data.get("dependencies")
    #     if not os.path.exists("lib"):
    #         os.makedirs("lib")

    #     for coordinate, filename in dependencies.items():
    #         url = repo_url + coordinate_to_path(coordinate)
    #         print("Downloading", coordinate, end='', flush=True)
    #         urllib.request.urlretrieve(url, "lib/" + filename)
    #         sys.stdout.write("\r")
    #         print(coordinate, colored(" Download complete", 'green'))
    #     print()
    #     print("Download complete")
    # except Exception:
    #     print()
    #     pbj_print("Error occured while downloading dependences", color="red")
    #     return False
    return True


#3. To generate Jar files when build is invoked
def build():
    pass

#4. To clean the build dir when clean task is invoked
def clean():
    ans = input("Are you sure?")
    if ans == 'y' or ans == 'Y':
        rmtree(build_dir)
    else:
        sys.exit(0)
     
def run():
    project_data = read_json_config()
    main_meth_data = project_data.get("main")
    # os.system(f"java -cp {class_path} build/{main_class}")
    os.system(f"java -cp build/classes/;lib/ {main_meth_data}")


def read_json_config():
    data = {}
    try:
        with open('project.json') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("File project.json not found")
        sys.exit(1) 
        

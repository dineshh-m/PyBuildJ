"""Project Directory Initializer

It contains functions to initialize the project directory 
and creation of project specification file.
"""

from pybuildj import project_name, src_dir
import os
import json
import sys

def init_project()->None:
    """Initializes the project by creating the project directory and 
    configuring the project name
    """

    global project_name
    current_dir = os.getcwd()
    default = os.path.basename(current_dir)
    ans = input(f"Enter the project name (default: {default}):")
    if ans != '':
        project_name = ans
    else:
        project_name = default

    src_path = os.path.join(current_dir, src_dir)

    try:
        os.makedirs(src_path)
    except FileExistsError:
        print("src directory already exists make sure the current directory is not a project directory", file=sys.stderr)
        sys.exit()
        
    #Creating the Project config and dependencies file
    with open('project.json', 'w') as proj_file:
        initial_dict = get_init_string()
        json.dump(initial_dict, proj_file, indent=2)


def get_init_string()->str:
    """Returns a initial confiuration JSON text

    Returns
    -------
    a initial JSON configuration text about name of project, version and author.
    """

    init_dict = {
            "name" : project_name,
            "version" : 1.0,
            "author" : 'Dinesh',
            "dependencies": {},
            "resources": []
            }
    return init_dict

# --- Import the required modules:
import json
import os
import subprocess

def update_modules():
    # --- Create an empty list to add the completed updates to:
    processed_modules = []
    try:
        # --- Attempt to load the installed_modules.json file:
        with open("./installed_modules.json", mode="r") as data_file:
            installed_modules = json.load(data_file)
            for module in installed_modules:
                # --- If the module name is one of the below, ignore it ann move to the next:
                if module["name"] == "pip" or module["name"] == "pip" or module["name"] == "setuptools" or module["name"] == "wheel":
                    pass
                else:
                    # --- Update the module and add the results to a dictionary that is then added to the processed_modules list:
                    print(f"Updating: {module['name']}")
                    os.system(f"pip3 install --upgrade {module['name']}")
                    updated_version_details = subprocess.check_output(["pip3", "show", module["name"]]).split()
                    updated_version = str(updated_version_details[3]).replace("b","", 1).strip("'")
                    processed_modules.append({"name": module['name'],
                                              "version_before": module['version'],
                                              "version_updated_to": updated_version
                                              })
        
        # --- Print out the list of updated modules:        
        print(processed_modules)
    
    # --- If the installed_modules.json file is not found, run pip3 to create it:    
    except FileNotFoundError:
        os.system("pip3 list outdated --format json > installed_modules.json")
        return update_modules()

# --- Start the program:    
update_modules()
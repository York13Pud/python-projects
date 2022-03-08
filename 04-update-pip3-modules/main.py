# --- Import the required modules:
from datetime import datetime
import json
import os
import platform
import subprocess


def build_final_json_output(updated_packages):
    """This function combines the list of updated modules with a dictionary that has the hostname and python
    version and outputs the dictionary to a JSON file."""
    
    # --- Build a dictionary with the hostname, python version and the list of updated modules:
    completed_updates = {"hostname": os.uname()[1],
                         "python_version": platform.python_version(),
                         "updates": updated_packages
    }
    
    # --- Output the completed_updates dictionary to a JSON file:
    with open("./updated_modules.json", mode="w") as out_file:
        json.dump(completed_updates, out_file)


def get_date_time():
    """Gets the date and time and returns back a list with the date and time formatted correctly."""
    
    # --- Get the current date and time:
    current_date_time = datetime.now()
    # --- Define a variable for the date:
    current_date = current_date_time.date().strftime("%Y-%m-%d")
    # --- Define a variable for the time:
    current_time = current_date_time.time().strftime("%H:%M")
    # --- Define a variable to create a list with formatted date and time:
    date_time_list = [current_date, current_time]
    # --- Return the date_time_list:
    return(date_time_list)


def update_modules():
    """This function will update any pip modules that are in a JSON file and add the results to a list of dictionaries."""
    
    # --- Create an empty list to add the completed updates to:
    processed_modules = []
    try:
        # --- Attempt to load the installed_modules.json file:
        with open("./installed_modules.json", mode="r") as data_file:
            installed_modules = json.load(data_file)
            for module in installed_modules:
                # --- If the module name is one of the below, ignore it ann move to the next:
                if module["name"] == "pip" or module["name"] == "setuptools" or module["name"] == "wheel":
                    pass
                else:
                    # --- Update the module and add the results to a dictionary that is then added to the processed_modules list:
                    print(f"Updating: {module['name']}")
                    started_at = get_date_time()
                    os.system(f"pip3 install --upgrade {module['name']}")
                    finished_at = get_date_time()
                    updated_version_details = subprocess.check_output(["pip3", "show", module["name"]]).split()
                    updated_version = str(updated_version_details[3]).replace("b","", 1).strip("'")
                    processed_modules.append({"name": module['name'],
                                              "start_date": started_at[0],
                                              "start_time": started_at[1],
                                              "version_before": module['version'],
                                              "finished_date": finished_at[0],
                                              "finished_time": finished_at[1],
                                              "version_updated_to": updated_version
                                              })
                    
        build_final_json_output(updated_packages = processed_modules)

    # --- If the installed_modules.json file is not found, run pip3 to create it:    
    except FileNotFoundError:
        os.system("pip3 list outdated --format json > installed_modules.json")
        return update_modules()


# --- Start the program:    
update_modules()
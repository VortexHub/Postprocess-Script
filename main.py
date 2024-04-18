# Made By Vortex
# NOTE THIS IS BETA 
# First Release 1.0
import json
import pyperclip
from tkinter import Tk
from tkinter.filedialog import askopenfilename


print("[Credit]: Made by @VortexHub on GitHub")

def convert_to_game_engine_format(json_data):
    output = ""
    for item in json_data:
        if item.get("Type") == "PostProcessComponent":
            output += "Begin Object Class=/Script/Engine." + item["Type"] + " Name=\"" + item["Name"] + "\" ExportPath=\"" + item["Class"] + "'/" + item["Name"] + "'\"\n"
            output += "   Settings=("
            if "Properties" in item and "Settings" in item["Properties"]:
                settings = item["Properties"]["Settings"]
                for key, value in settings.items():
                    if isinstance(value, dict):
                        output += key + "=("
                        for sub_key, sub_value in value.items():
                            output += sub_key + "=" + str(sub_value) + ","
                        output = output[:-1] + "),"
                    else:
                        output += key + "=" + str(value) + ","
                output = output[:-1] + ")"
            output += "\n"
            if "Priority" in item:
                output += "   Priority=" + str(item["Priority"]) + "\n"
            if "BlendRadius" in item:
                output += "   BlendRadius=" + str(item["BlendRadius"]) + "\n"
            if "BlendWeight" in item:
                output += "   BlendWeight=" + str(item["BlendWeight"]) + "\n"
            output += "End Object\n\n"
    return output

def main():
    # Open file explorer to JSON file
    Tk().withdraw() # I don't want a full GUI, so keep the root window from appearing
    file_path = askopenfilename(title="Select JSON file", filetypes=[("JSON files", "*.json")]) # show an "Open" dialog box and return the path to the selected file

    if not file_path:
        print("No file selected.")
        return

    # Read JSON data from file
    with open(file_path, "r") as file:
        json_data = json.load(file)

    # Replace "FortniteGame/Content/" with "/Game/" for items with "Type" as "PostProcessComponent"
    for item in json_data:
        if "Type" in item and item["Type"] == "PostProcessComponent" and "Class" in item:
            item["Class"] = item["Class"].replace("FortniteGame/Content/", "/Game/")

    # Convert JSON data to game engine format
    output_format = convert_to_game_engine_format(json_data)
    
    # Copy output to clipboard
    pyperclip.copy(output_format)
    print("Clipboard Updated!")

if __name__ == "__main__":
    main()
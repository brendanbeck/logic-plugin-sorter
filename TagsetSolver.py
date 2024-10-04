import glob
import plistlib

from Plugin import Plugin


def get_all_plugins(directory: str = "/Library/Audio/Plug-Ins/Components") -> None:
    plugins_list = []
    components_paths = glob.glob(directory + "/*.component", recursive=True)
    for component_path in components_paths:
        with open(component_path + "/Contents/Info.plist", 'rb') as infile:
            component_plist = plistlib.load(infile)
            if component_plist.get("AudioComponents") is None:
                print(component_path + " could not be sorted.")
                continue
            for component_metadata in component_plist["AudioComponents"]:
                plugins_list.append(Plugin(component_metadata["name"], component_metadata["manufacturer"],
                                           component_metadata["subtype"], component_metadata["type"]))
    print()

get_all_plugins()

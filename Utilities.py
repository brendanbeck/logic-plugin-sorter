import glob
import json
import plistlib
import shutil

from Plugin import Plugin


def load_json(filename: str) -> dict:
    with open(filename, 'r') as file:
        return json.load(file)


def backup_tags(source_directory: str, target_directory: str, time: str) -> str:
    target_directory_name = target_directory + "/Tags-backup" + time
    shutil.copytree(source_directory, target_directory_name)
    return target_directory_name


def get_plugins(directory: str) -> dict[str, list[str] | list[Plugin]]:
    sortable_plugins = []
    unsortable_plugins = []
    plugins = {"sortable_plugins": sortable_plugins,
               "unsortable_plugins": unsortable_plugins}

    components_paths = glob.glob(directory + "/*.component", recursive=True)
    for component_path in components_paths:
        with open(component_path + "/Contents/Info.plist", 'rb') as infile:
            component_plist = plistlib.load(infile)
            if component_plist.get("AudioComponents") is None:
                unsortable_plugins.append(component_path)
                continue
            for component_metadata in component_plist["AudioComponents"]:
                sortable_plugins.append(Plugin(component_metadata["name"], component_metadata["manufacturer"],
                                               component_metadata["subtype"], component_metadata["type"]))
    return plugins


def set_db_properties(directory: str, categories: list[str]) -> None:
    with open(directory + "/MusicApps.properties", 'rb') as infile:
        music_apps_props_plist = plistlib.load(infile)
    music_apps_props_plist["sorting"] = categories
    with open(directory + "/MusicApps.properties", 'wb') as infile:
        plistlib.dump(music_apps_props_plist, infile)


def set_db_tagpool(directory: str, categories: list[str]) -> None:
    with open(directory + "/MusicApps.tagpool", 'rb') as infile:
        music_apps_tp_plist = plistlib.load(infile)
    [music_apps_tp_plist.pop(key) for key in list(music_apps_tp_plist.keys()) if key != ""]
    category_tagpool_map = {}
    for category in categories:
        category_tagpool_map[category] = 0
    music_apps_tp_plist.update(category_tagpool_map)
    with open(directory + "/MusicApps.tagpool", 'wb') as infile:
        plistlib.dump(music_apps_tp_plist, infile)

import logging
from datetime import datetime

import Utilities

time = datetime.now().strftime("%m%d%Y%H%M%S")
logger = logging.getLogger('logic-plugin-sorter')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("logs/logic-plugin-sorter" + time + ".log")
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.log(20, "Running logic plugin sorter...")

config = Utilities.load_json("config.json")
logger.log(20, "Configuration used: " + str(config))

backup_dir = Utilities.backup_tags(config["tags_directory"], config["tags_backup_directory"], time)
logger.log(20, "Backup of tags database created at " + backup_dir)

plugins = Utilities.get_plugins(config["plugins_directory"])
logger.log(20, str(len(plugins.get("unsortable_plugins"))) + " plugins have insufficient plist data and "
           + "cannot be sorted: " + str(plugins["unsortable_plugins"]))
logger.log(20, "Found " + str(len(plugins.get("sortable_plugins"))) + " sortable plugins")

logger.log(20, "Writing categories to MusicApps.properties...")
Utilities.set_db_properties(config["tags_directory"], config["categories"])

logger.log(20, "Writing categories to MusicApps.tagpool...")
Utilities.set_db_tagpool(config["tags_directory"], config["categories"])



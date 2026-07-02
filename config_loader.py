import os
import yaml


def config_loader(filename="config.yaml", search_paths=None):
    if search_paths is None:
        search_paths = [
            os.getcwd(),
            os.path.dirname(os.path.abspath(__file__)),
        ]
<<<<<<< HEAD

    for path in search_paths:
        full_path = os.path.join(path, filename)
        if os.path.isfile(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
=======
       
    for path in search_paths:
        full_path = os.path.join(path, filename)
        print(full_path)
        if os.path.isfile(full_path):
            with open(full_path, "r", encoding="UTF-8") as f:
>>>>>>> feat_two_player_rps
                data = yaml.safe_load(f)
            return data if data else {}

    raise FileNotFoundError(f"Could not find '{filename}' in: {search_paths}")



<<<<<<< HEAD
config = config_loader("config.yaml")
=======
config = config_loader("config.yaml")
print(config)
>>>>>>> feat_two_player_rps

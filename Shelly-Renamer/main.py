import json
from math import e
import requests

file_path = "core.device_registry"

with open(file_path, "r", encoding='utf-8') as file:
    data = json.load(file)

    for device in data["data"]["devices"]:
        if device["manufacturer"] == "Shelly":
            if device["name_by_user"] is not None:
                
                print(device["name_by_user"])
                new_name = str(device["name_by_user"]).replace(" Shelly ", "").replace("ü", "ue").replace("ä", "ae").replace("ö", "oe").replace("ß", "ss").replace("-", "_").replace("PM", "").replace("Plug", "").replace("HT", "").replace("DW", "")
                
                try:
                    # Gen 1
                    url = device["configuration_url"] +"/settings"
                    print("\t"+url)
                    requests.post(url, data={"name": new_name}, timeout=15)
                except Exception as e:
                    try:
                        # Gen 2
                        url = device["configuration_url"] +"/rpc/Sys.SetConfig?config={\"device\":{\"name\":{\""+new_name+"\"}}}"
                        print("\t"+url)
                        requests.get(url, timeout=15)
                    except Exception as ex:
                        print("\t\033[91mError\033[0m")
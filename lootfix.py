import argparse
import json
import os


def edit_json_files(folder_path):
    for subdir, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(subdir, file)
            if file_path.endswith('.json'):

                print(f"Processing file: {file_path}")

                with open(file_path, 'r+') as json_file:
                    data = json.load(json_file)

                for pool in data.get("pools", []):
                    try:
                        try:
                            if pool['rools']['min'] == pool['rools']['max'] == 1:
                                pass
                            else:
                                if pool['rools']['min'] > 1:
                                    pool['rools']['min'] = int(pool['rools']['min'] // 2)
                                if pool['rools']['max'] > 1:
                                    pool['rools']['max'] = int(pool['rools']['max'] // 2)
                        except:
                            if pool['rools'] > 1:
                                pool['rools'] = int(pool['rools'] // 2)
                    except:
                        print("no rools found")

                    for entry in pool['entries']:
                        if entry['type'] == "empty":
                            entry['weight'] = entry['weight'] * 4
                        else:
                            try:
                                if entry['weight'] > 1:
                                    entry['weight'] = entry['weight'] // 2
                            except:
                                print("no weight found")
                        try:
                            for func in entry["functions"]:
                                try:
                                    if func["count"]['min'] == func["count"]['max'] == 1:
                                        pass
                                    else:
                                        if func["count"]['min'] > 1:
                                            func["count"]['min'] = 0.0
                                        if func["count"]['max'] > 1:
                                            func["count"]['max'] = float(func["count"]['max'] // 2)
                                except:
                                    if func["count"] > 1:
                                        func["count"] = int(func["count"] // 2)
                        except:
                            print("no count found")
                # Save the modified JSON back to the file
                with open(file_path, 'w+') as json_file:
                    json.dump(data, json_file, indent=2)


def main():
    parser = argparse.ArgumentParser(description='Edit JSON files in loot tables.')
    parser.add_argument('-f', '--folder', required=True, help='Root folder containing JSON files.')
    args = parser.parse_args()
    root_folder = args.folder
    paths = ["data\\pixelmon\\loot_tables", "data\\minecraft\\loot_tables"]
    for path in paths:
        edit_json_files(os.path.join(root_folder, path))


if __name__ == "__main__":
    main()

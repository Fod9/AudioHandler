import os
from audio_combiner import combine_audio, parse_audio
import shutil

accepted_extensions = ['.mp3', '.wav', ".ogg"]
subdirectories = {}


def delete_parsed_folders(path_to_folder):
    for root, dirs, files in os.walk(path_to_folder):
        for dir in dirs:
            if dir == "parsed":
                parsed_path = os.path.join(root, dir)
                print(f"Deleting {parsed_path}")
                shutil.rmtree(parsed_path)
            if dir == "Combined":
                combined_path = os.path.join(root, dir)
                print(f"Deleting {combined_path}")
                shutil.rmtree(combined_path)



def folder_exploration(path_to_folder, recursive=False, combine=True, parse=False, parse_time=0):

    delete_parsed_folders(path_to_folder)

    if recursive:
        for root, dirs, files in os.walk(path_to_folder):

            for dir in dirs:
                subdirectories[dir] = {
                    "path": os.path.join(root, dir),
                    "files": []
                }
            for file in files:
                if file.endswith(tuple(accepted_extensions)):
                    subdirectories[root.split("/")[-1]]["files"].append(file)
    else:
        subdirectories = {}
        for file in os.listdir(path_to_folder):
            if file.endswith(tuple(accepted_extensions)):
                file_name = file.split(".")[0]
                subdirectories[file_name] = {
                    "path": path_to_folder,
                    "files": [file]
                }
    if combine:
        combine_audio(subdirectories)
    if parse:
        combined_files = combine_audio(subdirectories)
        for file in combined_files:
            parse_audio(file, parse_time)
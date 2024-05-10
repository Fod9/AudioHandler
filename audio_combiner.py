import os

from pydub import AudioSegment


def combine_audio(subdirectories, save=True):
    combined_files = []
    directories = subdirectories
    for key, value in directories.items():
        if save:
            print(f"Combining files in {key}")
        combined = AudioSegment.empty()
        for file in value["files"]:
            combined += AudioSegment.from_file(os.path.join(value["path"], file))
        if save:
            os.makedirs(f"{value['path']}/Combined", exist_ok=True)
            combined.export(f"{value['path']}/Combined/{key}.mp3", format="mp3")
            print(f"Combined file exported to {value['path']}/{key}.mp3")
        combined_files.append({
            "path": value["path"] + "/Combined",
            "file": f"{key}.mp3",
            "name": f"{key}"
        })
    print("All files combined")

    return combined_files


def parse_audio(file, parse_time):  # parse_time in seconds
    # if parsed folder does not exist, create it
    parsed_folder = os.path.join(file["path"], "parsed")
    os.makedirs(parsed_folder, exist_ok=True)
    audio_file = AudioSegment.from_file(os.path.join(file["path"], file["file"]))
    for i in range(0, len(audio_file), parse_time * 1000):
        audio_file[i:i + parse_time * 1000].export(f"{parsed_folder}/{file['name']}_{i / 1000}.mp3", format="mp3")
    print(f"File parsed to {parsed_folder} with {parse_time}s intervals")


print("All files parsed")

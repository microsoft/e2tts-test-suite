import argparse
import os
import json

import soundfile as sf
from tqdm import tqdm


def create_file_list(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
    file_list = []
    for item in data:
        file_list.append(item["audio_prompt"].split("/")[2:])
    return file_list


def process_files(file_list, data_path, output_path):
    for file in tqdm(file_list):
        file_path = os.path.join(data_path, *file)
        # read the audio file
        audio, sr = sf.read(file_path.replace(".wav", ".flac"))
        # cut and keep only the last 3 seconds
        audio = audio[-3 * sr :]
        # save the audio file
        os.makedirs(os.path.join(output_path, *file[:-1]), exist_ok=True)
        output_file = os.path.join(output_path, *file)
        if not os.path.exists(output_file):
            sf.write(output_file, audio, sr)
    return


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_path",
        type=str,
        default="data/LibriSpeech/test-clean",
        help="Output path to save the extracted files",
    )
    parser.add_argument(
        "--input_json",
        type=str,
        default="data/e2tts_librispeech_pc_test_clean.json",
        help="test-clean.tar.gz URL",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        default="data/LibriSpeech/test-clean-last-3s",
        help="Output path to save the extracted files",
    )

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    file_list = create_file_list(args.input_json)
    print("Found {} files".format(len(file_list)))
    process_files(file_list, args.data_path, args.output_path)


if __name__ == "__main__":
    main()

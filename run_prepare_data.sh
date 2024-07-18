#!/bin/bash

# download and untar the data
if [ ! -d data/LibriSpeech/test-clean ]; then
    mkdir -p data
    wget http://www.openslr.org/resources/12/test-clean.tar.gz -P ./data
    (cd ./data && tar -xvzf test-clean.tar.gz)
    rm data/test-clean.tar.gz
fi

# preparing the audio prompts by cutting last 3 sec
if [ ! -d data/LibriSpeech/test-clean-last-3s ]; then
    cp assets/e2tts_librispeech_pc_test_clean.json data/e2tts_librispeech_pc_test_clean.json
    python utils/process_data.py \
        --data_path data/LibriSpeech/test-clean \
        --input_json data/e2tts_librispeech_pc_test_clean.json \
        --output_path data/LibriSpeech/test-clean-last-3s
fi

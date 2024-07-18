# E2 TTS Test Set Reproduction Tool

Reproducing the zero-shot TTS test set used in [E2 TTS: Embarrassingly Easy Fully Non-Autoregressive Zero-Shot TTS](https://arxiv.org/abs/2406.18009).
The data is based on [LibriSpeech-PC](https://www.openslr.org/145/), which is [LibriSpeech](https://www.openslr.org/12/) with restored punctuation and capitalization. 

## Motivation

We are releasing this test set reproduction tool because we noticed that various zero-shot TTS papers used their own test sets due to the randomness in selecting the audio prompt. Our test set is unique in that it contains punctuation and capitalization, so we believe the release of this test set is necessary for future works.

Additionally, while most works (e.g., VALL-E, Voicebox) used 3 seconds of trimmed audio for the audio prompt, some works trimmed redundant silence (e.g., Audiobox) or used an entire utterance (e.g., VALL-E 2, MELLE), making comparisons among different systems difficult. We hope this test set standardizes the evaluation process and makes comparing different zero-shot TTS models easier.

## Reproducing the Test Data
The following command will generate `data/LibriSpeech` folder.
```
$ conda create -n e2tts_test_set python=3.9
$ conda activate e2tts_test_set
$ pip install -r requirements.txt
$ bash run_prepare_data.sh
```

## Data and Test Protocol

[assets/e2tts_librispeech_pc_test_clean.json](assets/e2tts_librispeech_pc_test_clean.json) contains all the necessary information as follows.

```
[
    {
        "key": "1188-133604-0001",
        "ground_truth": "LibriSpeech/test-clean/1188/133604/1188-133604-0001.flac",
        "text_prompt": "They unite every quality; and sometimes you will find me referring to them as colorists, sometimes as chiaroscurists.",
        "audio_prompt": "LibriSpeech/test-clean-last-3s/1188/133604/1188-133604-0022.wav",
        "transcription_of_audio_prompt": "you need not think to keep out of the way of him."
    },
    ...
]
```

Test protocol
  - The audio should be generated from `text_prompt`, `audio_prompt`, and `transcription_of_audio_prompt`.
  - Objective evaluation
      - SIM-o should be computed based on the generated audio and `audio_prompt` using [WavLM-large-based speaker verification model](https://github.com/microsoft/UniSpeech/tree/main/downstreams/speaker_verification).
      - WER should be computed based on the generated audio by using [HuBERT-Large based ASR](https://huggingface.co/facebook/hubert-large-ls960-ft) .
  - Subjective evaluation
      - [assets/subjective_evaluation_key.txt](assets/subjective_evaluation_key.txt) contains the `key` for subjective evaluation.
      - Each sample is assessed by 12 native English evaluators.


## Citation

Please cite the following paper if you find this test set useful for your work.

```bibtex
@misc{eskimez2024e2ttsembarrassinglyeasy,
      title={{E2 TTS}: Embarrassingly Easy Fully Non-Autoregressive Zero-Shot {TTS}}, 
      author={Sefik Emre Eskimez and Xiaofei Wang and Manthan Thakker and Canrun Li and Chung-Hsien Tsai and Zhen Xiao and Hemin Yang and Zirun Zhu and Min Tang and Xu Tan and Yanqing Liu and Sheng Zhao and Naoyuki Kanda},
      year={2024},
      eprint={2406.18009},
      archivePrefix={arXiv},
      primaryClass={eess.AS},
      url={https://arxiv.org/abs/2406.18009}, 
}

@inproceedings{meister2023librispeech,
  title={LibriSpeech-PC: Benchmark for Evaluation of Punctuation and Capitalization Capabilities of end-to-end ASR Models},
  author={Meister, Aleksandr and Novikov, Matvei and Karpov, Nikolay and Bakhturina, Evelina and Lavrukhin, Vitaly and Ginsburg, Boris},
  booktitle={2023 IEEE Automatic Speech Recognition and Understanding Workshop (ASRU)},
  pages={1--7},
  year={2023},
  organization={IEEE}
}

@inproceedings{panayotov2015librispeech,
  title={Librispeech: an asr corpus based on public domain audio books},
  author={Panayotov, Vassil and Chen, Guoguo and Povey, Daniel and Khudanpur, Sanjeev},
  booktitle={2015 IEEE international conference on acoustics, speech and signal processing (ICASSP)},
  pages={5206--5210},
  year={2015},
  organization={IEEE}
}
```

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

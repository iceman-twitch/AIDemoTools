from TTS.api import TTS
# tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
tts = TTS("xtts_v2.0.2", gpu=False)

# generate speech by cloning a voice using default settings
tts.tts_to_file(text="Az én nevem JÉGEMBER",
                file_path="output.wav",
                speaker_wav=["./sample.wav"],
                language="hu",
                split_sentences=False,
                )
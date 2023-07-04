import openai
openai.api_key = "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"
audio_file= open("/home/yerassyl/Загрузки/as0q09BsHF.mp3", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)
print(transcript)

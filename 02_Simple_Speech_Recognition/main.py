import assemblyai as aai
from api_secrets import API_KEY_ASSEMBLYAI

aai.settings.api_key = API_KEY_ASSEMBLYAI

transcriber = aai.Transcriber()
config = aai.TranscriptionConfig(speaker_labels = True)
transcript = transcriber.transcribe("output.wav", config)
print(transcript.text)
for utterance in transcript.utterances:
    print(f"Speaker {utterance.speaker}: {utterance.text}")
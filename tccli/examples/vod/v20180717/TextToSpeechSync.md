**Example 1: 使用 ElevenLabs 模型同步语音合成**

指定 ElevenLabs V3 模型与官方音色合成，并通过 ExtParam 调整音色参数和输出格式。

Input: 

```
tccli vod TextToSpeechSync --cli-unfold-argument  \
    --ModelName ElevenLabs \
    --ModelVersion custom-model-ll-v3 \
    --Text 种子在土里沉默，是为了破土时的惊雷。 \
    --VoiceId 21m00Tcm4TlvDq8ikWAM \
    --LanguageBoost zh \
    --ExtParam {"voice_settings":{"stability":0.5,"similarity_boost":0.8,"speed":1.1},"seed":42,"audio_setting":{"format":"mp3","sample_rate":44100,"bitrate":128}} \
    --Output.Type url \
    --SubAppId 221***
```

Output: 
```
{
    "Response": {
        "AudioData": "",
        "AudioUrl": "https://speech-1300828900.cos.a*************************************07.mp3",
        "ExtInfo": "{\"audio_format\":\"mp3\",\"audio_sample_rate\":44100}",
        "RequestId": "9f3a1c2e-5b7d-4e8f-a1b2-c3d4e5f6a7b8"
    }
}
```

**Example 2: 同步语音合成**

同步语音合成

Input: 

```
tccli vod TextToSpeechSync --cli-unfold-argument  \
    --Text 种子在土里沉默，是为了破土时的惊雷。 \
    --VoiceId minimax_5*********527-4dff \
    --LanguageBoost zh \
    --ExtParam {"model": "minimax-speech-2.8-hd", "voice_setting": {"speed": 2.0, "vol": 2.0}, "audio_setting": {"sample_rate": 32000, "bitrate": 128000, "format": "mp3"}} \
    --SubAppId 221***
```

Output: 
```
{
    "Response": {
        "AudioData": "",
        "AudioUrl": "https://laurie-tmp-1300828900.cos.a***********************************b70-c745-4335-bbfc-b2f6c00ac0b2.mp3",
        "ExtInfo": "{\"audio_format\":\"mp3\",\"audio_length\":1836,\"audio_sample_rate\":32000,\"audio_size\":0,\"word_count\":16}",
        "RequestId": "a24cdb70-c745-4335-bbfc-b2f6c00ac0b2"
    }
}
```


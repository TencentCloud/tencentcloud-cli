**Example 1: 同步语音合成**

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


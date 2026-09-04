**Example 1: 同步音色克隆**

同步音色克隆

Input: 

```
tccli vod CloneVoiceSync --cli-unfold-argument  \
    --AudioFileId 966263******778501 \
    --LanguageBoost zh \
    --ExtParam {"text": "种子在土里沉默，是为了破土时的惊雷。", "tts_model":"minimax-speech-2.8-hd"} \
    --SubAppId 221*** \
    --AudioUrl https://laurie-tmp-1300828900.cos.accelerate*******************************************Async-773ca8f1756ed5fd016988dccb91eaa9t.wav
```

Output: 
```
{
    "Response": {
        "DemoAudio": "https://laurie-tmp-1300828900.cos.acce**************************************c3-41db-aa7a-29931e416b5b-preview.mp3",
        "ExtInfo": "{\"audio_length\":0,\"word_count\":34}",
        "VoiceId": "minimax_9*********d39-40d7",
        "RequestId": "60f2d5dc-2dc3-41db-aa7a-29931e416b5b"
    }
}
```


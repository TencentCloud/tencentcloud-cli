**Example 1: 音频声纹比对**

比对两段音频的声纹相似度

Input: 

```
tccli asr VoicePrintCompare --cli-unfold-argument  \
    --VoiceFormat 0 \
    --SampleRate 16000 \
    --SrcAudioData AAAAADADAAAAA \
    --DestAudioData AAAAADADAAAAA
```

Output: 
```
{
    "Response": {
        "Data": {
            "Score": "100.0",
            "Decision": "1"
        },
        "RequestId": "dsadasdasdasdasad"
    }
}
```


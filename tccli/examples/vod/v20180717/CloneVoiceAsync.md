**Example 1: 音色克隆**

音色克隆

Input: 

```
tccli vod CloneVoiceAsync --cli-unfold-argument  \
    --SubAppId 260***028 \
    --AudioUrl https://laurie-tmp-1300828900.cos.accelerate.m**********************************************136a4dea53b5db4493680d0d51bf33e2t-preview.mp3 \
    --LanguageBoost zh \
    --ExtParam { "model":"minimax-speech-02-hd", "text": "种子在土里沉默是为了破土时的惊雷" } \
    --SessionId 6bb56a09278***********6dab783efe
```

Output: 
```
{
    "Response": {
        "TaskId": "260085028-CloneVoiceAsync-d56011ff47099d4f1788e0b7f851c1e1t",
        "RequestId": "ede949b5-2f8e-40e8-9fde-ee5cdb64d24b"
    }
}
```


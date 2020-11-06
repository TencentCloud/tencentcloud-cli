**Example 1: 一句话识别相关接口**

实时识别60s以内的短语音。

Input: 

```
tccli aai SentenceRecognition --cli-unfold-argument  \
    --ProjectId 0 \
    --SubServiceType 2 \
    --EngSerViceType 8k \
    --SourceType 0 \
    --Url http%3A%2F%2Fliqiansunvoice-1255628450.cosgz.myqcloud.com%2Fdemo.mp3 \
    --SecretId 111 \
    --Timestamp 111 \
    --VoiceFormat mp3 \
    --UsrAudioKey www \
    --Data 00011100111 \
    --DataLen 11111
```

Output: 
```
{
    "Response": {
        "Result": "张先生，您好。那个为了规范保险从业人员的销售行为，也为了更好的保护您的合法权益。",
        "RequestId": "8984d9a9-343f-4c67-8fd9-5c79510a12da"
    }
}
```


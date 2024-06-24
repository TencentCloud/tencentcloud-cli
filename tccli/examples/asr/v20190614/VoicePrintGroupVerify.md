**Example 1: 说话人验证1:N**

提供一段音频数据和提前注册的一组说话人数据进行比对， 返回topN

Input: 

```
tccli asr VoicePrintGroupVerify --cli-unfold-argument  \
    --VoiceFormat 1 \
    --SampleRate 16000 \
    --Data UklGRsb7AQBXQVZFZm10IBAAAAAB \
    --GroupId test \
    --TopN 2
```

Output: 
```
{
    "Response": {
        "Data": {
            "VerifyTops": [
                {
                    "Score": "100.0",
                    "SpeakerId": "张三",
                    "VoicePrintId": "03c7c4-34e1-4cc2-97d4-f031bc6538d0"
                },
                {
                    "Score": "89.0",
                    "SpeakerId": "李四",
                    "VoicePrintId": "16a936-c0c9-44b8-81e6-19515a9515ef"
                }
            ]
        },
        "RequestId": "affe4cc1-7158-ad-aefc-371fce09c092"
    }
}
```


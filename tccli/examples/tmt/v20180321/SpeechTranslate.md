**Example 1: API调用**



Input: 

```
tccli tmt SpeechTranslate --cli-unfold-argument  \
    --ProjectId 0 \
    --SessionUuid sid-1516105689129 \
    --Source zh \
    --Target en \
    --AudioFormat 83886080 \
    --Seq 0 \
    --IsEnd 1 \
    --Data 
```

Output: 
```
{
    "Response": {
        "RecognizeStatus": 0,
        "RequestId": "6e698139-615a-4d42-8dea-6bfada24e83c",
        "Seq": 0,
        "SessionUuid": "sid-1516105689129",
        "Source": "zh",
        "SourceText": "你好。",
        "Target": "en",
        "TargetText": "Hello."
    }
}
```


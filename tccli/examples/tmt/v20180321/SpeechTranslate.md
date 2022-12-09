**Example 1: API调用**



Input: 

```
tccli tmt SpeechTranslate --cli-unfold-argument  \
    --Target en \
    --Seq 0 \
    --ProjectId 0 \
    --SessionUuid sid-1516105689129 \
    --Source zh \
    --AudioFormat 83886080 \
    --Data =%2F%2FtQxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
......
MGCwUAU4UeWgJDOGmC2JgzouqHJQBsZiKUicVTU5UGTZ6mVJYlri5s9geZdCjBnExqtEsaw%2F5rtShQ6UOkolgkGSpWK \
    --IsEnd 1
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
        "TargetText": "Hello.",
        "VadSeq": 0
    }
}
```


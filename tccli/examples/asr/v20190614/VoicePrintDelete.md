**Example 1: 说话人删除**

删除保存的说话人信息

Input: 

```
tccli asr VoicePrintDelete --cli-unfold-argument  \
    --VoicePrintId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "VoicePrintId": "abc",
            "SpeakerNick": "abc"
        },
        "RequestId": "abc"
    }
}
```


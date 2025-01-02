**Example 1: 说话人删除**

删除保存的说话人信息

Input: 

```
tccli asr VoicePrintDelete --cli-unfold-argument  \
    --VoicePrintId 34a0a2b-922f******90302f155a6d
```

Output: 
```
{
    "Response": {
        "Data": {
            "VoicePrintId": "34a0a2b-922f******90302f155a6d",
            "SpeakerNick": "小明"
        },
        "RequestId": "676a22c********3625b0"
    }
}
```


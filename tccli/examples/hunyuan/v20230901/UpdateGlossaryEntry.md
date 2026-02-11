**Example 1: 更新成功**



Input: 

```
tccli hunyuan UpdateGlossaryEntry --cli-unfold-argument  \
    --GlossaryId 3177dfae1f8cb180dfcc1bea2ddf19f6 \
    --Entries.0.EntryId cf0a1f13edae52ef71be9e46fc26ec59 \
    --Entries.0.SourceTerm Cloud Storage1 \
    --Entries.0.TargetTerm 云存储1
```

Output: 
```
{
    "Response": {
        "Entries": [
            {
                "EntryId": "cf0a1f13edae52ef71be9e46fc26ec59",
                "SourceTerm": "Cloud Storage1",
                "TargetTerm": "云存储1"
            }
        ],
        "RequestId": "6da07c33-e4c4-466b-a3f0-6f04e4291fb9"
    }
}
```


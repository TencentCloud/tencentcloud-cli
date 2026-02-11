**Example 1: 查询成功**



Input: 

```
tccli hunyuan ListGlossaryEntry --cli-unfold-argument  \
    --GlossaryId 3177dfae1f8cb180dfcc1bea2ddf19f6 \
    --Page 1 \
    --PageSize 2
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
        "Page": 1,
        "PageSize": 2,
        "Total": 2,
        "RequestId": "a5f73bfb-6725-45b1-8294-0af419fd61b0"
    }
}
```


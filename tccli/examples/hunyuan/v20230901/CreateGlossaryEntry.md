**Example 1: 添加成功**



Input: 

```
tccli hunyuan CreateGlossaryEntry --cli-unfold-argument  \
    --GlossaryId 3177dfae1f8cb180dfcc1bea2ddf19f6 \
    --Entries.0.SourceTerm Cloud Storage \
    --Entries.0.TargetTerm 云存储
```

Output: 
```
{
    "Response": {
        "Entries": [
            {
                "SourceTerm": "Cloud Storage",
                "TargetTerm": "云存储"
            }
        ],
        "RequestId": "76c19884-c0bf-47ca-b289-8bad552b137a"
    }
}
```


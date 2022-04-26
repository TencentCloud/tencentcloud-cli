**Example 1: 获取索引信息**



Input: 

```
tccli cls DescribeIndex --cli-unfold-argument  \
    --TopicId 826f8b26-b054-4a0d-8c8e-f3d609f5e0ea
```

Output: 
```
{
    "Response": {
        "TopicId": "826f8b26-b054-4a0d-8c8e-f3d609f5e0ea",
        "Status": true,
        "Rule": {
            "FullText": {
                "CaseSensitive": false,
                "Tokenizer": "-=/?"
            },
            "KeyValue": {
                "CaseSensitive": false,
                "KeyValues": [
                    {
                        "Key": "age",
                        "Value": {
                            "Type": "long",
                            "SqlFlag": true
                        }
                    }
                ]
            },
            "Tag": {
                "CaseSensitive": false,
                "KeyValues": [
                    {
                        "Key": "__TAG__.timestamp",
                        "Value": {
                            "Type": "long",
                            "SqlFlag": true
                        }
                    }
                ]
            }
        },
        "ModifyTime": "2021-01-13 21:00:08",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7",
        "IncludeInternalFields": true,
        "MetadataFlag": 1
    }
}
```


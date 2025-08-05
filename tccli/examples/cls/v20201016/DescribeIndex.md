**Example 1: 获取索引信息**



Input: 

```
tccli cls DescribeIndex --cli-unfold-argument  \
    --TopicId 75f531f6-3644-45e5-8717-af1dc294cc93
```

Output: 
```
{
    "Response": {
        "TopicId": "75f531f6-3644-45e5-8717-af1dc294cc93",
        "Status": false,
        "Rule": {
            "FullText": {
                "CaseSensitive": true,
                "Tokenizer": "@&?|#()='\",;:<>[]{}/ \n\t\r\\",
                "ContainZH": false
            },
            "KeyValue": {
                "CaseSensitive": true,
                "KeyValues": [
                    {
                        "Key": "age",
                        "Value": {
                            "Type": "long",
                            "Tokenizer": "",
                            "SqlFlag": false,
                            "ContainZH": false,
                            "Alias": ""
                        }
                    }
                ]
            },
            "Tag": {
                "CaseSensitive": true,
                "KeyValues": [
                    {
                        "Key": "tag",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "@&?|#()='\",;:<>[]{}/ \n\t\r\\",
                            "SqlFlag": false,
                            "ContainZH": false,
                            "Alias": ""
                        }
                    }
                ]
            },
            "DynamicIndex": {
                "Status": false
            }
        },
        "ModifyTime": "2025-08-04 15:09:10",
        "RequestId": "9cdcca5e-9d2b-41c1-8b69-6de7034e70ee",
        "IncludeInternalFields": true,
        "MetadataFlag": 0
    }
}
```


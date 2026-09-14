**Example 1: 查询知识库详情**

查询知识库详情

Input: 

```
tccli adp DescribeKB --cli-unfold-argument  \
    --KbId 2097668735455299264
```

Output: 
```
{
    "Response": {
        "Summary": {
            "KbId": "2097668735455299264",
            "Name": "托管es共享",
            "Description": "",
            "KbType": 2,
            "SharedSubType": 0,
            "DocCount": 0,
            "IsExceeded": false,
            "CreateTime": "1788958174",
            "UpdateTime": "1788958174",
            "ProcessingFlagList": [],
            "AppList": [],
            "LatestOperator": null,
            "Creator": null
        },
        "ModelConfig": {
            "EmbeddingModel": "Youtu/youtu-embedding-llm",
            "QaExtractModel": "Deepseek/deepseek-v4-pro",
            "SchemaModel": "Deepseek/deepseek-v4-pro"
        },
        "EsConfig": {
            "StorageType": 2,
            "InstanceId": "es-jirwzied",
            "UserName": "elastic",
            "EncryptedPassword": "",
            "CanModify": true
        },
        "CapacityInfo": {
            "MaxCharSize": "0",
            "UsedCharSize": "0",
            "OverCharSize": "0"
        },
        "Owner": {
            "UserId": "14337",
            "UserName": ""
        },
        "AppIdList": [],
        "RequestId": "b90eb2fd-e8ff-44dc-aa88-4f33c933ded6"
    }
}
```


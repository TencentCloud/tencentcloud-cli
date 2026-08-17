**Example 1: 创建模型**



Input: 

```
tccli dlc CreateInferenceModel --cli-unfold-argument  \
    --Name dasdas \
    --ModelType LLM \
    --InitialVersion v1 \
    --StorageType Local
```

Output: 
```
{
    "Response": {
        "AppId": 260200066,
        "BuiltIn": false,
        "CreateTime": 1786691307765,
        "HasCustomStorage": false,
        "HasStorage": true,
        "LatestVersion": "v1",
        "ModelId": "122",
        "ModelType": "LLM",
        "ModelUid": "m-dasdas-6a7ebeeb-f470",
        "Name": "dasdas",
        "Provider": "personal",
        "ResourceTags": [],
        "ServiceCount": 0,
        "StorageType": "COS",
        "SubAccountUin": "700002655694",
        "Tags": [],
        "Tasks": [],
        "UpdateTime": 1786691307765,
        "VersionCount": 1,
        "RequestId": "1d27fdf0-35b5-49dc-869e-0b7c99c36730"
    }
}
```


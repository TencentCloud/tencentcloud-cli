**Example 1: 获取模型 readme 信息**



Input: 

```
tccli dlc GetModelReadme --cli-unfold-argument  \
    --ModelUid m-xgboost-6a159272-99b2 \
    --ModelVersion v1
```

Output: 
```
{
    "Response": {
        "BuiltIn": false,
        "ModelName": "xgboost",
        "ModelType": "ML",
        "ParameterSize": "0.1",
        "Provider": "个人",
        "Readme": "",
        "RequestId": "fc0fbf7c-67d4-46c6-8b01-955bb16f889f"
    }
}
```


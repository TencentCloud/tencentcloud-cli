**Example 1: 示例**



Input: 

```
tccli dlc CreateInferenceModel --cli-unfold-argument  \
    --Name capi_test_123 \
    --ModelType ML \
    --InitialVersion v1 \
    --Provider personal \
    --Description description \
    --ParameterSize 1 \
    --Tags thisistag \
    --StorageUri storageUri \
    --UseCustomStorage True \
    --Tasks thisistask \
    --ModelUid thisismodelUid12345
```

Output: 
```
{
    "Response": {
        "AppId": 260200066,
        "BuiltIn": false,
        "CreateTime": 1781579668983,
        "Description": "description",
        "HasCustomStorage": true,
        "HasStorage": true,
        "LatestVersion": "v1",
        "ModelId": "60",
        "ModelType": "ML",
        "ModelUid": "thisismodelUid12345",
        "Name": "capi_test_123",
        "ParameterSize": "1",
        "Provider": "personal",
        "ServiceCount": 0,
        "StorageType": "COS",
        "SubAccountUin": "700002655694",
        "Tags": [
            "thisistag"
        ],
        "Tasks": [
            "thisistask"
        ],
        "UpdateTime": 1781579668983,
        "VersionCount": 1,
        "RequestId": "48031f8c-c648-4cfb-8237-d9d219149211"
    }
}
```


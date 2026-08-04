**Example 1: 示例**



Input: 

```
tccli dlc UpdateInferenceModel --cli-unfold-argument  \
    --ModelUid m-capi-test-6a30b76e-aa04 \
    --Name capi_test \
    --Description Description \
    --ParameterSize 1 \
    --Tags tagnew
```

Output: 
```
{
    "Response": {
        "AppId": 260200066,
        "BuiltIn": false,
        "CreateTime": 1781577582219,
        "Description": "Description",
        "HasCustomStorage": false,
        "HasStorage": true,
        "LatestVersion": "v1",
        "ModelId": "51",
        "ModelType": "ml",
        "ModelUid": "m-capi-test-6a30b76e-aa04",
        "Name": "capi_test",
        "ParameterSize": "1",
        "Provider": "personal",
        "ServiceCount": 0,
        "StorageType": "COS",
        "SubAccountUin": "700002655694",
        "Tags": [
            "tagnew"
        ],
        "Tasks": [
            "thisistask"
        ],
        "UpdateTime": 1781578511252,
        "VersionCount": 1,
        "RequestId": "4c7528af-fe6f-416d-b452-5b2921eea309"
    }
}
```


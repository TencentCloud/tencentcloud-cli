**Example 1: 创建模型新版本**



Input: 

```
tccli dlc CreateModelVersion --cli-unfold-argument  \
    --ModelUid m-xgboost-mao-6a2fc583-14cb \
    --ModelVersion v4 \
    --Description test model, 7B \
    --StorageUri cos://common-job-packages-251233710/models/ \
    --UseCustomStorage False
```

Output: 
```
{
    "Response": {
        "CreateTime": 1781516236155,
        "Description": "test model, 7B",
        "LinkedServices": [],
        "ModelId": "45",
        "StorageUri": "cos://common-job-packages-251233710/models/",
        "UpdateTime": 1781516236155,
        "Version": "v4",
        "VersionId": "65",
        "RequestId": "4925e7a8-b27a-4d81-8a63-e182b6cc6e0d"
    }
}
```


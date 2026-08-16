**Example 1: 创建模型版本**



Input: 

```
tccli dlc CreateModelVersion --cli-unfold-argument  \
    --ModelUid m-self-defined-model-6a79ed1a-f6f6 \
    --ModelVersion v6 \
    --StorageType Local
```

Output: 
```
{
    "Response": {
        "CreateTime": 1786690586382,
        "LinkedServices": [],
        "ModelId": "112",
        "StorageUri": "cos://common-job-packages-251233710/models/m-self-defined-model-6a79ed1a-f6f6/v6/",
        "UpdateTime": 1786690586382,
        "UseCustomStorage": false,
        "Version": "v6",
        "VersionId": "155",
        "RequestId": "e3ba2d9c-a2f2-4704-9297-33bef8430c80"
    }
}
```


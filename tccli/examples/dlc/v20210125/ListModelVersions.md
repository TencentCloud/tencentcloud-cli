**Example 1: 列出模型所有版本**



Input: 

```
tccli dlc ListModelVersions --cli-unfold-argument  \
    --ModelUid m-xgb-test-tangbo-6a2d680b-67ac
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateTime": 1781360717376,
                "Description": "",
                "LinkedServices": [],
                "ModelId": "39",
                "StorageUri": "common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/models/m-xgb-test-tangbo-6a2d680b-67ac/v3/model.json",
                "UpdateTime": 1781360717376,
                "Version": "v3",
                "VersionId": "55"
            }
        ],
        "Page": 1,
        "PageSize": 200,
        "Total": 3,
        "TotalPages": 1,
        "RequestId": "ff2a106c-6da3-4ba0-be07-dd59ab7f927a"
    }
}
```


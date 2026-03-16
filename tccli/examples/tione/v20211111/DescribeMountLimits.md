**Example 1: 成功示例**



Input: 

```
tccli tione DescribeMountLimits --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "MountLimits": [
            {
                "CreateTime": "2025-07-02T20:10:37Z",
                "Creator": "100038630886",
                "CreatorName": "zhangsan",
                "ExtraConf": {
                    "CFSProtocol": "NFS",
                    "CFSStorageType": "SD"
                },
                "LimitMount": true,
                "StorageId": "cfs-ndqrxskx",
                "StorageName": "test_cfs",
                "Type": "Cfs",
                "UpdateTime": "2025-07-02T20:10:37Z"
            }
        ],
        "RequestId": "cee4fb9b-f0c4-4ed7-b865-2d9d71ddbaaa",
        "TotalCount": 1
    }
}
```


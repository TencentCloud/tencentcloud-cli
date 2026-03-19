**Example 1: 成功示例**



Input: 

```
tccli tione DescribeDataSource --cli-unfold-argument  \
    --Id dsrc-Cfs-abum82k1s7wg
```

Output: 
```
{
    "Response": {
        "DataSourceInfo": {
            "CreateTime": "2025-07-08T19:31:47Z",
            "Creator": "100038630886",
            "CreatorName": "breezeliu",
            "ExtraConf": {
                "CFSProtocol": "NFS",
                "CFSStorageType": "SD"
            },
            "Id": "dsrc-Cfs-abum82k1s7wg",
            "LimitMount": true,
            "MountConfigure": {
                "WorkDir": "/abc"
            },
            "Name": "测试数据源",
            "Permission": "RW",
            "StorageId": "cfs-ndqrxskx",
            "StorageName": "shizhuhuang_cfs",
            "Tags": [
                {
                    "TagKey": "key1",
                    "TagValue": "value2"
                },
                {
                    "TagKey": "qcs:tag:createdBy",
                    "TagValue": "CAMUser:100038630886:breezeliu"
                }
            ],
            "Type": "Cfs",
            "UpdateTime": "2025-07-08T19:31:47Z"
        },
        "RequestId": "78188a2e-c160-4696-b066-0f0799e2ed2f"
    }
}
```


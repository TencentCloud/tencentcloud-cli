**Example 1: 成功示例**



Input: 

```
tccli tione DescribeDataSources --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DataSourceInfos": [
            {
                "CreateTime": "2025-07-08 19:31:47",
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
                "UpdateTime": "2025-07-08 19:31:47"
            }
        ],
        "RequestId": "98f3068f-279d-4b70-8dd3-2189b0d3c7c6",
        "TotalCount": 1
    }
}
```


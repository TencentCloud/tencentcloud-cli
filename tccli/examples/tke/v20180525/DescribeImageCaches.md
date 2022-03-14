**Example 1: 查询镜像缓存信息**



Input: 

```
tccli tke DescribeImageCaches --cli-unfold-argument  \
    --ImageCacheIds imc-xxx \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "6704dc99-e331-4055-8af9-123456789",
        "TotalCount": 1,
        "ImageCaches": [
            {
                "ImageCacheId": "imc-xxx",
                "ImageCacheName": "imc-nginx",
                "ImageCacheSize": 20,
                "Status": "Ready",
                "Images": [
                    "nginx"
                ],
                "CreationTime": "2021-12-06 22:52:24",
                "ExpireDateTime": "",
                "Events": [
                    {
                        "ImageCacheId": "imc-xxx",
                        "Reason": "SnapCreated",
                        "Type": "Normal",
                        "FirstTimestamp": "2021-12-06 15:10:43",
                        "LastTimestamp": "2021-12-06 15:10:43",
                        "Message": "Snap snap-xxx created"
                    },
                    {
                        "ImageCacheId": "imc-xxx",
                        "Reason": "DiskCreated",
                        "Type": "Normal",
                        "FirstTimestamp": "2021-12-06 15:03:24",
                        "LastTimestamp": "2021-12-06 15:03:24",
                        "Message": "Disk disk-xxx created"
                    },
                    {
                        "ImageCacheId": "imc-xxx",
                        "Reason": "EksciCreated",
                        "Type": "Normal",
                        "FirstTimestamp": "2021-12-06 15:03:24",
                        "LastTimestamp": "2021-12-06 15:03:24",
                        "Message": "Eksci eksci-xxx created"
                    }
                ],
                "LastMatchedTime": "2021-12-07 21:30:15",
                "SnapshotId": "snap-xxx"
            }
        ]
    }
}
```


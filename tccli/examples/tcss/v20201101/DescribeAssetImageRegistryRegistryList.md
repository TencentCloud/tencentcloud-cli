**Example 1: 镜像仓库查询镜像仓库列表**



Input: 

```
tccli tcss DescribeAssetImageRegistryRegistryList --cli-unfold-argument  \
    --Limit 100 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "e59f97b7-87d4-4909-8289-61bd28423d2f",
        "TotalCount": 15525,
        "List": [
            {
                "ConnDetectDetail": [
                    {
                        "ConnDetectMessage": "",
                        "ConnDetectStatus": "status_connected",
                        "FailReason": "",
                        "Quuid": "backend",
                        "Solution": "",
                        "Uuid": "backend"
                    }
                ],
                "ConnDetectHostCount": 1,
                "ConnDetectType": "backend",
                "ConnectMsg": "",
                "InstanceID": "",
                "LatestSyncTime": "2024-10-23 03:12:50",
                "Name": "aws_public",
                "NetType": "public",
                "RegistryId": 10000,
                "RegistryRegion": "default",
                "RegistryType": "aws",
                "RegistryVersion": "V1",
                "SyncFailReason": "",
                "SyncMessage": "",
                "SyncSolution": "",
                "SyncStatus": "success",
                "Url": "https://public.aws"
            }
        ]
    }
}
```


**Example 1: 查询快照信息接口**



Input: 

```
tccli es DescribeUserCosSnapshotList --cli-unfold-argument  \
    --CosBucket xxx \
    --BasePath xxx \
    --ClusterInstanceId xxx
```

Output: 
```
{
    "Response": {
        "CosSnapshotInfoList": [
            {
                "CosBucket": "xxx",
                "BasePath": "xxx",
                "SnapshotName": "xxx",
                "State": "xxx",
                "Version": "xxx",
                "CommonIndexArr": [
                    {
                        "IndexName": "abc",
                        "IsShardComplete": 0
                    }
                ],
                "DataStreamArr": [
                    {
                        "DataStreamName": "xxx",
                        "IsShardComplete": 0
                    }
                ]
            }
        ],
        "TotalCount": 10,
        "RequestId": "xxx"
    }
}
```


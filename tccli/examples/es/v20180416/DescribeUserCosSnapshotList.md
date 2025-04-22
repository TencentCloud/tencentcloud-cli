**Example 1: 查询快照信息接口**



Input: 

```
tccli es DescribeUserCosSnapshotList --cli-unfold-argument  \
    --CosBucket user-cos \
    --BasePath dir/ \
    --ClusterInstanceId es-feaffea
```

Output: 
```
{
    "Response": {
        "CosSnapshotInfoList": [
            {
                "CosBucket": "user-cos",
                "BasePath": "dir/",
                "SnapshotName": "testSnapshot",
                "State": "SUCCESS",
                "Version": "7.14.2",
                "CommonIndexArr": [
                    {
                        "IndexName": "testindex",
                        "IsShardComplete": 0
                    }
                ],
                "DataStreamArr": [
                    {
                        "DataStreamName": "index",
                        "IsShardComplete": 0
                    }
                ]
            }
        ],
        "TotalCount": 10,
        "RequestId": "iuhifaeui-feaihfhfa-feaijni-fieai"
    }
}
```


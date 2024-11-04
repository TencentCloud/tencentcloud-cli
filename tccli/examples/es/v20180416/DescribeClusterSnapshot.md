**Example 1: DescribeClusterSnapshot 查询快照列表**



Input: 

```
tccli es DescribeClusterSnapshot --cli-unfold-argument  \
    --InstanceId es-f1m2enyd \
    --RepositoryName ES_AUTO_BACKUP \
    --SnapshotName abc
```

Output: 
```
{
    "Response": {
        "RequestId": "50df75f7-ec95-4c32-b7b0-a8e98ae74fef11",
        "RepositoryName": "ES_AUTO_BACKUP",
        "InstanceId": "es-f1m2enyd",
        "Snapshots": [
            {
                "SnapshotName": "快照名称1",
                "Uuid": "OPoARqBBSKuEIdLPdp7_dA",
                "Version": "7.14.2",
                "Indices": [
                    "honorboardcloud-sit-logs",
                    "pushtoken_meta_info_v1_auto",
                    ".ds-logs-generic-default-2023.10.11-000002"
                ],
                "State": "SUCCESS",
                "StartTime": "2023-10-30T18:00:45.746Z",
                "EndTime": "2023-10-30T18:14:46.707Z",
                "DurationInMillis": 840961,
                "TotalShards": 316,
                "FailedShards": 0,
                "SuccessfulShards": 316,
                "Failures": [
                    {
                        "Index": "快照备份失败的索引名称",
                        "ShardId": 0,
                        "Reason": "快照失败的原因"
                    },
                    {
                        "Index": "快照备份失败的索引名称",
                        "ShardId": 0,
                        "Reason": "快照失败的原因"
                    }
                ]
            },
            {
                "SnapshotName": "快照名称1",
                "Uuid": "OPoARqBBSKuEIdLPdp7_dA",
                "Version": "7.14.2",
                "Indices": [
                    "honorboardcloud-sit-logs",
                    "pushtoken_meta_info_v1_auto",
                    ".ds-logs-generic-default-2023.10.11-000002"
                ],
                "State": "SUCCESS",
                "StartTime": "2023-10-30T18:00:45.746Z",
                "EndTime": "2023-10-30T18:14:46.707Z",
                "DurationInMillis": 840961,
                "TotalShards": 316,
                "FailedShards": 0,
                "SuccessfulShards": 316,
                "Failures": [
                    {
                        "Index": "快照备份失败的索引名称",
                        "ShardId": 0,
                        "Reason": "快照失败的原因"
                    },
                    {
                        "Index": "快照备份失败的索引名称",
                        "ShardId": 0,
                        "Reason": "快照失败的原因"
                    }
                ]
            }
        ]
    }
}
```


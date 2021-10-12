**Example 1: 查询从实例同步状态**



Input: 

```
tccli tcr DescribeReplicationInstanceSyncStatus --cli-unfold-argument  \
    --RegistryId tcr-12345 \
    --ReplicationRegistryId tcr-12345-5 \
    --ShowReplicationLog true \
    --Offset 1 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "ReplicationStatus": "Succeed",
        "ReplicationTime": "2021-09-28T08:00:15Z",
        "RequestId": "88b91f6a-2fbe-4d5d-9b2e-a9a4a273758d",
        "ReplicationLog": [
            {
                "ResourceType": "image",
                "Source": "test/test:[1]",
                "Destination": "test/test:[1]",
                "Status": "Succeed",
                "StartTime": "2021-09-28T07:47:44.302804Z",
                "EndTime": "2021-09-28T07:47:53Z"
            }
        ]
    }
}
```


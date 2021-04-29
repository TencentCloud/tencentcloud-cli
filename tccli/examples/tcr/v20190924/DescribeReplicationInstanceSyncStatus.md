**Example 1: 查询从实例同步状态**



Input: 

```
tccli tcr DescribeReplicationInstanceSyncStatus --cli-unfold-argument  \
    --RegistryId tcr-12345 \
    --ReplicationRegistryId tcr-12345-5 \
    --ReplicationRegionId 5
```

Output: 
```
{
    "Response": {
        "ReplicationStatus": "StatusUnKnow",
        "ReplicationTime": "0001-01-01T00:00:00Z",
        "RequestId": "4cc6f30c-0862-47d0-8d89-1b7a372b936b"
    }
}
```


**Example 1: 查询实例同步/实例复制任务列表**



Input: 

```
tccli tcr DescribeReplicationTasks --cli-unfold-argument  \
    --RegistryId tcr-xxx \
    --ExecutionId 10 \
    --Page 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ReplicationTaskList": [
            {
                "ResourceType": "image",
                "SrcResource": "test/test:[1g]",
                "DstResource": "test/test:[1g]",
                "JobID": "747c6571c2de465587690929",
                "Status": "Succeed",
                "StartTime": "2023-07-14T03:42:09.95279Z",
                "EndTime": "2023-07-14T03:42:17Z"
            }
        ],
        "RequestId": "xxx"
    }
}
```


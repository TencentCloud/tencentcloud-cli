**Example 1: 查询实例同步/实例复制执行记录列表**



Input: 

```
tccli tcr DescribeReplicationExecutions --cli-unfold-argument  \
    --RegistryId tcr-xxx \
    --PolicyId 1 \
    --ReplicationInstanceId tcr-xxx-1-xxx \
    --Page 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ReplicationExecutionList": [
            {
                "ExecutionID": "10",
                "PolicyID": "19",
                "Status": "succeed",
                "Total": "3",
                "Succeed": "3",
                "StartTime": "2023-08-01T12:00:00+00:00",
                "EndTime": "2023-08-01T12:00:01+00:00"
            }
        ],
        "RequestId": "abc"
    }
}
```


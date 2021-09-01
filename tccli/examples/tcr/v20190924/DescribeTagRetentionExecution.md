**Example 1: 查询版本保留执行记录**



Input: 

```
tccli tcr DescribeTagRetentionExecution --cli-unfold-argument  \
    --RegistryId tcr-12345 \
    --RetentionId 1 \
    --Limit 20 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "RequestId": "023eef7f-cf03-4e4a-b7bb-de7d66aa6fbc",
        "RetentionExecutionList": [
            {
                "ExecutionId": 1,
                "RetentionId": 1,
                "StartTime": "2021-04-12T10:49:20Z",
                "EndTime": "2021-04-12T10:49:20Z",
                "Status": "Succeed"
            }
        ],
        "TotalCount": 1
    }
}
```


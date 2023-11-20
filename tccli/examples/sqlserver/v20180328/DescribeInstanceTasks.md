**Example 1: 查询异步任务列表**



Input: 

```
tccli sqlserver DescribeInstanceTasks --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl \
    --Status 2 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "InstanceTaskSet": [
            {
                "EndTime": "2019-08-15 14:26:22",
                "ErrorCode": 0,
                "Id": 23517,
                "Message": "",
                "Progress": 100,
                "StartTime": "2019-08-15 14:25:20",
                "Status": 2,
                "Type": 62
            }
        ],
        "RequestId": "c736ff8a-5e23-4549-b9fb-6d79d11586ac",
        "TotalCount": 21
    }
}
```


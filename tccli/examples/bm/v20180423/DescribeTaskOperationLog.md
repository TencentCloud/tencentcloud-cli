**Example 1: 获取维修任务操作日志**



Input: 

```
tccli bm DescribeTaskOperationLog --cli-unfold-argument  \
    --TaskId bmj-test \
    --OrderField OperationTime \
    --Order 0
```

Output: 
```
{
    "Response": {
        "RequestId": "a2a13989-5776-4a8b-83d6-43714117ac3c",
        "TotalCount": 2,
        "TaskOperationLogSet": [
            {
                "TaskStep": "故障建单",
                "Operator": "腾讯云",
                "OperationDetail": "发生故障，系统建单",
                "OperationTime": "2018-04-15 17:10:25"
            },
            {
                "TaskStep": "未授权-暂不处理",
                "Operator": "123456",
                "OperationDetail": "用户已收到通知，稍后处理",
                "OperationTime": "2018-04-15 17:50:02"
            }
        ]
    }
}
```


**Example 1: 集群任务信息**



Input: 

```
tccli goosefs ListMountPointClusterTasks --cli-unfold-argument  \
    --ClusterId clst-1vURpywj \
    --Offset 0 \
    --Limit 20 \
    --StartTimestamp 1782875372 \
    --EndTimestamp 1784603399
```

Output: 
```
{
    "Response": {
        "Tasks": [
            {
                "Content": "",
                "CreateTime": 1784196744,
                "EndTime": 1784196744,
                "Status": "FAILED",
                "TaskId": "K1rzyihaW5pg",
                "TaskMessage": "",
                "TaskName": "保活失败"
            }
        ],
        "TotalCount": 120572,
        "RequestId": "b797efee-57e8-440c-8e8e-3e3da08ef09d"
    }
}
```


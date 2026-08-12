**Example 1: 查询任务信息**



Input: 

```
tccli goosefs DescribeMountPointClusterTask --cli-unfold-argument  \
    --ClusterId clst-1vURpywj \
    --TaskId 0006ev4bX0iq
```

Output: 
```
{
    "Response": {
        "Content": "{\"retry_time\":1782843960}",
        "CreateTime": 1782843960,
        "EndTime": 1782843962,
        "Message": "保活重启成功",
        "Status": "SUCCESS",
        "SubTasks": [],
        "TaskId": "0006ev4bX0iq",
        "TaskName": "保活自动重启",
        "RequestId": "447fc85b-f827-4be2-ba73-ed96368eb76b"
    }
}
```


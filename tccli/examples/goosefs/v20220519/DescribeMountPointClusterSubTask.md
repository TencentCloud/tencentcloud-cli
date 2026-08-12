**Example 1: 查询子任务的具体信息**



Input: 

```
tccli goosefs DescribeMountPointClusterSubTask --cli-unfold-argument  \
    --ClusterId clst-1vURpywj \
    --TaskId K1rzyihaW5pg \
    --SubTaskId 1
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "CreateTime": 1784196744,
                "EndTime": 1784196744,
                "EntityId": "mpc-yz9572iP",
                "Message": "keepalive failed",
                "NodeId": "ins-otbj03yi",
                "NodeIp": "10.0.0.4",
                "Status": "FAILED",
                "SubTaskId": 1,
                "TaskId": "K1rzyihaW5pg"
            }
        ],
        "ExistDetail": true,
        "Message": "keepalive failed",
        "Status": "FAILED",
        "SubTaskId": 1,
        "SubTaskName": "保活超限处理",
        "TaskId": "K1rzyihaW5pg",
        "TotalDetails": 1,
        "RequestId": "79228f07-a330-424f-a973-8338a20311f4"
    }
}
```


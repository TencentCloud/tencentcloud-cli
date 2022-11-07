**Example 1: 查询实时任务实例节点信息**

查询实时任务实例节点信息

Input: 

```
tccli wedata DescribeRealTimeTaskInstanceNodeInfo --cli-unfold-argument  \
    --ProjectId xx \
    --TaskId xx
```

Output: 
```
{
    "Response": {
        "RealTimeTaskInstanceNodeInfo": {
            "InstanceNodeInfoList": [
                {
                    "NodeType": "SOURCE",
                    "NodeId": "xx",
                    "NodeName": "xx"
                }
            ],
            "TaskName": "xx",
            "TaskId": "xx"
        },
        "RequestId": "xx"
    }
}
```


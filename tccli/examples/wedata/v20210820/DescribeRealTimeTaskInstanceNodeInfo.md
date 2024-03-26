**Example 1: 查询实时任务实例节点信息**

查询实时任务实例节点信息

Input: 

```
tccli wedata DescribeRealTimeTaskInstanceNodeInfo --cli-unfold-argument  \
    --TaskId abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "RealTimeTaskInstanceNodeInfo": {
            "TaskName": "abc",
            "TaskId": "abc",
            "InstanceNodeInfoList": [
                {
                    "NodeType": "abc",
                    "NodeId": "abc",
                    "NodeName": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```


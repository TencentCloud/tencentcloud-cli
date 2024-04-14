**Example 1: 查询实时任务实例节点信息**

查询实时任务实例节点信息

Input: 

```
tccli wedata DescribeRealTimeTaskInstanceNodeInfo --cli-unfold-argument  \
    --TaskId 20220506145218687 \
    --ProjectId 11022568003970304
```

Output: 
```
{
    "Response": {
        "RealTimeTaskInstanceNodeInfo": {
            "TaskName": "task1",
            "TaskId": "1",
            "InstanceNodeInfoList": [
                {
                    "NodeType": "INPUT",
                    "NodeId": "3039",
                    "NodeName": "1"
                }
            ]
        },
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```


**Example 1: 查询云数据库实例的当前操作**

查询云数据库实例的当前操作

Input: 

```
tccli mongodb DescribeCurrentOp --cli-unfold-argument  \
    --InstanceId cmgo-p8vn****
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "CurrentOps": [
            {
                "OpId": 1804858933,
                "Ns": "db.****",
                "Query": "",
                "Op": "command",
                "ReplicaSetName": "salve-1",
                "NodeName": "salve-1",
                "Operation": "****",
                "State": "Primary",
                "MicrosecsRunning": 30353723,
                "ExecNode": "从节点"
            }
        ],
        "RequestId": "66956cf3-2d10-4c68-87c0-7bd558deae7e"
    }
}
```


**Example 1: 查询云数据库实例的当前操作**



Input: 

```
tccli mongodb DescribeCurrentOp --cli-unfold-argument  \
    --InstanceId cmgo-p8vnipr5
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "CurrentOps": [
            {
                "ReplicaSetName": "xx",
                "NodeName": "xx",
                "State": "xx",
                "MicrosecsRunning": 1,
                "Query": "xx",
                "OpId": 0,
                "Ns": "xx",
                "Operation": "xx",
                "Op": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```


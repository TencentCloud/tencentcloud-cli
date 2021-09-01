**Example 1: 终止数据库实例特定操作**



Input: 

```
tccli mongodb KillOps --cli-unfold-argument  \
    --InstanceId cmgo-p8vnipr5 \
    --Operations.0.ReplicaSetName cmgo-p8vnipr5_0 \
    --Operations.0.NodeName 10.108.93.135:7017:39920912 \
    --Operations.0.OpId 61
```

Output: 
```
{
    "Response": {
        "RequestId": "302530d2-ee57-495e-89d0-51e03b11815e"
    }
}
```


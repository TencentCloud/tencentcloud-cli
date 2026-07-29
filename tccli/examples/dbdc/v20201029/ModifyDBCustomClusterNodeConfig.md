**Example 1: 修改集群中节点的配置信息接口**

本接口（ModifyDBCustomClusterNodeConfig） 用于修改 DB Custom 集群节点的标签与污点配置

Input: 

```
tccli dbdc ModifyDBCustomClusterNodeConfig --cli-unfold-argument  \
    --ClusterId dbcc-sizxd0hi \
    --NodeIds dbcn-yfw66wu9 \
    --UpsertTaints.0.Key A.B \
    --UpsertTaints.0.Effect PreferNoSchedule
```

Output: 
```
{
    "Response": {
        "TaskId": 1499,
        "RequestId": "7fff902d-87dd-4109-94b0-7029c15e33a7"
    }
}
```


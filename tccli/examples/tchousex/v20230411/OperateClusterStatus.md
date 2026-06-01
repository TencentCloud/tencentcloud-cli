**Example 1: 参数示例**



Input: 

```
tccli tchousex OperateClusterStatus --cli-unfold-argument  \
    --ManualOperateClusterMeta.InstanceId test \
    --ManualOperateClusterMeta.VirtualCluster test \
    --ManualOperateClusterMeta.Component test \
    --ManualOperateClusterMeta.Start True
```

Output: 
```
{
    "Response": {
        "FlowId": 0,
        "ErrorMsg": "test",
        "RequestId": "test"
    }
}
```


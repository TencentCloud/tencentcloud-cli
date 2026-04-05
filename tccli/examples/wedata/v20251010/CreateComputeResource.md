**Example 1: 创建计算资源**



Input: 

```
tccli wedata CreateComputeResource --cli-unfold-argument  \
    --WorkspaceId 12 \
    --ResourceName mock \
    --Description mock \
    --ResourceType 1 \
    --BillType postpaid \
    --Config.MinCU None \
    --Config.MaxCU None \
    --Config.AutoStartStop None \
    --Config.AutoStopSeconds None \
    --Config.MaxInstances None \
    --Config.SingleInstanceQuota None \
    --Config.MaxConcurrency None \
    --CreateType None
```

Output: 
```
{
    "Response": {
        "Data": {
            "ResourceId": "mock"
        },
        "RequestId": "d28b4aa5-262a-4fb3-87d8-87c036b6341a"
    }
}
```


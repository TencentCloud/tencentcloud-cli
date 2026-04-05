**Example 1: 更新计算资源**

更新计算资源只更新名称

Input: 

```
tccli wedata UpdateComputeResource --cli-unfold-argument  \
    --WorkspaceId 12 \
    --ResourceId mock \
    --ResourceName mock \
    --Description None \
    --Config.MinCU None \
    --Config.MaxCU None \
    --Config.AutoStartStop None \
    --Config.AutoStopSeconds None \
    --Config.MaxInstances None \
    --Config.SingleInstanceQuota None \
    --Config.MaxConcurrency None
```

Output: 
```
{
    "Response": {
        "Data": {},
        "RequestId": "a5287a15-f4b7-4ed4-a5bc-83710f59a791"
    }
}
```


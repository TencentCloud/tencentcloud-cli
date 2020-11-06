**Example 1: 批量解绑后端服务**



Input: 

```
tccli ecm BatchDeregisterTargets --cli-unfold-argument  \
    --LoadBalancerId lb-xxxx \
    --Targets.0.ListenerId lbl-xxxx \
    --Targets.0.InstanceId ein-xxx \
    --Targets.0.Port 80 \
    --Targets.0.Weight 10
```

Output: 
```
{
    "Response": {
        "FailListenerIdSet": [],
        "RequestId": "83129908-a282-4f9f-8ab-131a3025ba22"
    }
}
```


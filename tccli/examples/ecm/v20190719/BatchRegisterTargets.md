**Example 1: 批量绑定后端目标**



Input: 

```
tccli ecm BatchRegisterTargets --cli-unfold-argument  \
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
        "FailListenerIdSet": [
            "xx"
        ],
        "RequestId": "a2764f3c-f173-421c-8e42-7b1e7a608a33"
    }
}
```


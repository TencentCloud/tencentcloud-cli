**Example 1: 绑定云主机或弹性网卡**



Input: 

```
tccli clb BatchRegisterTargets --cli-unfold-argument  \
    --Targets.0.InstanceId ins-xxx \
    --Targets.0.ListenerId lbl-xxxx \
    --Targets.0.Weight 10 \
    --Targets.0.Port 80 \
    --LoadBalancerId lb-xxxx
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


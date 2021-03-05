**Example 1: 从监听器的绑定列表中解绑一个云服务器**



Input: 

```
tccli clb DeregisterTargets --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0 \
    --ListenerId lbl-d1ubsydq \
    --Targets.0.InstanceId ins-dm4xtz0i \
    --Targets.0.Port 334
```

Output: 
```
{
    "Response": {
        "RequestId": "4d1df727-d61c-45bf-936b-cb0368fb2a7d"
    }
}
```


**Example 1: 修改监听器绑定的后端机器的端口**



Input: 

```
tccli ecm ModifyTargetPort --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0 \
    --ListenerId lbl-d1ubsydq \
    --Targets.0.InstanceId ein-dm4xtz0i \
    --Targets.0.Port 233 \
    --NewPort 334
```

Output: 
```
{
    "Response": {
        "RequestId": "a2764f3c-f173-421c-8e42-7b1e7a608ffd"
    }
}
```


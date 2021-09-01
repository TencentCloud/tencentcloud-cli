**Example 1: 修改绑定的后端服务的端口**

将绑定到监听器lbl-d1ubsydq的云服务器ins-dm4xtz0i的端口从原来的233改为334

Input: 

```
tccli clb ModifyTargetPort --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0 \
    --ListenerId lbl-d1ubsydq \
    --Targets.0.InstanceId ins-dm4xtz0i \
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


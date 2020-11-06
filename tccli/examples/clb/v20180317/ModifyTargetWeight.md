**Example 1: 修改四层监听器上绑定的后端服务的权重**

将绑定到监听器lbl-d1ubsydq的后端服务ins-dm4xtz0i（绑定端口为334）的权重修改为8

Input: 

```
tccli clb ModifyTargetWeight --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0 \
    --ListenerId lbl-d1ubsydq \
    --Targets.0.InstanceId ins-dm4xtz0i \
    --Targets.0.Port 334 \
    --Weight 8
```

Output: 
```
{
    "Response": {
        "RequestId": "85c7b3e8-7fd8-4c62-8b3b-7ba52d7a1dca"
    }
}
```


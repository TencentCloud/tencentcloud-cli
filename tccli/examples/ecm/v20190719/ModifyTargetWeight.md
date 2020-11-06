**Example 1: 修改监听器绑定的后端机器的转发权重**



Input: 

```
tccli ecm ModifyTargetWeight --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0 \
    --ListenerId lbl-d1ubsydq \
    --Targets.0.InstanceId ein-dm4xtz0i \
    --Targets.0.Port 334 \
    --Weight 8
```

Output: 
```
{
    "Response": {
        "RequestId": "a2764f3c-f173-421c-8e42-7b1e7a608a12"
    }
}
```


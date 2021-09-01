**Example 1: 批量修改监听器绑定的后端机器的转发权重**



Input: 

```
tccli ecm BatchModifyTargetWeight --cli-unfold-argument  \
    --LoadBalancerId lb-dx98lwo0 \
    --ModifyList.0.ListenerId lbl-4b5hnc9a \
    --ModifyList.0.Targets.0.InstanceId ein-19404pl5 \
    --ModifyList.0.Targets.0.Port 110 \
    --ModifyList.0.Targets.0.Weight 50 \
    --ModifyList.1.ListenerId lbl-20jjtaaw \
    --ModifyList.1.Targets.0.InstanceId ein-19411tzv \
    --ModifyList.1.Targets.0.Port 80 \
    --ModifyList.1.Targets.0.Weight 30
```

Output: 
```
{
    "Response": {
        "RequestId": "83329908-a282-4f9f-8ab-031a3025b377"
    }
}
```


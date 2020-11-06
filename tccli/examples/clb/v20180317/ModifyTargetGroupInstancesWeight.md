**Example 1: 批量修改目标组服务器权重**



Input: 

```
tccli clb ModifyTargetGroupInstancesWeight --cli-unfold-argument  \
    --TargetGroupId lbtg-815iz538 \
    --TargetGroupInstances.0.BindIP 172.16.0.34 \
    --TargetGroupInstances.0.Port 1234 \
    --TargetGroupInstances.0.Weight 55
```

Output: 
```
{
    "Response": {
        "RequestId": "ed90470e-eade-423f-aae6-264d814d0d65"
    }
}
```


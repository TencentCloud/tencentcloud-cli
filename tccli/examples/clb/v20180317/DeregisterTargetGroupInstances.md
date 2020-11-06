**Example 1: 从目标组中解绑服务器**



Input: 

```
tccli clb DeregisterTargetGroupInstances --cli-unfold-argument  \
    --TargetGroupId lbtg-815iz538 \
    --TargetGroupInstances.0.BindIP 172.16.0.34 \
    --TargetGroupInstances.0.Port 1234
```

Output: 
```
{
    "Response": {
        "RequestId": "4b4987ca-58d0-4bad-9ded-344fa4011bda"
    }
}
```


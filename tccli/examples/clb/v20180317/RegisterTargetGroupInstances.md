**Example 1: 添加服务器到目标组中**



Input: 

```
tccli clb RegisterTargetGroupInstances --cli-unfold-argument  \
    --TargetGroupId lbtg-815iz538 \
    --TargetGroupInstances.0.BindIP 172.16.0.34 \
    --TargetGroupInstances.0.Port 443 \
    --TargetGroupInstances.0.Weight 10
```

Output: 
```
{
    "Response": {
        "RequestId": "acf6c2b3-b18d-4d2e-91e4-4eacff16c07e"
    }
}
```


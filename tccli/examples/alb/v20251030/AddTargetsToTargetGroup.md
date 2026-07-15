**Example 1: 向目标组内添加后端服务**



Input: 

```
tccli alb AddTargetsToTargetGroup --cli-unfold-argument  \
    --TargetGroupId lbtg-0zrnc9qa \
    --Targets.0.Port 80 \
    --Targets.0.TargetIp 10.0.0.1 \
    --Targets.0.Weight 100
```

Output: 
```
{
    "Response": {
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```


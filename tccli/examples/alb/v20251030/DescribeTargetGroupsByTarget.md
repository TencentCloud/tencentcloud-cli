**Example 1: 根据后端服务查询绑定的目标组**



Input: 

```
tccli alb DescribeTargetGroupsByTarget --cli-unfold-argument  \
    --TargetId ins-x8q2m4pa
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```


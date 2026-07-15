**Example 1: 根据后端服务查询绑定的目标组**



Input: 

```
tccli alb DescribeTargetGroupsByTarget --cli-unfold-argument  \
    --MaxResults 10 \
    --TargetId ins-x8q2m4pa \
    --TargetIp.IpList 10.0.0.1 \
    --TargetIp.VpcId vpc-92hffaxb
```

Output: 
```
{
    "Response": {
        "NextToken": "",
        "TargetGroups": [
            {
                "TargetGroupId": "lbtg-0zrnc9qa",
                "TargetGroupName": "target-group-name",
                "CreateTime": "2025-01-01T08:30:00+08:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```


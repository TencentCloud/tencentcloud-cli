**Example 1: 查询目标组内后端服务**



Input: 

```
tccli alb DescribeTargetGroupTargets --cli-unfold-argument  \
    --MaxResults 20 \
    --TargetGroupId lbtg-0zrnc9qa
```

Output: 
```
{
    "Response": {
        "NextToken": "",
        "Targets": [
            {
                "TargetIp": "10.0.0.1",
                "Port": 80,
                "Weight": 10,
                "TargetStatus": "Active",
                "TargetType": "CVM",
                "TargetId": "ins-x8q2m4pa",
                "TargetName": "",
                "EniId": "eni-p4q7x2ma"
            }
        ],
        "TotalCount": 1,
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```


**Example 1: 查询伸缩组配置建议**



Input: 

```
tccli as DescribeAutoScalingAdvices --cli-unfold-argument  \
    --AutoScalingGroupIds asg-2pvrsyog
```

Output: 
```
{
    "Response": {
        "AutoScalingAdviceSet": [
            {
                "AutoScalingGroupId": "asg-2pvrsyog",
                "Advices": [
                    {
                        "Problem": "InvalidInstanceType",
                        "Solution": "It is recommended to replace the invalid instance type.",
                        "Detail": "Instance Type `S2.MEDIUM4`(`POSTPAID_BY_HOUR`) in `ap-guangzhou-1` is invalid."
                    },
                    {
                        "Problem": "InvalidInstanceType",
                        "Solution": "It is recommended to replace the invalid instance type.",
                        "Detail": "Instance Type `S2.MEDIUM4`(`POSTPAID_BY_HOUR`) in `ap-guangzhou-4` is invalid."
                    }
                ]
            }
        ],
        "RequestId": "5f7c48b7-222b-4f13-ae5e-978716b49f1c"
    }
}
```


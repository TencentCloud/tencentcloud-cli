**Example 1: 查询规则列表**



Input: 

```
tccli alb DescribeRules --cli-unfold-argument  \
    --LoadBalancerId alb-f8q2xk9m \
    --ListenerId lst-d9p3k7wa \
    --MaxResults 100
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "NextToken": "",
        "Rules": [
            {
                "RuleId": "rule-h8cy5gwl",
                "Priority": 1,
                "RuleName": "rule1",
                "Direction": "Request",
                "Conditions": [
                    {
                        "Type": "Host",
                        "HostConfig": [
                            "test.com"
                        ]
                    }
                ],
                "Actions": [
                    {
                        "Type": "TargetGroup",
                        "Order": 1,
                        "TargetGroupConfig": {
                            "TargetGroups": [
                                {
                                    "TargetGroupId": "lbtg-0zrnc9qa",
                                    "Weight": 10
                                }
                            ]
                        }
                    }
                ],
                "Status": "Active",
                "Tags": []
            }
        ],
        "RequestId": "ed300290-70cc-41f6-af02-50e151f91f90"
    }
}
```


**Example 1: 查看七层转发规则**



Input: 

```
tccli ga2 DescribeForwardingRule --cli-unfold-argument  \
    --GlobalAcceleratorId ga-r0aukpq8 \
    --ListenerId lsr-rk9g6p8x \
    --ForwardingPolicyId dm-9z3ue2yq
```

Output: 
```
{
    "Response": {
        "ForwardingRuleSet": [
            {
                "EnableOriginSni": false,
                "ForwardingPolicyId": "dm-9z3ue2yq",
                "ForwardingRuleId": "rule-bydbpo9y",
                "GlobalAcceleratorId": "ga-r0aukpq8",
                "ListenerId": "lsr-rk9g6p8x",
                "OriginHeaders": [],
                "OriginHost": "",
                "OriginSni": "",
                "RuleAction": [
                    {
                        "RuleActionType": "ForwardGroup",
                        "RuleActionValue": "epg-hru0z2dc"
                    }
                ],
                "RuleCondition": [
                    {
                        "RuleConditionType": "Path",
                        "RuleConditionValue": [
                            ""
                        ]
                    }
                ]
            }
        ],
        "RequestId": "c894e656-4f87-4d7d-a272-636c2de7633d",
        "TotalCount": 1
    }
}
```


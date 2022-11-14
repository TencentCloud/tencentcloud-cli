**Example 1: 查询规则组订阅信息**



Input: 

```
tccli wedata DescribeRuleGroupSubscription --cli-unfold-argument  \
    --ProjectId 1 \
    --RuleGroupId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Receivers": [
                {
                    "ReceiverName": "xx"
                }
            ],
            "SubscribeType": [
                1
            ],
            "RuleGroupId": 1
        },
        "RequestId": "xx"
    }
}
```


**Example 1: 查询规则组订阅信息**

查询规则组订阅详情

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
            "RuleGroupId": 1,
            "Receivers": [
                {
                    "ReceiverUserId": 1,
                    "ReceiverName": "zhangsan"
                }
            ],
            "SubscribeType": [
                1
            ],
            "WebHooks": [
                {
                    "HookType": "8",
                    "HookAddress": "http:www.baidu.com"
                }
            ],
            "RuleId": 1,
            "RuleName": "规则1"
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```


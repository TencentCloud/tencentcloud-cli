**Example 1: 更新规则组订阅信息**



Input: 

```
tccli wedata ModifyRuleGroupSubscription --cli-unfold-argument  \
    --DatabaseId xx \
    --Receivers.0.ReceiverUserId 1 \
    --Receivers.0.ReceiverName xx \
    --ProjectId xx \
    --RuleGroupId 1 \
    --SubscribeType 1 \
    --DatasourceId xx \
    --TableId xx
```

Output: 
```
{
    "Response": {
        "Data": 123456,
        "RequestId": "xx"
    }
}
```


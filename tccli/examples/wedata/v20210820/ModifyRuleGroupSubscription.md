**Example 1: 更新规则组订阅信息**

生成/编辑规则组的订阅信息

Input: 

```
tccli wedata ModifyRuleGroupSubscription --cli-unfold-argument  \
    --RuleGroupId 1 \
    --Receivers.0.ReceiverUserId 1 \
    --Receivers.0.ReceiverName zhangsan \
    --SubscribeType 1 \
    --ProjectId 5667890432 \
    --DatabaseId r896tygouq24tg79 \
    --DatasourceId 567890 \
    --TableId 980yuiheowfcsy8huio23 \
    --WebHooks.0.HookType 8 \
    --WebHooks.0.HookAddress www.baidu.com
```

Output: 
```
{
    "Response": {
        "Data": 1,
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```


**Example 1: 更新规则组订阅信息**

生成/编辑规则组的订阅信息

Input: 

```
tccli wedata ModifyRuleGroupSubscription --cli-unfold-argument  \
    --DatabaseId xx \
    --Receivers.0.ReceiverUserId 1 \
    --Receivers.0.ReceiverName xx \
    --WebHooks.0.HookType feishu \
    --WebHooks.0.HookAddress http://xxxxxxxxxxxx \
    --WebHooks.1.HookType feishu \
    --WebHooks.1.HookAddress http://xxxxxxxxxxxx \
    --ProjectId xx \
    --RuleGroupId 1 \
    --SubscribeType 1 7 \
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


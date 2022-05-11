**Example 1: 创建规则示例**



Input: 

```
tccli iotcloud CreateTopicRule --cli-unfold-argument  \
    --TopicRulePayload.Sql U0VMRUNUIGZpZWxkMSwgZmllbGQyIEZST00gJ3NyY1Byb2R1Y3RJZC9zcmNEZXZpY2VOYW1lL2V2ZW50Jw== \
    --TopicRulePayload.Description xx \
    --TopicRulePayload.Actions [] \
    --TopicRulePayload.RuleDisabled True \
    --RuleName testrulename
```

Output: 
```
{
    "Response": {
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e97e"
    }
}
```


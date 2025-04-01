**Example 1: 替换规则示例**



Input: 

```
tccli iotcloud ReplaceTopicRule --cli-unfold-argument  \
    --RuleName test \
    --TopicRulePayload.Sql SELECT * FROM '#' \
    --TopicRulePayload.Actions [1] \
    --TopicRulePayload.Description mydescription \
    --TopicRulePayload.RuleDisabled True
```

Output: 
```
{
    "Response": {
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e97e"
    }
}
```


**Example 1: 创建规则**



Input: 

```
tccli iotexplorer CreateTopicRule --cli-unfold-argument  \
    --RuleName test_create \
    --TopicRulePayload.Sql U0VMRUNUICogRlJPTSAnJHRoaW5nL3VwLysvVFRVMk5OSVU3MC8jJw== \
    --TopicRulePayload.Actions [{"forward":{"api":"http://127.0.0.1:1080/sub.php"}}] \
    --TopicRulePayload.Description test \
    --TopicRulePayload.RuleDisabled True
```

Output: 
```
{
    "Response": {
        "RequestId": "f92406b3-5a9a-4fe8-bc43-45e3d794bb68"
    }
}
```


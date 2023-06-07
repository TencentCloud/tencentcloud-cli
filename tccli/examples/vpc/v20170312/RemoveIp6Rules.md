**Example 1: 删除IPV6转换规则**

删除IPV6转换规则。

Input: 

```
tccli vpc RemoveIp6Rules --cli-unfold-argument  \
    --Ip6TranslatorId ip6-90pt7p9q \
    --Ip6RuleIds rule6-k5l5hnwk
```

Output: 
```
{
    "Response": {
        "RequestId": "688521e4-25d8-4b28-b0de-2b098f6fe535"
    }
}
```


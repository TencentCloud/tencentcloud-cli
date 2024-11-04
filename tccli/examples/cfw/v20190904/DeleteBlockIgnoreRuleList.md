**Example 1: 批量删除入侵防御封禁列表、放通列表规则**



Input: 

```
tccli cfw DeleteBlockIgnoreRuleList --cli-unfold-argument  \
    --Rules.0.IP 1.1.1.1 \
    --Rules.0.Direction 0 \
    --Rules.0.Domain  \
    --RuleType 0
```

Output: 
```
{
    "Response": {
        "RequestId": ""
    }
}
```


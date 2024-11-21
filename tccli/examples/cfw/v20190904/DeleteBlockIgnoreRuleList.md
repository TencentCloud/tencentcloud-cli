**Example 1: 批量删除入侵防御封禁列表、放通列表规则**



Input: 

```
tccli cfw DeleteBlockIgnoreRuleList --cli-unfold-argument  \
    --Rules.0.IP 1.1.1.1 \
    --Rules.0.Direction 0 \
    --Rules.0.Domain www.doamin.com \
    --RuleType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "29f9896a-bb5e-49d1-840c-cf3a0177bd2d"
    }
}
```


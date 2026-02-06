**Example 1: 修改规则状态**



Input: 

```
tccli waf ModifyOwaspRuleStatus --cli-unfold-argument  \
    --Domain owasp.saas3.testwaf.com \
    --RuleStatus 1 \
    --SelectAll False \
    --RuleIDs 16 \
    --TypeId 10000000
```

Output: 
```
{
    "Response": {
        "RequestId": "c7d727dd-48de-4609-ba67-6cca079bae04"
    }
}
```


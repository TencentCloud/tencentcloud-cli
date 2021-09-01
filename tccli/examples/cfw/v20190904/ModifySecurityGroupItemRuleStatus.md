**Example 1: 启用停用单条企业安全组规则**

启用停用单条企业安全组规则

Input: 

```
tccli cfw ModifySecurityGroupItemRuleStatus --cli-unfold-argument  \
    --RuleSequence 5 \
    --Direction 1 \
    --Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "Status": 0
    }
}
```


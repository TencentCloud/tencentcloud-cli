**Example 1: 互联网边界规则快速排序**

互联网边界规则快速排序

Input: 

```
tccli cfw ModifySequenceAclRules --cli-unfold-argument  \
    --RuleChangeItems.0.OrderIndex 0 \
    --RuleChangeItems.0.NewOrderIndex 0 \
    --Direction 1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```


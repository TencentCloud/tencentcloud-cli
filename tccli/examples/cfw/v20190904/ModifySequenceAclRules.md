**Example 1: 互联网边界规则快速排序**

互联网边界规则快速排序

Input: 

```
tccli cfw ModifySequenceAclRules --cli-unfold-argument  \
    --RuleChangeItems.0.OrderIndex 2 \
    --RuleChangeItems.0.NewOrderIndex 1 \
    --RuleChangeItems.1.OrderIndex 1 \
    --RuleChangeItems.1.NewOrderIndex 2 \
    --Direction 0
```

Output: 
```
{
    "Response": {
        "RequestId": "b02e2d2c-ce3c-425a-bcc1-cfc6b454162c"
    }
}
```


**Example 1: NAT防火墙规则快速排序**

NAT防火墙规则快速排序

Input: 

```
tccli cfw ModifyNatSequenceRules --cli-unfold-argument  \
    --RuleChangeItems.0.OrderIndex 1 \
    --RuleChangeItems.0.NewOrderIndex 2 \
    --RuleChangeItems.1.OrderIndex 2 \
    --RuleChangeItems.1.NewOrderIndex 1 \
    --Direction 1
```

Output: 
```
{
    "Response": {
        "RequestId": "985187d2-9a80-4ee7-b519-ad48e75f6588"
    }
}
```


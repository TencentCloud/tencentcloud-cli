**Example 1: NAT防火墙规则快速排序**

NAT防火墙规则快速排序

Input: 

```
tccli cfw ModifyNatSequenceRules --cli-unfold-argument  \
    --RuleChangeItems.0.OrderIndex 0 \
    --RuleChangeItems.0.NewOrderIndex 0 \
    --Direction 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```


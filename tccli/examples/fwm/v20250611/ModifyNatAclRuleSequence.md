**Example 1: NAT 规则组内快速排序**



Input: 

```
tccli fwm ModifyNatAclRuleSequence --cli-unfold-argument  \
    --GroupId fwmrg_wrzekq94u7 \
    --Sequences.0.OrderIndex 1 \
    --Sequences.0.NewOrderIndex 3 \
    --Sequences.1.OrderIndex 2 \
    --Sequences.1.NewOrderIndex 1 \
    --Sequences.2.OrderIndex 3 \
    --Sequences.2.NewOrderIndex 2 \
    --Direction 1
```

Output: 
```
{
    "Response": {
        "RequestId": "7d8a3017-26bb-4d73-b2e3-58ca0443bb3b"
    }
}
```


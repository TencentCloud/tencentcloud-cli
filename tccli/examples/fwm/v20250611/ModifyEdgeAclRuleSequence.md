**Example 1: 互联网边界规则组内规则快速排序**



Input: 

```
tccli fwm ModifyEdgeAclRuleSequence --cli-unfold-argument  \
    --Direction 1 \
    --GroupId fwmrg_4ae6vv1l7c \
    --Sequences.0.OrderIndex 1 \
    --Sequences.0.NewOrderIndex 2 \
    --Sequences.1.OrderIndex 2 \
    --Sequences.1.NewOrderIndex 3 \
    --Sequences.2.OrderIndex 3 \
    --Sequences.2.NewOrderIndex 4 \
    --Sequences.3.OrderIndex 4 \
    --Sequences.3.NewOrderIndex 1
```

Output: 
```
{
    "Response": {
        "RequestId": "025c3756-bf58-408e-b806-2e68ead7f6a0"
    }
}
```


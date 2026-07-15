**Example 1: VPC 规则组内规则快速排序**



Input: 

```
tccli fwm ModifyVpcAclRuleSequence --cli-unfold-argument  \
    --GroupId fwmrg_aussbmarr2 \
    --Sequences.0.OrderIndex 1 \
    --Sequences.0.NewOrderIndex 3 \
    --Sequences.1.OrderIndex 2 \
    --Sequences.1.NewOrderIndex 1 \
    --Sequences.2.OrderIndex 3 \
    --Sequences.2.NewOrderIndex 2
```

Output: 
```
{
    "Response": {
        "RequestId": "3034a6c8-1bc4-4e4e-b69b-a11b1468b79e"
    }
}
```


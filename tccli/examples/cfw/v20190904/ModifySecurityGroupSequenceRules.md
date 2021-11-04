**Example 1: 企业安全组规则快速排序**

企业安全组规则快速排序

Input: 

```
tccli cfw ModifySecurityGroupSequenceRules --cli-unfold-argument  \
    --Direction 1 \
    --Data.0.NewOrderIndex 1 \
    --Data.0.OrderIndex 2 \
    --Data.1.NewOrderIndex 2 \
    --Data.1.OrderIndex 1
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


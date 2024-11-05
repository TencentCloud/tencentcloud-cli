**Example 1: vpc间规则快速排序**

vpc间规则快速排序示例

Input: 

```
tccli cfw ModifyVpcFwSequenceRules --cli-unfold-argument  \
    --RuleChangeItems.0.OrderIndex 2 \
    --RuleChangeItems.0.NewOrderIndex 1 \
    --RuleChangeItems.1.OrderIndex 1 \
    --RuleChangeItems.1.NewOrderIndex 2
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```


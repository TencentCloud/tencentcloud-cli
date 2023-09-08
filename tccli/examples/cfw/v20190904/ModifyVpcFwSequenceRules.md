**Example 1: vpc间规则快速排序**

vpc间规则快速排序示例

Input: 

```
tccli cfw ModifyVpcFwSequenceRules --cli-unfold-argument  \
    --RuleChangeItems.0.OrderIndex 100 \
    --RuleChangeItems.0.NewOrderIndex 100
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```


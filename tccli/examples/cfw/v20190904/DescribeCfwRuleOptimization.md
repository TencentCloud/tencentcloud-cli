**Example 1: 查询互联网边界规则优化建议**

只读返回优化建议；示例仅展示代表性字段，是否处理以及如何处理由调用方决定。

Input: 

```
tccli cfw DescribeCfwRuleOptimization --cli-unfold-argument  \
    --IdleDays 180
```

Output: 
```
{
    "Response": {
        "Data": "{\"rule_type\":\"border\",\"dimension_counts\":{\"D1\":1},\"finding_total\":1,\"findings\":[{\"dim\":\"D1 完全重复\"}]}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```


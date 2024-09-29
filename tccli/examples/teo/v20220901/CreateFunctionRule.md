**Example 1: 创建边缘函数规则**



Input: 

```
tccli teo CreateFunctionRule --cli-unfold-argument  \
    --ZoneId zone-293e7s5jne1i \
    --FunctionRuleConditions.0.RuleConditions.0.Operator equal \
    --FunctionRuleConditions.0.RuleConditions.0.Values /123 \
    --FunctionRuleConditions.0.RuleConditions.0.Target url \
    --FunctionId ef-1pakhnuy \
    --Remark my function rule
```

Output: 
```
{
    "Response": {
        "RuleId": "rule-vnqup0uc",
        "RequestId": "aab9a28a-4cce-434d-852f-5442275817aa"
    }
}
```


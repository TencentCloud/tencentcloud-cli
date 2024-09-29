**Example 1: 修改边缘函数规则**



Input: 

```
tccli teo ModifyFunctionRule --cli-unfold-argument  \
    --ZoneId zone-2gqxim9jstab \
    --RuleId rule-vnqup0uc \
    --FunctionRuleConditions.0.RuleConditions.0.Operator equal \
    --FunctionRuleConditions.0.RuleConditions.0.Values /test \
    --FunctionRuleConditions.0.RuleConditions.0.Target url \
    --FunctionId ef-1pakhnuy \
    --Remark my function
```

Output: 
```
{
    "Response": {
        "RequestId": "7a1e998f-fa00-4670-8457-ed4b4fe5018a"
    }
}
```


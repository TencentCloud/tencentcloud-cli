**Example 1: 启用停用VPC间规则或Nat边界规则**

启用停用VPC间规则或Nat边界规则

Input: 

```
tccli cfw ModifyEWRuleStatus --cli-unfold-argument  \
    --RuleSequence 5 \
    --Direction 1 \
    --Status 1 \
    --RuleType vpc \
    --EdgeId EdgeId
```

Output: 
```
{
    "Response": {
        "ReturnMsg": "success",
        "ReturnCode": 0,
        "RequestId": "9a86c4e3-b926-4244-919b-aba9a7e82686"
    }
}
```


**Example 1: 示例**

示例

Input: 

```
tccli dsgc CreateIdentifyRuleAnotherName --cli-unfold-argument  \
    --DspaId dspa-abcd1234 \
    --ComplianceId 100118 \
    --CategoryId 1 \
    --RuleId 128 \
    --RuleName 身份证校验 \
    --AnotherName id-card
```

Output: 
```
{
    "Response": {
        "RequestId": "test-002"
    }
}
```


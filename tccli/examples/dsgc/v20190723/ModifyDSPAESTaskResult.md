**Example 1: 示例**

示例

Input: 

```
tccli dsgc ModifyDSPAESTaskResult --cli-unfold-argument  \
    --DspaId dspa-abcd1234 \
    --FieldResultId 1 \
    --IsSetNonSensitiveField True \
    --DestRuleId 128 \
    --DestCategoryId 2 \
    --DestLevelId 101 \
    --ComplianceId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "test-003"
    }
}
```


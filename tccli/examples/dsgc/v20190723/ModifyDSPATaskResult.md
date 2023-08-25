**Example 1: 调整任务扫描结果**



Input: 

```
tccli dsgc ModifyDSPATaskResult --cli-unfold-argument  \
    --ComplianceId 1 \
    --DestRuleId 1 \
    --FieldResultId 1 \
    --DspaId 1 \
    --DestCategoryId 1 \
    --DestLevelId 1 \
    --IsSetNonSensitiveField true
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```


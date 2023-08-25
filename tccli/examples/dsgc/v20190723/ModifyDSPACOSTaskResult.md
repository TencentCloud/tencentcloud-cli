**Example 1: 调整COS任务扫描结果**



Input: 

```
tccli dsgc ModifyDSPACOSTaskResult --cli-unfold-argument  \
    --IsSetNonSensitiveFile true \
    --FileResultId 1 \
    --DspaId 1 \
    --ComplianceId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```


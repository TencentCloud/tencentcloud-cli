**Example 1: 示例**



Input: 

```
tccli wedata CreateCalcField --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --DashboardAccessKey 800017322219413504 \
    --DatasetKey fc3c9d4d176879276283850d1494e \
    --DisplayName 测试2 \
    --Description  \
    --CalcFormula ZGVwYXJ0bWVudA==
```

Output: 
```
{
    "Response": {
        "Data": {
            "Key": "0ff1d6291770117210285f5359b30",
            "DatasetKey": "fc3c9d4d176879276283850d1494e",
            "TranId": "76344598cc0c9595c51fea702d6d44af",
            "TranStatus": "1",
            "ErrorMessage": ""
        },
        "RequestId": "5837d9fe-9f85-452a-aaaa-9e11f08e77eb"
    }
}
```


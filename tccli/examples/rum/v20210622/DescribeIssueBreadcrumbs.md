**Example 1: 示例**



Input: 

```
tccli rum DescribeIssueBreadcrumbs --cli-unfold-argument  \
    --AppId 146692 \
    --IssueId 0f5f040e0c3d999eb9557bdb3adcd18253d64785594e80785d443d222d3abe1f \
    --EventId evt_1782809888621_krrt7d \
    --Before 60 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Result": "{\"Data\":{\"session_id\":\"bce090071fdf4aa9a5d5ef4f242dd4f1\",\"items\":[{\"ts\":1782809888515,\"category\":\"behavior\",\"event_type\":\"click\",\"message\":\"触发JS错误\",\"data\":{\"target_class\":\"test-button danger-button\",\"target_id\":\"\"}}]}}",
        "RequestId": "a841adcc-60a0-48e0-992c-10c0e7ddc61f"
    }
}
```


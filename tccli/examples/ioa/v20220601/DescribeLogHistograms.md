**Example 1: 示例1**



Input: 

```
tccli ioa DescribeLogHistograms --cli-unfold-argument  \
    --StartTime 1777305600 \
    --LogId LicenseAuth \
    --Step day \
    --Filters.0.Field TenantId \
    --Filters.0.Operator eq \
    --Filters.0.Values 251437404 \
    --Filters.0.Describe 租户ID \
    --EndTime 1777391999
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": [
                {
                    "Timestamp": 1777305600,
                    "Value": 5
                }
            ],
            "Total": 1
        },
        "RequestId": "c5848f1b-da8b-458e-a25b-4a891225aaa8"
    }
}
```


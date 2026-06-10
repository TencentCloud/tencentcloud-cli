**Example 1: 示例1**



Input: 

```
tccli csip CreateIaCFileExportJob --cli-unfold-argument  \
    --Filter.Limit 1000000 \
    --Filter.Offset 0 \
    --Filter.Filters.0.Name Status \
    --Filter.Filters.0.Values 3 \
    --Filter.Filters.0.OperatorType 7 \
    --Filter.StartTime 2026-04-01T00:00:00+08:00 \
    --Filter.EndTime 2026-04-07T23:59:59+08:00 \
    --MemberId mem-a6df317cb6a8c424
```

Output: 
```
{
    "Response": {
        "JobID": "0129d37d-4f23-4657-a09b-312313b88dad",
        "RequestId": "ca090e80-d2e8-4b0d-abff-8d75406a7c93"
    }
}
```


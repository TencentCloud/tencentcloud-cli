**Example 1: 示例1**



Input: 

```
tccli wedata ListTaskInstanceInfo --cli-unfold-argument  \
    --WorkspaceId spaceId \
    --PageNumber 1 \
    --PageSize 10 \
    --TaskId taskId \
    --Filters.0.Name name \
    --Filters.0.Values value \
    --OrderFields.0.Name dk \
    --OrderFields.0.Direction desc \
    --StartTime 12 \
    --EndTime 23
```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                {
                    "Container": "container-1",
                    "JobId": "job-1",
                    "RunningOrderId": "orderid-1"
                }
            ],
            "TotalNum": "1"
        },
        "RequestId": "88f936c0-dd47-4d14-bc5b-d5da0fff0a74"
    }
}
```


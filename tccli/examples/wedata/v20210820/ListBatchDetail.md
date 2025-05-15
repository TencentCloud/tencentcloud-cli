**Example 1: 成功示例**



Input: 

```
tccli wedata ListBatchDetail --cli-unfold-argument  \
    --JobId 118786 \
    --ProjectId 1461767738399854592
```

Output: 
```
{
    "Response": {
        "FailResource": [
            {
                "ExtraInfo": null,
                "ProcessId": 190394,
                "ResourceId": "20250415191408327",
                "ResourceName": "aaaadasd"
            }
        ],
        "JobId": 118786,
        "JobStatus": "FAIL",
        "JobType": "BATCH_MODIFY_SCHEDULE",
        "NeedApprove": false,
        "RequestId": "2fe33308-82db-4d40-a275-d9fca1e5e284",
        "RunType": "ASYNC",
        "SuccessResource": [],
        "TotalResource": 1
    }
}
```


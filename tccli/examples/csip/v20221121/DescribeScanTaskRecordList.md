**Example 1: 扫描任务记录**



Input: 

```
tccli csip DescribeScanTaskRecordList --cli-unfold-argument  \
    --MemberId mem-68b*0**a***6***0 \
    --Limit 1 \
    --Offset 0 \
    --Order UpdateTime \
    --By DESC
```

Output: 
```
{
    "Response": {
        "TaskRecordList": [
            {
                "CostQuota": 0,
                "CreateTime": "2026-04-19 00:04:13",
                "EndTime": "2026-04-19 00:22:53",
                "Progress": 100,
                "Status": "completed",
                "TaskID": "csip-main-task-a6ae8383e62d974882457fd60353a5ad",
                "TaskSource": "asset_cron"
            }
        ],
        "TotalCount": 8,
        "RequestId": "f73c087e-40d2-46d8-913e-58d075a00b9d"
    }
}
```


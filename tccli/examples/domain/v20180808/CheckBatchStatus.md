**Example 1: 检查批量任务状态**



Input: 

```
tccli domain CheckBatchStatus --cli-unfold-argument  \
    --LogIds 1
```

Output: 
```
{
    "Response": {
        "RequestId": "d391e9be-c0ef-11ea-9522-080027f4585e",
        "StatusSet": [
            {
                "LogId": 1,
                "Status": "failed",
                "BatchAction": "batch_transfer_prohibition"
            },
            {
                "LogId": 2,
                "Status": "failed",
                "BatchAction": "batch_transfer_prohibition"
            }
        ]
    }
}
```


**Example 1: 批量操作日志**



Input: 

```
tccli domain DescribeBatchOperationLogs --cli-unfold-argument  \
    --Offset 1 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "DomainBatchLogSet": [
            {
                "LogId": 10001,
                "Number": 1,
                "Status": "doing",
                "CreatedOn": "2023-01-01 20:30:00",
                "Success": 0,
                "Doing": 0,
                "Failed": 0
            }
        ],
        "RequestId": "xxxx-xxx-xxx-xxxx"
    }
}
```


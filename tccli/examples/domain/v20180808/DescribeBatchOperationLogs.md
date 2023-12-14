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
                "LogId": 0,
                "Number": 0,
                "Status": "abc",
                "CreatedOn": "abc",
                "Success": 0,
                "Doing": 0,
                "Failed": 0
            }
        ],
        "RequestId": "abc"
    }
}
```


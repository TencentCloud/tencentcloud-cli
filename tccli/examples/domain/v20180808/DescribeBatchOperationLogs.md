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
        "TotalCount": 204,
        "DomainBatchLogSet": [
            {
                "LogId": 318,
                "CreatedOn": "2020-06-10 20:08:43",
                "Number": 12,
                "Status": "doing"
            }
        ],
        "RequestId": "1af07f55-2b13-4076-a301-74c2480f7af7"
    },
    "ResultStatus": true
}
```


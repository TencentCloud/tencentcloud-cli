**Example 1: 批量购买域名日志**



Input: 

```
tccli domain DescribeIntlBatchOperationLogs --cli-unfold-argument  \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 204,
        "DomainBatchLogSet": [
            {
                "LogId": 318,
                "Action": "new",
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


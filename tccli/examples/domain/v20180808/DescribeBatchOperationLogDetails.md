**Example 1: 批量操作日志详情**



Input: 

```
tccli domain DescribeBatchOperationLogDetails --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --LogId 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 12,
        "RequestId": "13f43fa6-7282-4652-a99c-66819145ba5f",
        "DomainBatchDetailSet": [
            {
                "Status": "doing",
                "Domain": "qq.com",
                "UpdatedOn": "2020-06-10 20:08:50",
                "CreatedOn": "2020-06-10 20:08:44",
                "Reason": "",
                "Id": 1
            }
        ]
    },
    "ResultStatus": true
}
```


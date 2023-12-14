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
        "TotalCount": 0,
        "DomainBatchDetailSet": [
            {
                "Id": 0,
                "Action": "abc",
                "Domain": "abc",
                "Status": "abc",
                "Reason": "abc",
                "CreatedOn": "abc",
                "UpdatedOn": "abc",
                "BigDealId": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```


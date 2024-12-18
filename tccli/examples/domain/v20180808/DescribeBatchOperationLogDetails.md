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
        "TotalCount": 1,
        "RequestId": "f376d0e6-f064-1234-b27f-a8ae3b054dfa",
        "DomainBatchDetailSet": [
            {
                "UpdatedOn": "2024-12-18 12:21:16",
                "BigDealId": "",
                "Action": "batch_modify_domain_dns1",
                "Status": "failed",
                "Domain": "***.com",
                "CreatedOn": "2024-12-18 12:21:12",
                "Reason": "域名已开启【禁止更新锁】保护域名信息安全，不能修改信息。如需操作，请先关闭【禁止更新锁】",
                "Id": 1001
            }
        ]
    }
}
```


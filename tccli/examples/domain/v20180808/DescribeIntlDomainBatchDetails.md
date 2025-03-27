**Example 1: 获取批量购买域名日志详情**



Input: 

```
tccli domain DescribeIntlDomainBatchDetails --cli-unfold-argument  \
    --LogId 1 \
    --Limit 0 \
    --Offset 0
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
                "Domain": "batchzz426.club",
                "UpdatedOn": "2020-06-10 20:08:50",
                "CreatedOn": "2020-06-10 20:08:44",
                "Reason": "",
                "ReasonZh": "修改DNS失败",
                "Action": "new",
                "Id": 85215,
                "TransferDnsResult": true,
                "PayStatus": 0,
                "BigDealId": ""
            }
        ]
    }
}
```


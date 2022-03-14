**Example 1: 获取代金券使用记录**



Input: 

```
tccli billing DescribeVoucherUsageDetails --cli-unfold-argument  \
    --Limit 10 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": "0",
        "TotalUsedAmount": 0,
        "UsageRecords": [
            {
                "UsedAmount": 0,
                "UsedTime": "xx",
                "UsageDetails": [
                    {
                        "ProductName": "xxx",
                        "SubProductName": "xxx"
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```


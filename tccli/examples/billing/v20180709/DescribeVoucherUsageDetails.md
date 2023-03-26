**Example 1: 获取代金券使用记录**

获取代金券使用记录

Input: 

```
tccli billing DescribeVoucherUsageDetails --cli-unfold-argument  \
    --Limit 10 \
    --Offset 1 \
    --VoucherId "abc" \
    --Operator "abc"
```

Output: 
```
{
    "Response": {
        "TotalCount": "1",
        "TotalUsedAmount": 18000000000,
        "UsageRecords": [
            {
                "UsedAmount": 18000000000,
                "UsedTime": "2021-01-01 00:00:00",
                "UsageDetails": [
                    {
                        "ProductName": "轻量应用服务器",
                        "SubProductName": "轻量应用服务器 (通用型-2核2G-50G-500G)"
                    }
                ]
            }
        ],
        "RequestId": "76cf663e-f683-41b9-b44d-849123783bf4"
    }
}
```


**Example 1: 经销商查询子客代金券使用详情**

经销商查询子客代金券使用详情

Input: 

```
tccli intlpartnersmgt DescribeCustomerVoucherUsageDetails --cli-unfold-argument  \
    --Page 1 \
    --PageSize 10 \
    --CustomerUin 800000495142 \
    --VoucherId 12130012 \
    --Month 2024-03
```

Output: 
```
{
    "Response": {
        "CustomerUin": 800000495142,
        "Data": [],
        "Month": "2024-03",
        "RecordsCountByMonth": 0,
        "RemainAmount": 0,
        "TotalAmount": 1,
        "TotalRecordsCount": 2,
        "VoucherId": 12130012,
        "RequestId": "28404cbe-6694-4b52-84a7-74e61efac79f"
    }
}
```


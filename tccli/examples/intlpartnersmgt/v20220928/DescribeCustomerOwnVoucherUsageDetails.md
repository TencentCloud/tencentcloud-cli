**Example 1: 子客查询自身代金券使用详情**

子客查询自身代金券使用详情

Input: 

```
tccli intlpartnersmgt DescribeCustomerOwnVoucherUsageDetails --cli-unfold-argument  \
    --Page 1 \
    --PageSize 100 \
    --VoucherId 12365856 \
    --Month 2026-03
```

Output: 
```
{
    "Response": {
        "Data": [],
        "Month": "2026-03",
        "RecordsCountByMonth": 0,
        "RemainAmount": 0,
        "TotalAmount": 0,
        "TotalRecordsCount": 0,
        "VoucherId": 12365856,
        "RequestId": "3a9de07b-5f47-4f20-98b4-6fcb562af626"
    }
}
```


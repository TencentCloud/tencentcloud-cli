**Example 1: 通过API获取子客账单地域汇总值**

通过API获取子客账单地域汇总值

Input: 

```
tccli intlpartnersmgt DescribeBillSummaryByRegion --cli-unfold-argument  \
    --BillMonth 2022-11 \
    --CustomerUin 123456
```

Output: 
```
{
    "Response": {
        "SummaryOverview": [
            {
                "RegionId": "8",
                "RegionName": "1North China (Beijing)",
                "OriginalCost": "100.00000000",
                "VoucherPayAmount": "100.00000000",
                "TotalCost": "100.00000000"
            }
        ],
        "RequestId": "asdfgh"
    }
}
```


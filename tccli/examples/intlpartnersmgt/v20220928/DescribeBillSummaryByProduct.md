**Example 1: 获取子客账单产品维度汇总值**

获取子客账单产品维度汇总值

Input: 

```
tccli intlpartnersmgt DescribeBillSummaryByProduct --cli-unfold-argument  \
    --BillMonth 2022-11 \
    --CustomerUin 123456
```

Output: 
```
{
    "Response": {
        "SummaryOverview": [
            {
                "BusinessCode": "p_cbs",
                "BusinessCodeName": "cloud block storage",
                "OriginalCost": "100.00000000",
                "VoucherPayAmount": "100.00000000",
                "TotalCost": "100.00000000"
            }
        ],
        "RequestId": "asdfgh"
    }
}
```


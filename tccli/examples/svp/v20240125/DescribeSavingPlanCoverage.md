**Example 1: 示例**

示例

Input: 

```
tccli svp DescribeSavingPlanCoverage --cli-unfold-argument  \
    --StartDate 2024-12-01 \
    --EndDate 2024-12-30 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "DetailSet": [
            {
                "BillingItemName": "计费项",
                "EndDate": "2024-12-30",
                "ExpectedAmount": -4.550174,
                "OwnerUinName": "9099账号",
                "PayerUin": "9099",
                "PayerUinName": "9099账号",
                "ProductCode": "p_cbs",
                "RegionId": 1,
                "ResourceId": "billingVirtualHighPrecisionFlatAccountId_",
                "SpCoverage": 0,
                "SpCoveredAmount": 0,
                "SpUncoveredAmount": -4.550174,
                "StartDate": "2024-12-01",
                "SubBillingItemName": "计费细项",
                "SubProductCode": "sp_cbs_bssd",
                "SubProductName": "通用型SSD云硬盘",
                "TotalRealAmount": -4.550174
            }
        ],
        "RateSet": [
            {
                "DatePoint": "2024-12-01",
                "Rate": 10.05
            }
        ],
        "RequestId": "7816cba1-60d9-4a07-8556-5b62ab8d3641",
        "TotalCount": 25
    }
}
```


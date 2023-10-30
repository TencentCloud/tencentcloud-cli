**Example 1: 查询节省计划覆盖率数据**

查询节省计划覆盖率数据

Input: 

```
tccli billing DescribeSavingPlanCoverage --cli-unfold-argument  \
    --PeriodType 1 \
    --StartDate 2023-06-01 \
    --EndDate 2023-07-01 \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "DetailSet": [
            {
                "EndDate": "2023-06-13",
                "ExpectedAmount": 99.01,
                "ProductCode": "p_trade_t_s",
                "RegionId": 1,
                "ResourceId": "0140051917592",
                "SpCoverage": 0,
                "SpCoveredAmount": 0,
                "SpUncoveredAmount": 99.01,
                "StartDate": "2023-06-13",
                "SubProductCode": "sp_trade_t_s",
                "TotalRealAmount": 99.01
            },
            {
                "EndDate": "2023-06-13",
                "ExpectedAmount": 99.01,
                "ProductCode": "p_trade_t_s",
                "RegionId": 1,
                "ResourceId": "0140053056082",
                "SpCoverage": 0,
                "SpCoveredAmount": 0,
                "SpUncoveredAmount": 99.01,
                "StartDate": "2023-06-13",
                "SubProductCode": "sp_trade_t_s",
                "TotalRealAmount": 99.01
            }
        ],
        "RateSet": [
            {
                "DatePoint": "2023-06-07",
                "Rate": 0
            },
            {
                "DatePoint": "2023-06-13",
                "Rate": 0
            },
            {
                "DatePoint": "2023-06-14",
                "Rate": 0
            }
        ],
        "RequestId": "a0041c91-65c3-4552-8802-f073cfed0202",
        "TotalCount": 6
    }
}
```


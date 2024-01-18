**Example 1: 输出示例**

查询名下可共享的sp资源详细

Input: 

```
tccli billing DescribeSavingPlanResourceInfo --cli-unfold-argument  \
    --Limit 0 \
    --Offset 1 \
    --CreateStartDate 2023-06-01 \
    --CreateEndDate 2023-09-30
```

Output: 
```
{
    "Response": {
        "RequestId": "37963bb4-f4ac-4c20-8c83-97d751f1aa91",
        "SavingPlanInfoData": [
            {
                "BuyTime": "2023-09-07 10:30:11",
                "EndTime": "2023-09-17 10:00:00",
                "MatchingSavingPlanProductRule": [
                    {
                        "BillingItemCode": "*",
                        "MatchFlag": "include",
                        "ProductCode": "p_cvm",
                        "SubBillingItemCode": "*",
                        "SubProductCode": "*"
                    }
                ],
                "MatchingSavingPlanRegionRule": [
                    {
                        "RegionId": "1",
                        "ZoneIdList": [
                            "*"
                        ]
                    }
                ],
                "SpId": "svp-victotman-test2",
                "SpType": "svp_common",
                "StartTime": "2023-09-17 10:00:00",
                "Status": 1
            }
        ],
        "Total": 3
    }
}
```


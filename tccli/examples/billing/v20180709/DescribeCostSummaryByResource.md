**Example 1: 获取按资源汇总消耗详情**

获取按资源汇总消耗详情

Input: 

```
tccli billing DescribeCostSummaryByResource --cli-unfold-argument  \
    --EndTime 2018-11 \
    --Limit 1 \
    --BeginTime 2018-11 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "Total": {
            "RealTotalCost": "abc"
        },
        "ConditionValue": {
            "Business": [
                {
                    "BusinessCode": "abc",
                    "BusinessCodeName": "abc"
                }
            ],
            "Project": [
                {
                    "ProjectId": "abc",
                    "ProjectName": "abc"
                }
            ],
            "Region": [
                {
                    "RegionId": "abc",
                    "RegionName": "abc"
                }
            ],
            "PayMode": [
                {
                    "PayMode": "abc",
                    "PayModeName": "abc"
                }
            ]
        },
        "RecordNum": 1,
        "Data": [
            {
                "ResourceId": "abc",
                "ResourceName": "abc",
                "RealTotalCost": "abc",
                "CashPayAmount": "abc",
                "ProjectId": "abc",
                "ProjectName": "abc",
                "RegionId": "abc",
                "RegionName": "abc",
                "PayMode": "abc",
                "PayModeName": "abc",
                "BusinessCode": "abc",
                "BusinessCodeName": "abc",
                "ConsumptionTypeName": "abc",
                "RealCost": "abc",
                "FeeBeginTime": "abc",
                "FeeEndTime": "abc",
                "DayDiff": "abc",
                "DailyTotalCost": "abc",
                "OrderId": "abc",
                "VoucherPayAmount": "abc",
                "IncentivePayAmount": "abc",
                "TransferPayAmount": "abc",
                "PayerUin": "abc",
                "OwnerUin": "abc",
                "OperateUin": "abc",
                "ProductCode": "abc",
                "ProductCodeName": "abc",
                "RegionType": "abc",
                "RegionTypeName": "abc",
                "Extend1": "abc",
                "Extend2": "abc",
                "Extend3": "abc",
                "Extend4": "abc",
                "Extend5": "abc",
                "InstanceType": "abc",
                "InstanceTypeName": "abc",
                "PayTime": "abc",
                "ZoneName": "abc",
                "ComponentConfig": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```


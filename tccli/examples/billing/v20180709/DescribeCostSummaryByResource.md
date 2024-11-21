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
        "RecordNum": 4,
        "ConditionValue": {
            "Business": [
                {
                    "BusinessCode": "p_cdn",
                    "BusinessCodeName": "内容分发网络 CDN"
                }
            ],
            "Project": [
                {
                    "ProjectId": "0",
                    "ProjectName": "默认项目"
                }
            ],
            "Region": [
                {
                    "RegionId": "0",
                    "RegionName": "其他"
                }
            ],
            "PayMode": [
                {
                    "PayMode": "postPay",
                    "PayModeName": "按量计费"
                }
            ]
        },
        "Total": {
            "RealTotalCost": "0.07"
        },
        "Data": [
            {
                "OwnerUin": "10002011014",
                "PayerUin": "10002011014",
                "OperateUin": "10002011014",
                "BusinessCode": "p_cdn",
                "BusinessCodeName": "内容分发网络 CDN",
                "ProductCode": "sp_cdn_ov",
                "ProductCodeName": "中国境外CDN",
                "ResourceId": "1300342678_1002522_102391_sv_cdn_ov_hour_flux_AS1_1",
                "ResourceName": "未命名",
                "RealTotalCost": "0.07",
                "RealCost": "0.08",
                "CashPayAmount": "0.06570339",
                "RegionId": "1001",
                "RegionName": "亚太地区（亚太一区）",
                "RegionType": "international",
                "RegionTypeName": "国际",
                "PayMode": "postPay",
                "PayModeName": "按量计费",
                "ProjectId": "0",
                "ProjectName": "默认项目",
                "FeeBeginTime": "2024-11-01 08:00:00",
                "FeeEndTime": "2024-11-17 19:59:59",
                "DayDiff": "17",
                "DailyTotalCost": "0.00386491",
                "ConsumptionTypeName": "按量计费小时结",
                "OrderId": "-",
                "VoucherPayAmount": "0.00000000",
                "IncentivePayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000",
                "Extend1": "",
                "Extend2": "",
                "Extend3": "",
                "Extend4": "",
                "Extend5": "",
                "InstanceType": "-",
                "InstanceTypeName": "-",
                "PayTime": "-",
                "ZoneName": "其他",
                "ComponentConfig": "海外CDN-按小时结算-流量: 0.00000533 GB",
                "Tags": ""
            }
        ],
        "RequestId": "4a3ec37d-7628-4e22-b9ab-08e696bcc1f2"
    }
}
```


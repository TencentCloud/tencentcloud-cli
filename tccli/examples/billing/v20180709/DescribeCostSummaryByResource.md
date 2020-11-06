**Example 1: 获取按资源汇总消耗详情**



Input: 

```
tccli billing DescribeCostSummaryByResource --cli-unfold-argument  \
    --PayerUin 909619400 \
    --BeginTime 2018-11-0100:00:00 \
    --EndTime 2018-11-3023:59:59 \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ConditionValue": {
            "Business": [
                {
                    "BusinessCode": "p_cdb",
                    "BusinessCodeName": "云数据库MySQL"
                }
            ],
            "Project": [
                {
                    "ProjectId": "1003540",
                    "ProjectName": "默认项目"
                }
            ],
            "Region": [
                {
                    "RegionId": "1",
                    "RegionName": "华南地区（广州）"
                }
            ],
            "PayMode": [
                {
                    "PayMode": "prePay",
                    "PayModeName": "包年包月"
                }
            ]
        },
        "Total": {
            "RealTotalCost": "510.15"
        },
        "Data": [
            {
                "BusinessCode": "billVirtualId",
                "BusinessCodeName": "月度计费精度差异",
                "ResourceId": "billVirtualId",
                "ResourceName": "扣费精度补偿",
                "RealTotalCost": "-0.69",
                "CashPayAmount": "-0.69",
                "RegionId": "0",
                "RegionName": "其他",
                "PayMode": "postPay",
                "PayModeName": "按量计费",
                "ProjectId": "0",
                "ProjectName": "默认项目"
            }
        ],
        "PageSize": 1,
        "PageNo": 1,
        "RecordNum": 29,
        "Ready": 1,
        "RequestId": "59a408bc-5d95-4d40-bf21-58e5e8d48dd0"
    }
}
```


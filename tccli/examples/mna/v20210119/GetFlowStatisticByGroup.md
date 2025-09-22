**Example 1: 根据分组获取用量统计信息**



Input: 

```
tccli mna GetFlowStatisticByGroup --cli-unfold-argument  \
    --GroupId cliGrp-xf8rboasbh \
    --BeginTime 1711296000 \
    --EndTime 1711987200 \
    --Type 1 \
    --TimeGranularity 2 \
    --AccessRegion MC \
    --MpApplicationId mna-w795bzezug \
    --GatewayType 0
```

Output: 
```
{
    "Response": {
        "AvgValue": 154434162.5,
        "MaxValue": 305576473,
        "NetDetails": [
            {
                "Current": 305576473,
                "Time": "1711555200"
            },
            {
                "Current": 3291852,
                "Time": "1711641600"
            }
        ],
        "RequestId": "e5b650a9-d994-439f-9132-3e5c56054903",
        "TotalValue": 308868325
    }
}
```


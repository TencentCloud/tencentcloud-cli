**Example 1: cos概览信息**



Input: 

```
tccli csip DescribeCosOverview --cli-unfold-argument  \
    --Filter.Offset 0 \
    --Filter.Limit 10 \
    --Filter.Order desc \
    --Filter.By CreateTime \
    --Filter.StartTime 2024-01-24 00:00:00 \
    --Filter.EndTime 2024-01-31 23:59:59
```

Output: 
```
{
    "Response": {
        "CosOverview": {
            "AssetCount": 1256,
            "AlarmAssetCount": 89,
            "RiskAssetCount": 34,
            "AlarmCount": 156,
            "IncrementAlarmCount": 12,
            "RiskCount": 67,
            "IncrementRiskCount": 5,
            "RiskTop": [
                {
                    "PolicyType": 1,
                    "PolicyTypeName": "公共读取权限风险",
                    "PolicyCount": 23
                }
            ]
        },
        "RequestId": "6a625df7-dea0-4ba2-9942-97303d13d23e"
    }
}
```


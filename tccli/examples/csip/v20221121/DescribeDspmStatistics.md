**Example 1: cdb测试用例**



Input: 

```
tccli csip DescribeDspmStatistics --cli-unfold-argument  \
    --AssetType cdb
```

Output: 
```
{
    "Response": {
        "AnalyseAssetStatusCount": {
            "AssetTypeCountSet": [
                {
                    "AssetType": "cdb",
                    "CloseCount": 0,
                    "ClosingCount": 0,
                    "OpenCount": 2,
                    "OpeningCount": 0
                }
            ],
            "CloseCount": 0,
            "ClosingCount": 0,
            "OpenCount": 2,
            "OpeningCount": 0
        },
        "AssetCount": {
            "AlarmAssetCount": 2,
            "AssetCount": 2,
            "DangerRiskCount": 0,
            "LowRiskCount": 2,
            "RiskAssetCount": 2
        },
        "IpCount": {
            "IpCount": 2,
            "PrivateIpCount": 2,
            "UnmarkedPublicIpCount": 0
        },
        "RiskCount": {
            "AccountSensitiveOperation": 0,
            "AttackSurfaceRisk": 0,
            "LoginBehaviorAnomaly": 35,
            "NumOfNewAlarmEvent": 5,
            "NumOfNewConfigRisk": 0,
            "PermissionAnomaly": 18,
            "SQLBehaviorAnomaly": 0,
            "UnprocessedAlarm": 35,
            "UnprocessedRisk": 18
        },
        "UserCount": {
            "PersonCount": 2,
            "TotalAccountCount": 4,
            "UinAccountCount": 2
        },
        "RequestId": "7f5e0bef-5349-4ec9-8476-7cf3a3bfff59"
    }
}
```


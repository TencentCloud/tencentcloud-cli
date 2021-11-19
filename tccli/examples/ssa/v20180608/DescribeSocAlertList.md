**Example 1: demo**



Input: 

```
tccli ssa DescribeSocAlertList --cli-unfold-argument  \
    --Filter.0.FilterKey xx \
    --Filter.0.FilterOperatorType 0 \
    --Filter.0.FilterValue xx \
    --PageIndex 0 \
    --Scenes 0 \
    --PageSize 0 \
    --Sorter.0.SortType 0 \
    --Sorter.0.SortKey xx
```

Output: 
```
{
    "Response": {
        "Data": {
            "Total": 0,
            "AlertList": [
                {
                    "AlertId": "xx",
                    "VictimAssetSub": "xx",
                    "Source": "xx",
                    "Concerns": [
                        {
                            "StatisticsCount": 0,
                            "ConcernType": 0,
                            "EntityType": 0,
                            "Concern": "xx"
                        }
                    ],
                    "EventStatus": 0,
                    "AlertName": "xx",
                    "VictimAssetType": "xx",
                    "AssetName": "xx",
                    "Type": "xx",
                    "ConcernVictimCount": 0,
                    "Status": 0,
                    "SubType": "xx",
                    "AssetId": "xx",
                    "AssetPrivateIp": [
                        "xx"
                    ],
                    "EventId": "xx",
                    "Level": 0,
                    "AttackTactic": "xx",
                    "AlertTime": "xx",
                    "Action": 0,
                    "ConcernMaliciousCount": 0,
                    "AssetPublicIp": [
                        "xx"
                    ],
                    "AttackId": "xx",
                    "AttackName": "xx",
                    "AttackResult": 0,
                    "AttackChain": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```


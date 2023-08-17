**Example 1: demo**



Input: 

```
tccli ssa DescribeSocAlertList --cli-unfold-argument  \
    --Filter.0.FilterKey abc \
    --Filter.0.FilterOperatorType 0 \
    --Filter.0.FilterValue abc \
    --Sorter.0.SortKey abc \
    --Sorter.0.SortType 0 \
    --PageSize 0 \
    --PageIndex 0 \
    --Scenes 0 \
    --ExportFlag True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Total": 0,
            "AlertList": [
                {
                    "AlertTime": "abc",
                    "AlertId": "abc",
                    "AssetId": "abc",
                    "AssetPrivateIp": [
                        "abc"
                    ],
                    "AlertName": "abc",
                    "Level": 0,
                    "Type": "abc",
                    "Source": "abc",
                    "AttackChain": "abc",
                    "AttackId": "abc",
                    "Concerns": [
                        {
                            "ConcernType": 0,
                            "EntityType": 0,
                            "Concern": "abc",
                            "StatisticsCount": 0,
                            "IpCountry": "abc",
                            "IpProvince": "abc",
                            "Result": "abc",
                            "Confidence": 0,
                            "IpIsp": "abc",
                            "IpInfrastructure": "abc",
                            "ThreatType": [
                                "abc"
                            ],
                            "Groups": [
                                "abc"
                            ],
                            "Status": "abc",
                            "Tags": [
                                "abc"
                            ],
                            "VictimAssetType": "abc",
                            "VictimAssetName": "abc",
                            "DomainRegistrant": "abc",
                            "DomainRegisteredInstitution": "abc",
                            "DomainRegistrationTime": "abc",
                            "FileName": "abc",
                            "FileMd5": "abc",
                            "VirusName": "abc",
                            "FilePath": "abc",
                            "FileSize": "abc",
                            "ProcName": "abc",
                            "Pid": "abc",
                            "ProcPath": "abc",
                            "ProcUser": "abc",
                            "DefendedCount": 1,
                            "DetectedCount": 1,
                            "SearchData": "abc",
                            "IpCountryIso": "abc",
                            "IpProvinceIso": "abc",
                            "IpCity": "abc",
                            "EventSubType": "abc"
                        }
                    ],
                    "Action": 0,
                    "AttackResult": 0,
                    "EventStatus": 0,
                    "EventId": "abc",
                    "Status": 0,
                    "AssetName": "abc",
                    "ConcernMaliciousCount": 0,
                    "ConcernVictimCount": 0,
                    "VictimAssetType": "abc",
                    "SubType": "abc",
                    "AttackName": "abc",
                    "AssetPublicIp": [
                        "abc"
                    ],
                    "AttackTactic": "abc",
                    "VictimAssetSub": "abc",
                    "VictimAssetVpc": "abc",
                    "Timestamp": "abc",
                    "AssetGroupName": [
                        "abc"
                    ],
                    "AssetProjectName": "abc",
                    "VictimAssetContent": [
                        "abc"
                    ],
                    "WrongReportStatus": 0,
                    "WrongReportConditionId": 0
                }
            ],
            "Aggregations": {
                "Name": "abc",
                "Value": "abc"
            }
        },
        "RequestId": "abc"
    }
}
```


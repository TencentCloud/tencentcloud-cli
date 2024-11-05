**Example 1: 获取告警列表**



Input: 

```
tccli ssa DescribeSocAlertList --cli-unfold-argument  \
    --Filter.0.FilterKey FileMd5 \
    --Filter.0.FilterOperatorType 0 \
    --Filter.0.FilterValue md5ac876*** \
    --Sorter.0.SortKey Level \
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
                    "AlertTime": "2020-10-01 12:12:12",
                    "AlertId": "1",
                    "AssetId": "2",
                    "AssetPrivateIp": [
                        "10.10.10.1"
                    ],
                    "AlertName": "name",
                    "Level": 0,
                    "Type": "cvm",
                    "Source": "cvm",
                    "AttackChain": "/bin/ps",
                    "AttackId": "1",
                    "Concerns": [
                        {
                            "ConcernType": 0,
                            "EntityType": 0,
                            "Concern": "1",
                            "StatisticsCount": 0,
                            "IpCountry": "深圳市",
                            "IpProvince": "广东省",
                            "Result": "1",
                            "Confidence": 0,
                            "IpIsp": "1",
                            "IpInfrastructure": "1",
                            "ThreatType": [],
                            "Groups": [
                                "group1"
                            ],
                            "Status": "1",
                            "Tags": [
                                "tag1"
                            ],
                            "VictimAssetType": "cvm",
                            "VictimAssetName": "name",
                            "DomainRegistrant": "1",
                            "DomainRegisteredInstitution": "1",
                            "DomainRegistrationTime": "1",
                            "FileName": "file-name",
                            "FileMd5": "md5***",
                            "VirusName": "virusname",
                            "FilePath": "/bin/ps",
                            "FileSize": "1560",
                            "ProcName": "ps",
                            "Pid": "5445",
                            "ProcPath": "/bin/ps",
                            "ProcUser": "root",
                            "DefendedCount": 1,
                            "DetectedCount": 1,
                            "SearchData": "search-key",
                            "IpCountryIso": "1",
                            "IpProvinceIso": "1",
                            "IpCity": "深圳市",
                            "EventSubType": "0"
                        }
                    ],
                    "Action": 0,
                    "AttackResult": 0,
                    "EventStatus": 0,
                    "EventId": "1",
                    "Status": 0,
                    "AssetName": "name",
                    "ConcernMaliciousCount": 0,
                    "ConcernVictimCount": 0,
                    "VictimAssetType": "1",
                    "SubType": "1",
                    "AttackName": "attack name",
                    "AssetPublicIp": [
                        "132.x.x.x"
                    ],
                    "AttackTactic": "attack tactic",
                    "VictimAssetSub": "1",
                    "VictimAssetVpc": "vpc",
                    "Timestamp": "1604054472",
                    "AssetGroupName": [
                        "group1"
                    ],
                    "AssetProjectName": "project name",
                    "VictimAssetContent": [
                        "content1"
                    ],
                    "WrongReportStatus": 0,
                    "WrongReportConditionId": 0
                }
            ],
            "Aggregations": {
                "Name": "aggregation name",
                "Value": "value1"
            }
        },
        "RequestId": "f9184c15-9721-456d-8ca0-4263967b5ead"
    }
}
```


**Example 1: 查询场景列表**



Input: 

```
tccli pts DescribeScenarios --cli-unfold-argument  \
    --ScenarioIds scenario-xx
```

Output: 
```
{
    "Response": {
        "RequestId": "abc-123-xyz",
        "ScenarioSet": [
            {
                "AppId": 251008000,
                "Configs": null,
                "CreatedAt": "2024-12-25T11:43:42+08:00",
                "CronId": "",
                "Datasets": [],
                "Description": "",
                "DomainNameConfig": {
                    "DNSConfig": null,
                    "HostAliases": null
                },
                "EncodedScripts": "",
                "Extensions": null,
                "Load": {
                    "GeoRegionsLoadDistribution": [
                        {
                            "Percentage": 80,
                            "Region": "ap-guangzhou",
                            "RegionId": 1
                        },
                        {
                            "Percentage": 20,
                            "Region": "ap-shanghai",
                            "RegionId": 4
                        }
                    ],
                    "LoadSpec": {
                        "Concurrency": {
                            "GracefulStopSeconds": 3,
                            "IterationCount": 0,
                            "MaxRequestsPerSecond": 40,
                            "Resources": 5,
                            "Stages": [
                                {
                                    "DurationSeconds": 60,
                                    "TargetVirtualUsers": 5
                                },
                                {
                                    "DurationSeconds": 0,
                                    "TargetVirtualUsers": 5
                                }
                            ]
                        },
                        "RequestsPerSecond": null,
                        "ScriptOrigin": null
                    },
                    "VpcLoadDistribution": null
                },
                "Name": "pts-js(2024-12-25 11:43:40)",
                "NotificationHooks": null,
                "Owner": "",
                "Plugins": [],
                "ProjectId": "project-1a2b3c4d",
                "ProjectName": "name",
                "Protocols": [],
                "RequestFiles": [],
                "SLAId": "",
                "SLAPolicy": {
                    "AlertChannel": {
                        "AMPConsumerId": "",
                        "NoticeId": ""
                    },
                    "SLARules": []
                },
                "ScenarioId": "scenario-1a2b3c4d",
                "Status": 2,
                "SubAccountUin": "700000200000",
                "TestScripts": [
                    {
                        "EncodedContent": "EncodedContent",
                        "EncodedHttpArchive": "",
                        "FileId": "",
                        "LoadWeight": 100,
                        "Name": "script.js",
                        "Size": 896,
                        "Type": "js",
                        "UpdatedAt": "2024-12-26T10:30:34+08:00"
                    }
                ],
                "Type": "pts-js",
                "Uin": "3510500000",
                "UpdatedAt": "2024-12-26T10:30:57+08:00"
            }
        ],
        "Total": 1
    }
}
```


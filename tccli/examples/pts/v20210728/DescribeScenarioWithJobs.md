**Example 1: 查询场景及对应的job内容**

查询场景及对应的job内容

Input: 

```
tccli pts DescribeScenarioWithJobs --cli-unfold-argument  \
    --ScenarioIds scenario-1a2b3c4d \
    --ScenarioRelatedJobsParams.OrderBy StartTime \
    --ScenarioRelatedJobsParams.Limit 10 \
    --ScenarioRelatedJobsParams.Ascend True
```

Output: 
```
{
    "Response": {
        "RequestId": "abc-123-xyz",
        "ScenarioWithJobsSet": [
            {
                "Scenario": {
                    "AppId": 251201585,
                    "Uin": "700000153395",
                    "SubAccountUin": "700000153395",
                    "CreatedAt": "2021-09-27T10:46:26+08:00",
                    "UpdatedAt": "2021-09-27T10:46:26+08:00",
                    "ScenarioId": "scenario-1a2b3c4d",
                    "Name": "hello",
                    "Type": "pts-js",
                    "Load": {
                        "LoadSpec": {
                            "Concurrency": {
                                "Stages": [
                                    {
                                        "DurationSeconds": 60,
                                        "TargetVirtualUsers": 10
                                    }
                                ],
                                "IterationCount": 5,
                                "MaxRequestsPerSecond": 1000,
                                "GracefulStopSeconds": 3,
                                "Resources": 1
                            },
                            "RequestsPerSecond": null,
                            "ScriptOrigin": null
                        },
                        "VpcLoadDistribution": {
                            "Region": "ap-guangzhou",
                            "RegionId": 1,
                            "VpcId": "1",
                            "SubnetIds": null
                        },
                        "GeoRegionsLoadDistribution": [
                            {
                                "Region": "1",
                                "RegionId": 1,
                                "Percentage": 1
                            }
                        ]
                    },
                    "EncodedScripts": "",
                    "Description": "",
                    "Status": 2,
                    "Configs": [
                        "a.prop"
                    ],
                    "Datasets": null,
                    "Extensions": [
                        "a.jar"
                    ],
                    "ProjectId": "project-1a2b3c4d",
                    "ProjectName": "name",
                    "SLAId": "",
                    "CronId": "",
                    "TestScripts": null,
                    "Protocols": [],
                    "RequestFiles": [],
                    "Plugins": [],
                    "SLAPolicy": {
                        "SLARules": [],
                        "AlertChannel": {
                            "NoticeId": "",
                            "AMPConsumerId": ""
                        }
                    },
                    "DomainNameConfig": {
                        "HostAliases": null,
                        "DNSConfig": null
                    },
                    "NotificationHooks": null,
                    "Owner": ""
                },
                "Jobs": [
                    {
                        "ErrorRate": 0,
                        "RequestTotal": 0,
                        "RequestsPerSecond": 0,
                        "ResponseTimeAverage": 0,
                        "ResponseTimeP99": 0,
                        "ResponseTimeP95": 0,
                        "ResponseTimeP90": 0,
                        "ResponseTimeMax": 0,
                        "ResponseTimeMin": 0,
                        "NetworkReceiveRate": 0,
                        "NetworkSendRate": 0,
                        "JobId": "job-1a2b3c4d",
                        "ProjectId": "project-1a2b3c4d",
                        "ProjectName": "name",
                        "ScenarioId": "scenario-1a2b3c4d",
                        "ScenarioName": "name",
                        "CronId": "",
                        "Type": "pts-js",
                        "Load": {
                            "LoadSpec": {
                                "Concurrency": {
                                    "Stages": [
                                        {
                                            "DurationSeconds": 60,
                                            "TargetVirtualUsers": 10
                                        }
                                    ],
                                    "IterationCount": 5,
                                    "MaxRequestsPerSecond": 1000,
                                    "Resources": 1,
                                    "GracefulStopSeconds": 3
                                },
                                "RequestsPerSecond": null,
                                "ScriptOrigin": null
                            },
                            "VpcLoadDistribution": null,
                            "GeoRegionsLoadDistribution": [
                                {
                                    "Region": "ap-guangzhou",
                                    "RegionId": 1,
                                    "Percentage": 100
                                }
                            ]
                        },
                        "TestScripts": null,
                        "Datasets": null,
                        "Protocols": [],
                        "RequestFiles": [],
                        "Plugins": [],
                        "StartTime": "2021-09-27T10:46:26+08:00",
                        "EndTime": "2021-09-27T10:46:26+08:00",
                        "Note": "",
                        "JobOwner": "owner",
                        "AbortReason": 0,
                        "Status": 12,
                        "Message": "",
                        "DomainNameConfig": {
                            "HostAliases": null,
                            "DNSConfig": null
                        },
                        "Debug": false,
                        "NotificationHooks": null,
                        "Duration": 600,
                        "MaxVirtualUserCount": 1,
                        "MaxRequestsPerSecond": 8,
                        "LoadSourceInfos": null,
                        "CreatedAt": "2021-09-27T10:46:26+08:00",
                        "Configs": null,
                        "Extensions": null,
                        "Scripts": null,
                        "LoadSources": null
                    }
                ]
            }
        ],
        "Total": 1
    }
}
```


**Example 1: 查询任务列表**



Input: 

```
tccli pts DescribeJobs --cli-unfold-argument  \
    --ProjectIds project-xx \
    --OrderBy asc \
    --JobIds job-xx \
    --Ascend True \
    --Limit 0 \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --Offset 0 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --ScenarioIds scenario-xx
```

Output: 
```
{
    "Response": {
        "JobSet": [
            {
                "ErrorRate": 0,
                "RequestTotal": 78,
                "RequestsPerSecond": 3.6055887,
                "ResponseTimeAverage": 0.041749522,
                "ResponseTimeP99": 0.0988,
                "ResponseTimeP95": 0.094,
                "ResponseTimeP90": 0.088,
                "ResponseTimeMax": 0.08245612,
                "ResponseTimeMin": 0.004263497,
                "NetworkReceiveRate": 1842.4558,
                "NetworkSendRate": 773.39874,
                "JobId": "job-1a2b3c4d",
                "ProjectId": "project-1a2b3c4d",
                "ProjectName": "project-name",
                "ScenarioId": "scenario-1a2b3c4d",
                "ScenarioName": "pts-js(2024-08-07 11:40:53)",
                "CronId": "",
                "Type": "pts-js",
                "Load": {
                    "LoadSpec": {
                        "Concurrency": {
                            "Stages": [
                                {
                                    "DurationSeconds": 120,
                                    "TargetVirtualUsers": 2
                                },
                                {
                                    "DurationSeconds": 120,
                                    "TargetVirtualUsers": 4
                                },
                                {
                                    "DurationSeconds": 120,
                                    "TargetVirtualUsers": 5
                                },
                                {
                                    "DurationSeconds": 240,
                                    "TargetVirtualUsers": 5
                                }
                            ],
                            "Resources": 1,
                            "IterationCount": 0,
                            "MaxRequestsPerSecond": 40,
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
                "StartTime": "2024-08-08T14:31:50+08:00",
                "EndTime": "2024-08-08T14:32:12+08:00",
                "Note": "",
                "JobOwner": "job-owner",
                "AbortReason": 1,
                "Status": 16,
                "Message": "用户中断",
                "DomainNameConfig": {
                    "HostAliases": null,
                    "DNSConfig": null
                },
                "Debug": false,
                "NotificationHooks": null,
                "Duration": 600,
                "MaxVirtualUserCount": 5,
                "MaxRequestsPerSecond": 40,
                "LoadSourceInfos": null,
                "CreatedAt": "2024-08-08T14:31:44+08:00",
                "Configs": null,
                "Extensions": null,
                "Scripts": null,
                "LoadSources": null
            }
        ],
        "RequestId": "ae27925c-eb40-47d3-8643-c8c204ab77be",
        "Total": 1
    }
}
```


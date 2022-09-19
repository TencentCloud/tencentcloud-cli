**Example 1: 查询任务列表**



Input: 

```
tccli pts DescribeJobs --cli-unfold-argument  \
    --ProjectIds xx \
    --OrderBy xx \
    --JobIds xx \
    --Ascend True \
    --Limit 0 \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --Offset 0 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --ScenarioIds xx
```

Output: 
```
{
    "Response": {
        "JobSet": [
            {
                "ErrorRate": 0,
                "RequestTotal": 3433,
                "RequestsPerSecond": 5.7235827,
                "ResponseTimeAverage": 0.22972645,
                "ResponseTimeP99": 0.48834386,
                "ResponseTimeP95": 0.26974347,
                "ResponseTimeP90": 0.24264774,
                "ResponseTimeMax": 0.8703224,
                "ResponseTimeMin": 0.2167055,
                "JobId": "job-o5u4k8es",
                "ProjectId": "project-m51m6h0a",
                "ScenarioId": "scenario-piekhfoc",
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
                            "IterationCount": 0,
                            "MaxRequestsPerSecond": 0
                        }
                    },
                    "GeoRegionsLoadDistribution": [
                        {
                            "Region": "ap-guangzhou",
                            "RegionId": 1,
                            "Percentage": 100
                        }
                    ]
                },
                "Scripts": [
                    "script_0.js"
                ],
                "Configs": [],
                "Datasets": [],
                "Extensions": [],
                "StartTime": "2021-11-15T15:54:40+08:00",
                "EndTime": "2021-11-15T16:04:40+08:00",
                "Note": "",
                "JobOwner": "test_env_master",
                "Status": 12,
                "Duration": 600,
                "MaxVirtualUserCount": 5,
                "MaxRequestsPerSecond": 0,
                "LoadSources": [
                    {
                        "PodName": "job-o5u4k8es-p7wh5",
                        "IP": "9.139.1.182",
                        "Region": "ap-guangzhou"
                    }
                ]
            }
        ],
        "RequestId": "xx",
        "Total": 1
    }
}
```


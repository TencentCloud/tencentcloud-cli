**Example 1: 查询场景及对应的job内容**

查询场景及对应的job内容

Input: 

```
tccli pts DescribeScenarioWithJobs --cli-unfold-argument  \
    --ScenarioIds scenario-44dlxys2 \
    --ScenarioRelatedJobsParams.OrderBy StartTime \
    --ScenarioRelatedJobsParams.Limit 10 \
    --ScenarioRelatedJobsParams.Ascend True
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "ScenarioWithJobsSet": [
            {
                "Scenario": {
                    "AppId": 251201585,
                    "Uin": "700000153395",
                    "SubAccountUin": "700000153395",
                    "CreatedAt": "2021-09-27T10:46:26+08:00",
                    "UpdatedAt": "2021-09-27T10:46:26+08:00",
                    "ScenarioId": "scenario-44dlxys2",
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
                                "MaxRequestsPerSecond": 1000
                            }
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
                    "Description": "this is a test",
                    "Status": 2,
                    "Configs": [
                        "a.prop"
                    ],
                    "Datasets": [
                        {
                            "Name": "a.csv",
                            "UpdatedAt": null,
                            "Size": 0,
                            "LineCount": 5,
                            "HeaderInFile": true,
                            "Split": true,
                            "HeaderColumns": null
                        }
                    ],
                    "Extensions": [
                        "a.jar"
                    ],
                    "ProjectId": "1",
                    "SLAId": "",
                    "CronId": ""
                },
                "Jobs": [
                    {
                        "ErrorRate": 0,
                        "RequestTotal": 0,
                        "ResponseTimeAverage": 0,
                        "ResponseTimeP99": 0,
                        "ResponseTimeP95": 0,
                        "ResponseTimeP90": 0,
                        "JobId": "job-j4j0t76k",
                        "ScenarioId": "scenario-44dlxys2",
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
                                    "MaxRequestsPerSecond": 1000
                                }
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
                        "Scripts": [
                            "a.js"
                        ],
                        "Configs": [
                            "a.prop"
                        ],
                        "Datasets": [
                            {
                                "Name": "a.csv",
                                "UpdatedAt": null,
                                "Size": 0,
                                "LineCount": 5,
                                "HeaderInFile": true,
                                "Split": true,
                                "HeaderColumns": null
                            }
                        ],
                        "Extensions": [
                            "a.jar"
                        ],
                        "StartTime": "2021-09-27T13:50:52+08:00",
                        "EndTime": "2021-09-28T14:00:52+08:00",
                        "Note": "",
                        "JobOwner": "lucas",
                        "Status": 5,
                        "Duration": 60,
                        "MaxVirtualUserCount": 10,
                        "MaxRequestsPerSecond": 1000,
                        "LoadSources": null
                    }
                ]
            }
        ],
        "Total": 1
    }
}
```


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
        "Total": 0,
        "ScenarioSet": [
            {
                "Status": 0,
                "Load": {
                    "VpcLoadDistribution": {
                        "VpcId": "xx",
                        "Region": "xx",
                        "RegionId": 0
                    },
                    "GeoRegionsLoadDistribution": [
                        {
                            "Region": "xx",
                            "RegionId": 0,
                            "Percentage": 0
                        }
                    ],
                    "LoadSpec": {
                        "RequestsPerSecond": {
                            "DurationSeconds": 0
                        },
                        "Concurrency": {
                            "Stages": [
                                {
                                    "DurationSeconds": 0,
                                    "TargetVirtualUsers": 0
                                }
                            ],
                            "IterationCount": 0
                        }
                    }
                },
                "Datasets": [
                    {
                        "HeaderInFile": true,
                        "Name": "xx",
                        "LineCount": 0,
                        "Split": true,
                        "UpdatedAt": "2020-09-22T00:00:00+00:00",
                        "HeaderColumns": [
                            "xx"
                        ],
                        "Size": 0
                    }
                ],
                "Description": "xx",
                "SubAccountUin": "xx",
                "Uin": "xx",
                "Extensions": [
                    "xx"
                ],
                "CreatedAt": "xx",
                "AppId": 0,
                "UpdatedAt": "xx",
                "Configs": [
                    "xx"
                ],
                "Type": "xx",
                "Name": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```


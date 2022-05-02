**Example 1: DescribeFiles**



Input: 

```
tccli pts DescribeFiles --cli-unfold-argument  \
    --ProjectIds xx \
    --Offset 0 \
    --FileIds xx \
    --Limit 0 \
    --FileName xx \
    --Kind 1
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "FileSet": [
            {
                "Status": 0,
                "Kind": 0,
                "HeaderInFile": true,
                "Name": "xx",
                "Type": "xx",
                "TailLines": [
                    "xx"
                ],
                "FileInfos": [
                    {
                        "UpdatedAt": "2020-09-22T00:00:00+00:00",
                        "Type": "xx",
                        "Name": "xx",
                        "Size": 0
                    }
                ],
                "LineCount": 0,
                "ScenarioSet": [
                    {
                        "SubAccountUin": "xx",
                        "DomainNameConfig": {
                            "HostAliases": [
                                {
                                    "IP": "xx",
                                    "HostNames": [
                                        "xx"
                                    ]
                                }
                            ],
                            "DNSConfig": {
                                "Nameservers": [
                                    "xx"
                                ]
                            }
                        },
                        "SLAId": "xx",
                        "Type": "xx",
                        "CronId": "xx",
                        "Status": 0,
                        "Description": "xx",
                        "SLAPolicy": {
                            "AlertChannel": {
                                "NoticeId": "xx",
                                "AMPConsumerId": "xx"
                            },
                            "SLARules": [
                                {
                                    "For": "xx",
                                    "Metric": "xx",
                                    "Aggregation": "xx",
                                    "Value": 0.0,
                                    "AbortFlag": true,
                                    "LabelFilter": [
                                        {
                                            "LabelName": "xx",
                                            "LabelValue": "xx"
                                        }
                                    ],
                                    "Condition": "xx"
                                }
                            ]
                        },
                        "AppId": 0,
                        "UpdatedAt": "xx",
                        "Configs": [
                            "xx"
                        ],
                        "Protocols": [
                            {
                                "UpdatedAt": "2020-09-22T00:00:00+00:00",
                                "Type": "xx",
                                "Name": "xx",
                                "Size": 0
                            }
                        ],
                        "Datasets": [
                            {
                                "HeaderInFile": true,
                                "Name": "xx",
                                "TailLines": [
                                    "xx"
                                ],
                                "LineCount": 0,
                                "Split": true,
                                "UpdatedAt": "2020-09-22T00:00:00+00:00",
                                "HeaderColumns": [
                                    "xx"
                                ],
                                "HeadLines": [
                                    "xx"
                                ],
                                "Type": "xx",
                                "Size": 0
                            }
                        ],
                        "Name": "xx",
                        "ScenarioId": "xx",
                        "ProjectId": "xx",
                        "TestScripts": [
                            {
                                "Name": "xx",
                                "EncodedHttpArchive": "xx",
                                "UpdatedAt": "2020-09-22T00:00:00+00:00",
                                "Size": 0,
                                "Type": "xx",
                                "EncodedContent": "xx"
                            }
                        ],
                        "Extensions": [
                            "xx"
                        ],
                        "RequestFiles": [
                            {
                                "UpdatedAt": "2020-09-22T00:00:00+00:00",
                                "Type": "xx",
                                "Name": "xx",
                                "Size": 0
                            }
                        ],
                        "Load": {
                            "VpcLoadDistribution": {
                                "VpcId": "xx",
                                "Region": "xx",
                                "RegionId": 0,
                                "SubnetIds": [
                                    "xx"
                                ]
                            },
                            "GeoRegionsLoadDistribution": [
                                {
                                    "Region": "xx",
                                    "RegionId": 0,
                                    "Percentage": 0
                                }
                            ],
                            "LoadSpec": {
                                "ScriptOrigin": {
                                    "DurationSeconds": 0,
                                    "MachineSpecification": "xx",
                                    "MachineNumber": 0
                                },
                                "RequestsPerSecond": {
                                    "DurationSeconds": 0,
                                    "MaxRequestsPerSecond": 0
                                },
                                "Concurrency": {
                                    "MaxRequestsPerSecond": 0,
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
                        "EncodedScripts": "xx",
                        "Uin": "xx",
                        "CreatedAt": "xx",
                        "Plugins": [
                            {
                                "UpdatedAt": "2020-09-22T00:00:00+00:00",
                                "Type": "xx",
                                "Name": "xx",
                                "Size": 0
                            }
                        ]
                    }
                ],
                "HeaderColumns": [
                    "xx"
                ],
                "HeadLines": [
                    "xx"
                ],
                "FileId": "xx",
                "UpdatedAt": "2020-09-22T00:00:00+00:00",
                "Size": 0
            }
        ],
        "RequestId": "xx"
    }
}
```


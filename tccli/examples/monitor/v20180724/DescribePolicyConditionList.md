**Example 1: Getting basic alarm policy conditions**



Input: 

```
tccli monitor DescribePolicyConditionList --cli-unfold-argument  \
    --Module monitor
```

Output: 
```
{
    "Response": {
        "Conditions": [
            {
                "EventMetrics": null,
                "IsSupportMultiRegion": true,
                "Metrics": [
                    {
                        "ConfigManual": {
                            "CalcType": {
                                "Keys": [
                                    1,
                                    2,
                                    3,
                                    4,
                                    5,
                                    6
                                ],
                                "Need": true
                            },
                            "CalcValue": {
                                "Default": null,
                                "Fixed": null,
                                "Max": "1024.000000",
                                "Min": "0.000000",
                                "Need": true
                            },
                            "ContinueTime": {
                                "Default": null,
                                "Keys": [
                                    60,
                                    120,
                                    180,
                                    240,
                                    300,
                                    600,
                                    900,
                                    1200,
                                    1500
                                ],
                                "Need": true
                            },
                            "Period": {
                                "Default": null,
                                "Keys": [
                                    60,
                                    300
                                ],
                                "Need": true
                            },
                            "PeriodNum": {
                                "Default": null,
                                "Keys": [
                                    1,
                                    2,
                                    3,
                                    4,
                                    5
                                ],
                                "Need": true
                            },
                            "StatType": {
                                "P10": null,
                                "P1800": null,
                                "P300": "max",
                                "P3600": null,
                                "P5": null,
                                "P60": "sum",
                                "P600": null,
                                "P86400": null
                            }
                        },
                        "MetricId": 1837,
                        "MetricShowName": "Number of server ports with exceptions",
                        "MetricUnit": "Piece"
                    }
                ],
                "Name": "Cloud Load Balancer-Server port (others)-Listener level",
                "PolicyViewName": "LB_RS_PORT_STATUS",
                "SortId": 500,
                "SupportDefault": false,
                "SupportRegions": [
                    "bj",
                    "gz",
                    "nj"
                ]
            },
            {
                "EventMetrics": null,
                "IsSupportMultiRegion": true,
                "Metrics": [
                    {
                        "ConfigManual": {
                            "CalcType": {
                                "Keys": [
                                    1,
                                    2,
                                    3,
                                    4,
                                    5,
                                    6
                                ],
                                "Need": true
                            },
                            "CalcValue": {
                                "Default": null,
                                "Fixed": null,
                                "Max": "199.000000",
                                "Min": "10.000000",
                                "Need": true
                            },
                            "ContinueTime": {
                                "Default": null,
                                "Keys": [
                                    60,
                                    120,
                                    180,
                                    240,
                                    300,
                                    600,
                                    900,
                                    1200,
                                    1500
                                ],
                                "Need": true
                            },
                            "Period": {
                                "Default": null,
                                "Keys": [
                                    60,
                                    300
                                ],
                                "Need": true
                            },
                            "PeriodNum": {
                                "Default": null,
                                "Keys": [
                                    1,
                                    2,
                                    3,
                                    4,
                                    5
                                ],
                                "Need": true
                            },
                            "StatType": {
                                "P10": null,
                                "P1800": null,
                                "P300": "min",
                                "P3600": null,
                                "P5": null,
                                "P60": "min",
                                "P600": null,
                                "P86400": null
                            }
                        },
                        "MetricId": 7025,
                        "MetricShowName": "13_shan002_metric01",
                        "MetricUnit": "s"
                    }
                ],
                "Name": "13_shan002_policy",
                "PolicyViewName": "13_shan002_policy",
                "SortId": 500,
                "SupportDefault": true,
                "SupportRegions": [
                    "bj",
                    "gz",
                    "nj"
                ]
            },
            {
                "EventMetrics": null,
                "IsSupportMultiRegion": true,
                "Metrics": [
                    {
                        "ConfigManual": {
                            "CalcType": {
                                "Keys": [
                                    1,
                                    2,
                                    3,
                                    4,
                                    5,
                                    6
                                ],
                                "Need": true
                            },
                            "CalcValue": {
                                "Default": null,
                                "Fixed": null,
                                "Max": "100000000.000000",
                                "Min": "0.000000",
                                "Need": true
                            },
                            "ContinueTime": {
                                "Default": null,
                                "Keys": [
                                    60,
                                    120,
                                    180,
                                    240,
                                    300,
                                    600,
                                    900,
                                    900,
                                    1200,
                                    1500
                                ],
                                "Need": true
                            },
                            "Period": {
                                "Default": null,
                                "Keys": [
                                    300,
                                    60
                                ],
                                "Need": true
                            },
                            "PeriodNum": {
                                "Default": null,
                                "Keys": [
                                    1,
                                    2,
                                    3,
                                    4,
                                    5
                                ],
                                "Need": true
                            },
                            "StatType": {
                                "P10": null,
                                "P1800": null,
                                "P300": "max",
                                "P3600": null,
                                "P5": null,
                                "P60": "max",
                                "P600": null,
                                "P86400": null
                            }
                        },
                        "MetricId": 2580,
                        "MetricShowName": "rtt",
                        "MetricUnit": "us"
                    }
                ],
                "Name": "cluster_status_test0",
                "PolicyViewName": "cluster_status_test0",
                "SortId": 500,
                "SupportDefault": false,
                "SupportRegions": [
                    "bj",
                    "gz",
                    "nj"
                ]
            }
        ]
    }
}
```


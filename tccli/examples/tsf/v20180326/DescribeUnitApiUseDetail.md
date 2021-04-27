**Example 1: 查询网关API监控明细数据**



Input: 

```
tccli tsf DescribeUnitApiUseDetail --cli-unfold-argument  \
    --ApiId api-qabo8xyl \
    --GatewayInstanceId gw-ins-4hkjbwxy \
    --GatewayDeployGroupId gw-e42d597 \
    --GroupId grp-vcgimq3x \
    --Period 60 \
    --Offset 0 \
    --Limit 20 \
    --EndTime '2020-09-22 00:00:00' \
    --StartTime '2020-09-22 00:00:00'
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 20,
            "Content": [
                {
                    "NamespaceId": "ns-123456",
                    "NamespaceName": "ns-test",
                    "SumReqAmount": "8213434",
                    "AvgFailureRate": "82.11",
                    "AvgTimeCost": "10.11",
                    "MetricDataPointMap": {
                        "SumReqAmount": [
                            {
                                "Key": "1615374000000",
                                "Value": null,
                                "Tag": null
                            },
                            {
                                "Key": "1615374060000",
                                "Value": null,
                                "Tag": null
                            }
                        ],
                        "AvgFailureRate": [
                            {
                                "Key": "1615374000000",
                                "Value": null,
                                "Tag": null
                            },
                            {
                                "Key": "1615374060000",
                                "Value": null,
                                "Tag": null
                            }
                        ],
                        "AvgTimeCost": [
                            {
                                "Key": "1615374000000",
                                "Value": null,
                                "Tag": null
                            },
                            {
                                "Key": "1615374060000",
                                "Value": null,
                                "Tag": null
                            }
                        ]
                    },
                    "TopStatusCode": [
                        {
                            "Name": "2xx",
                            "Count": "20000",
                            "Ratio": "0.35565"
                        },
                        {
                            "Name": "4xx",
                            "Count": "18000",
                            "Ratio": "0.28625"
                        }
                    ],
                    "TopTimeCost": [
                        {
                            "Name": "0_50_ms",
                            "Count": "20000",
                            "Ratio": "0.35565"
                        },
                        {
                            "Name": "50_100_ms",
                            "Count": "18000",
                            "Ratio": "0.28625"
                        },
                        {
                            "Name": "100_200_ms",
                            "Count": "13000",
                            "Ratio": "0.28625"
                        },
                        {
                            "Name": "others",
                            "Count": "13000",
                            "Ratio": "0.28625"
                        }
                    ],
                    "Quantile": {
                        "MaxValue": "12.13",
                        "MinValue": "0.32",
                        "FifthPositionValue": "0.26",
                        "NinthPositionValue": "1.32"
                    }
                },
                {
                    "NamespaceId": "ns-1234567",
                    "NamespaceName": "ns-test2",
                    "SumReqAmount": "20",
                    "AvgFailureRate": "11.21",
                    "AvgTimeCost": "20.12",
                    "MetricDataPointMap": {
                        "SumReqAmount": [
                            {
                                "Key": "1615374000000",
                                "Value": null,
                                "Tag": null
                            },
                            {
                                "Key": "1615374060000",
                                "Value": null,
                                "Tag": null
                            }
                        ],
                        "AvgFailureRate": [
                            {
                                "Key": "1615374000000",
                                "Value": null,
                                "Tag": null
                            },
                            {
                                "Key": "1615374060000",
                                "Value": null,
                                "Tag": null
                            }
                        ],
                        "AvgTimeCost": [
                            {
                                "Key": "1615374000000",
                                "Value": null,
                                "Tag": null
                            },
                            {
                                "Key": "1615374060000",
                                "Value": null,
                                "Tag": null
                            }
                        ]
                    },
                    "TopStatusCode": [
                        {
                            "Name": "2xx",
                            "Count": "20000",
                            "Ratio": "0.35565"
                        },
                        {
                            "Name": "4xx",
                            "Count": "18000",
                            "Ratio": "0.28625"
                        }
                    ],
                    "TopTimeCost": [
                        {
                            "Name": "0_50_ms",
                            "Count": "20000",
                            "Ratio": "0.35565"
                        },
                        {
                            "Name": "50_100_ms",
                            "Count": "18000",
                            "Ratio": "0.28625"
                        },
                        {
                            "Name": "100_200_ms",
                            "Count": "13000",
                            "Ratio": "0.28625"
                        },
                        {
                            "Name": "others",
                            "Count": "13000",
                            "Ratio": "0.28625"
                        }
                    ],
                    "Quantile": {
                        "MaxValue": "12.13",
                        "MinValue": "0.32",
                        "FifthPositionValue": "0.26",
                        "NinthPositionValue": "1.32"
                    }
                }
            ]
        },
        "RequestId": "5d996e05507e42d5970cd2e25ed5267a"
    }
}
```


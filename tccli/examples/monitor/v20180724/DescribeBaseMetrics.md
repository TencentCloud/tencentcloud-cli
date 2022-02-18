**Example 1: 获取监控指标列表**

查询基础监控指标的种类。查询到对应的名字空间下面的监控指标类型。

Input: 

```
tccli monitor DescribeBaseMetrics --cli-unfold-argument  \
    --Namespace QCE/CVM \
    --MetricName AccOuttraffic
```

Output: 
```
{
    "Response": {
        "RequestId": "15e8eb48-e445-48b5-97ca-985908e207bb",
        "MetricSet": [
            {
                "Namespace": "QCE/CVM",
                "MetricName": "AccOuttraffic",
                "MetricCName": "外网出流量",
                "MetricEName": "the out traffic",
                "Unit": "MB",
                "UnitCname": "",
                "Period": [
                    10,
                    60,
                    300,
                    3600,
                    86400
                ],
                "Periods": [
                    {
                        "Period": "10",
                        "StatType": [
                            "sum"
                        ]
                    },
                    {
                        "Period": "60",
                        "StatType": [
                            "sum"
                        ]
                    },
                    {
                        "Period": "300",
                        "StatType": [
                            "sum"
                        ]
                    },
                    {
                        "Period": "3600",
                        "StatType": [
                            "sum"
                        ]
                    },
                    {
                        "Period": "86400",
                        "StatType": [
                            "sum"
                        ]
                    }
                ],
                "Dimensions": [
                    {
                        "Dimensions": [
                            "InstanceId"
                        ]
                    }
                ],
                "Meaning": {
                    "En": "",
                    "Zh": "外网网卡的平均每秒出流量"
                }
            }
        ]
    }
}
```

**Example 2: 获取监控指标列表(QCE/CDB)**

查询基础监控指标的种类。查询到对应的名字空间下面的监控指标类型。

Input: 

```
tccli monitor DescribeBaseMetrics --cli-unfold-argument  \
    --Namespace QCE/CDB \
    --MetricName BytesReceived
```

Output: 
```
{
    "Response": {
        "RequestId": "2102703c-a1bb-4f71-9eb8-58cdfb544590",
        "MetricSet": [
            {
                "Namespace": "QCE/CDB",
                "MetricName": "BytesReceived",
                "MetricCName": "",
                "MetricEName": "",
                "Unit": "Bps",
                "UnitCname": "",
                "Period": [
                    60,
                    300,
                    3600,
                    86400
                ],
                "Periods": [
                    {
                        "Period": "60",
                        "StatType": [
                            "max"
                        ]
                    },
                    {
                        "Period": "300",
                        "StatType": [
                            "max"
                        ]
                    },
                    {
                        "Period": "3600",
                        "StatType": [
                            "max"
                        ]
                    },
                    {
                        "Period": "86400",
                        "StatType": [
                            "max"
                        ]
                    }
                ],
                "Dimensions": [
                    {
                        "Dimensions": [
                            "InstanceId",
                            "InstanceType"
                        ]
                    }
                ],
                "Meaning": {
                    "En": "",
                    "Zh": "接受数据量"
                }
            }
        ]
    }
}
```


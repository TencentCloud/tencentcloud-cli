**Example 1: 查询告警指标列表**

查询“云服务器-基础监控”的告警指标列表

Input: 

```
tccli monitor DescribeAlarmMetrics --cli-unfold-argument  \
    --Module monitor \
    --MonitorType MT_QCE \
    --Namespace cvm_device
```

Output: 
```
{
    "Response": {
        "RequestId": "92hg92hj1-2h352h25hj-2h235h",
        "Metrics": [
            {
                "Namespace": "cvm_device",
                "MetricName": "cpu_usage",
                "Description": "CPU使用率",
                "Max": 100,
                "Min": 0,
                "Dimensions": [
                    "InstanceId",
                    "UUID"
                ],
                "Unit": "%",
                "MetricConfig": {
                    "Operator": [
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne"
                    ],
                    "Period": [
                        60,
                        300
                    ],
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ]
                }
            }
        ]
    }
}
```


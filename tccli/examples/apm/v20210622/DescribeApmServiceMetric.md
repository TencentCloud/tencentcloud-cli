**Example 1: 成功获取APM应用指标**

获取APM应用指标

Input: 

```
tccli apm DescribeApmServiceMetric --cli-unfold-argument  \
    --InstanceId apm-eDyXpD6CD
```

Output: 
```
{
    "Response": {
        "ApplicationCount": 1,
        "ErrorCount": 1,
        "Page": 0,
        "PageSize": 0,
        "RequestId": "84d35deb-232e-463e-b2ac-fe49338707a2",
        "ServiceMetricList": [
            {
                "Fields": [
                    {
                        "CompareVal": "0.9%",
                        "CompareVals": null,
                        "Key": "duration_avg",
                        "LastPeriodValue": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": 681.7527368527665
                            }
                        ],
                        "NameCN": "平均响应时间",
                        "NameEN": "Average Response Time",
                        "Unit": "ms",
                        "Value": 688
                    },
                    {
                        "CompareVal": "-1.7%",
                        "CompareVals": null,
                        "Key": "qps",
                        "LastPeriodValue": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": 0.40692708333333333
                            }
                        ],
                        "NameCN": "平均请求量",
                        "NameEN": "Average RPS",
                        "Unit": "qps",
                        "Value": 0.4
                    },
                    {
                        "CompareVal": "-0.3%",
                        "CompareVals": null,
                        "Key": "request_count_sum",
                        "LastPeriodValue": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": 70317
                            }
                        ],
                        "NameCN": "总请求数",
                        "NameEN": "Total Requests",
                        "Unit": "",
                        "Value": 70129
                    },
                    {
                        "CompareVal": "0.0%",
                        "CompareVals": null,
                        "Key": "error_req_rate_avg",
                        "LastPeriodValue": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": 62.81837962370408
                            }
                        ],
                        "NameCN": "平均错误率",
                        "NameEN": "Average Error Rate",
                        "Unit": "%",
                        "Value": 62.8
                    },
                    {
                        "CompareVal": "-4.4%",
                        "CompareVals": null,
                        "Key": "adpdex",
                        "LastPeriodValue": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": 0.7325824480566577
                            }
                        ],
                        "NameCN": "平均 Apdex",
                        "NameEN": "Average Apdex",
                        "Unit": "",
                        "Value": 0.7
                    },
                    {
                        "CompareVal": "0",
                        "CompareVals": null,
                        "Key": "alarm_count",
                        "LastPeriodValue": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": 0
                            }
                        ],
                        "NameCN": "告警数",
                        "NameEN": "Alarm Count",
                        "Unit": "次",
                        "Value": 0
                    },
                    {
                        "CompareVal": "-0.4%",
                        "CompareVals": null,
                        "Key": "error_request_count",
                        "LastPeriodValue": [
                            {
                                "Key": "CompareByYesterday",
                                "Value": 44172
                            }
                        ],
                        "NameCN": "异常数量",
                        "NameEN": "Error Count",
                        "Unit": "个",
                        "Value": 44008
                    },
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "NameCN": "",
                        "NameEN": "",
                        "Unit": "",
                        "Value": 1
                    },
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "critical_vulnerability_count",
                        "LastPeriodValue": null,
                        "NameCN": "",
                        "NameEN": "",
                        "Unit": "",
                        "Value": 0
                    },
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "important_vulnerability_count",
                        "LastPeriodValue": null,
                        "NameCN": "",
                        "NameEN": "",
                        "Unit": "",
                        "Value": 0
                    },
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "vulnerability_count",
                        "LastPeriodValue": null,
                        "NameCN": "",
                        "NameEN": "",
                        "Unit": "",
                        "Value": 0
                    }
                ],
                "ServiceDetail": {
                    "AppID": 250015922,
                    "CreateUIN": "1511340626",
                    "InstanceKey": "apm-eDyXpD6CD",
                    "InstanceName": "",
                    "Region": "ap-guangzhou",
                    "ServiceDescription": "",
                    "ServiceID": "svc-ELHkoErzzc",
                    "ServiceName": "java-order-service",
                    "Tags": []
                },
                "Tags": [
                    {
                        "Key": "service.name",
                        "Value": "java-order-service"
                    },
                    {
                        "Key": "color",
                        "Value": "red"
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "WarningCount": 0,
        "WarningErrorCount": 1
    }
}
```


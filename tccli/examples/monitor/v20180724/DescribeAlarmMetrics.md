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
        "Metrics": [
            {
                "Description": "CPU利用率",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 100,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "CpuUsage",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "%"
            },
            {
                "Description": "基础CPU利用率",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 100,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "BaseCpuUsage",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "%"
            },
            {
                "Description": "内存利用率",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 100,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "MemUsage",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "%"
            },
            {
                "Description": "内存使用量",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 1000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "MemUsed",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "MB"
            },
            {
                "Description": "磁盘利用率",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 100,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "CvmDiskUsage",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "%"
            },
            {
                "Description": "磁盘读流量(适用于i3机型)",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 100000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "DiskReadTraffic",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "KB/s"
            },
            {
                "Description": "磁盘写流量(适用于i3机型)",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 100000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "DiskWriteTraffic",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "KB/s"
            },
            {
                "Description": "磁盘IO等待(适用于i3机型)",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 3600000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "DiskIoAwait",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "毫秒"
            },
            {
                "Description": "内网入包量",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 1000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "LanInpkg",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "个/秒"
            },
            {
                "Description": "内网出包量",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 1000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "LanOutpkg",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "个/秒"
            },
            {
                "Description": "外网入带宽",
                "Dimensions": [
                    "InstanceId"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 10000000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "WanIntraffic",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "Mbps"
            },
            {
                "Description": "外网出带宽",
                "Dimensions": [
                    "InstanceId"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 10000000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "WanOuttraffic",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "Mbps"
            },
            {
                "Description": "外网入包量",
                "Dimensions": [
                    "InstanceId"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 100000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "WanInpkg",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "个/秒"
            },
            {
                "Description": "外网出包量",
                "Dimensions": [
                    "InstanceId"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 100000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "WanOutpkg",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "个/秒"
            },
            {
                "Description": "外网出带宽使用率",
                "Dimensions": [
                    "InstanceId"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 100,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "Outratio",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "%"
            },
            {
                "Description": "TCP连接数",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 10000000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "TcpCurrEstab",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "个"
            },
            {
                "Description": "内网入带宽",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 10000000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "LanIntraffic",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "Mbps"
            },
            {
                "Description": "内网出带宽",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 10000000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "LanOuttraffic",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "Mbps"
            },
            {
                "Description": "CPU一分钟平均负载",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 1000000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "CpuLoadavg",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": ""
            },
            {
                "Description": "CPU五分钟平均负载",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 1000000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "Cpuloadavg5m",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": ""
            },
            {
                "Description": "CPU十五分钟平均负载",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 1000000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "Cpuloadavg15m",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": ""
            },
            {
                "Description": "子机utc时间和ntp时间差值",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 10000000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60
                    ]
                },
                "MetricName": "Timeoffset",
                "Min": -100,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "s"
            },
            {
                "Description": "连接跟踪丢包",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 10000000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "NfctDrop",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "Count"
            },
            {
                "Description": "插入失败",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 10000000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "no_data"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "NfctInsertFail",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "Count"
            },
            {
                "Description": "用户实际使用内存",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 1000000,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "day_increase",
                        "day_decrease",
                        "week_increase",
                        "week_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave",
                        "day_wave",
                        "week_wave"
                    ],
                    "Period": [
                        60,
                        300
                    ]
                },
                "MetricName": "MemTotalUsed",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "MB"
            },
            {
                "Description": "GPU_nvidia_smi命令卡住",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 1,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave"
                    ],
                    "Period": [
                        300
                    ]
                },
                "MetricName": "GpuNvidiaHung",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "None"
            },
            {
                "Description": "Nvidia_fabricmanager服务状态",
                "Dimensions": [
                    "vm_uuid"
                ],
                "IsAdvanced": 0,
                "IsLatenessMetric": 0,
                "IsOpen": 0,
                "Max": 1,
                "MetricConfig": {
                    "ContinuePeriod": [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    "Operator": [
                        "cycle_increase",
                        "cycle_decrease",
                        "gt",
                        "ge",
                        "lt",
                        "le",
                        "eq",
                        "ne",
                        "cycle_wave"
                    ],
                    "Period": [
                        300
                    ]
                },
                "MetricName": "FabricmanagerService",
                "Min": 0,
                "Namespace": "cvm_device",
                "Operators": [],
                "Periods": null,
                "ProductId": 0,
                "Unit": "None"
            }
        ],
        "RequestId": "3e097fc4-5fb5-4105-bdc9-d466e021e83c"
    }
}
```


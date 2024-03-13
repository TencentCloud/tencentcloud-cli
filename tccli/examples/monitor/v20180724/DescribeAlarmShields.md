**Example 1: 获取告警屏蔽规则列表**



Input: 

```
tccli monitor DescribeAlarmShields --cli-unfold-argument  \
    --Name xx \
    --PageSize 1 \
    --Module xx \
    --Field xx \
    --PageNumber 1 \
    --ShieldIds xx \
    --Order xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "RequestId": "fasdfaghash434stsi579ah",
        "Shields": [
            {
                "ShieldId": "Shield-xxxx",
                "Enable": 1,
                "Name": "测试屏蔽",
                "MonitorType": "MT_QCE",
                "MonitorTypeShowName": "云产品监控",
                "NameSpace": "CKAFKA-CONSUMERGROUP-TOPIC",
                "NameSpaceShowName": "消息队列Kafka-ConsumerGroup-Topic",
                "ShieldObject": [
                    "cafka-xxx",
                    "cafka-xxx"
                ],
                "ShieldMetric": [
                    {
                        "Metric": "UnconsumeTopic",
                        "MetricShowName": "取消消费主题"
                    },
                    {
                        "Metric": "MaxOffsetTopic",
                        "MetricShowName": "最大偏移主题"
                    }
                ],
                "ShieldTimeType": "LOOP_SHIELD",
                "StartTime": "36000",
                "EndTime": "72000",
                "LoopStartDate": "1648742400",
                "LoopEndDate": "1649088000",
                "CurrentStatus": "NOT_TRIGGERED"
            }
        ]
    }
}
```

**Example 2: DescribeAlarmShields示例1**



Input: 

```
tccli monitor DescribeAlarmShields --cli-unfold-argument  \
    --Module monitor \
    --PageNumber 1 \
    --Order DESC \
    --PageSize 10 \
    --Field updated_at
```

Output: 
```
{
    "Response": {
        "RequestId": "cc1d43ed-5bc1-4613-bb90-20841e4d1c3f",
        "Shields": [
            {
                "ShieldId": "Shield-vk7mc7s2ol",
                "Enable": 0,
                "Name": "1311",
                "MonitorType": "MT_QCE",
                "MonitorTypeShowName": "Cloud Product Monitoring",
                "NameSpace": "cvm_device",
                "NameSpaceShowName": "云服务器-基础监控",
                "ShieldObject": [
                    "cafka-xxx"
                ],
                "ShieldMetric": [
                    {
                        "Metric": "CpuUsage",
                        "MetricShowName": "CPU利用率"
                    },
                    {
                        "Metric": "CpuUsage",
                        "MetricShowName": "CPU利用率"
                    }
                ],
                "ShieldTimeType": "LOOP_SHIELD",
                "StartTime": 36000,
                "EndTime": 72000,
                "LoopStartDate": 1648742400,
                "LoopEndDate": 1649088000,
                "CurrentStatus": "EXPIRED"
            },
            {
                "ShieldId": "Shield-6se9k4ycel",
                "Enable": 0,
                "Name": "1311",
                "MonitorType": "MT_QCE",
                "MonitorTypeShowName": "Cloud Product Monitoring",
                "NameSpace": "cvm_device",
                "NameSpaceShowName": "云服务器-基础监控",
                "ShieldObject": [
                    "cafka-xxx"
                ],
                "ShieldMetric": [
                    {
                        "Metric": "CpuUsage",
                        "MetricShowName": "CPU利用率"
                    },
                    {
                        "Metric": "CpuUsage",
                        "MetricShowName": "CPU利用率"
                    }
                ],
                "ShieldTimeType": "LOOP_SHIELD",
                "StartTime": 36000,
                "EndTime": 72000,
                "LoopStartDate": 1648742400,
                "LoopEndDate": 1649088000,
                "CurrentStatus": "EXPIRED"
            },
            {
                "ShieldId": "Shield-a5jsrhcj17",
                "Enable": 0,
                "Name": "1311",
                "MonitorType": "MT_QCE",
                "MonitorTypeShowName": "Cloud Product Monitoring",
                "NameSpace": "cvm_device",
                "NameSpaceShowName": "云服务器-基础监控",
                "ShieldObject": [
                    "cafka-xxx"
                ],
                "ShieldMetric": [
                    {
                        "Metric": "CpuUsage",
                        "MetricShowName": "CPU利用率"
                    },
                    {
                        "Metric": "CpuUsage",
                        "MetricShowName": "CPU利用率"
                    }
                ],
                "ShieldTimeType": "LOOP_SHIELD",
                "StartTime": 36000,
                "EndTime": 72000,
                "LoopStartDate": 1648742400,
                "LoopEndDate": 1649088000,
                "CurrentStatus": "EXPIRED"
            },
            {
                "ShieldId": "Shield-rzkg24tedr",
                "Enable": 0,
                "Name": "1311",
                "MonitorType": "MT_QCE",
                "MonitorTypeShowName": "Cloud Product Monitoring",
                "NameSpace": "cvm_device",
                "NameSpaceShowName": "云服务器-基础监控",
                "ShieldObject": [
                    "cafka-xxx"
                ],
                "ShieldMetric": [
                    {
                        "Metric": "CpuUsage",
                        "MetricShowName": "CPU利用率"
                    },
                    {
                        "Metric": "CpuUsage",
                        "MetricShowName": "CPU利用率"
                    }
                ],
                "ShieldTimeType": "LOOP_SHIELD",
                "StartTime": 36000,
                "EndTime": 72000,
                "LoopStartDate": 1648742400,
                "LoopEndDate": 1649088000,
                "CurrentStatus": "EXPIRED"
            }
        ],
        "TotalCount": 4
    }
}
```


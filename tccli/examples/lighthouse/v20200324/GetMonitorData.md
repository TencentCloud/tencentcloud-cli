**Example 1: 拉取单个实例监控数据**



Input: 

```
tccli lighthouse GetMonitorData --cli-unfold-argument  \
    --Namespace QCE/CVM \
    --MetricName CPUUsage \
    --Period 300 \
    --StartTime 2020-04-10T00:00:00+08:00 \
    --EndTime 2020-04-10T00:10:00+08:00 \
    --Instances.0.Dimensions.0.Name InstanceId \
    --Instances.0.Dimensions.0.Value lhins-aglzynfg
```

Output: 
```
{
    "Response": {
        "StartTime": "2020-04-10 00:00:00",
        "EndTime": "2020-04-10 00:10:00",
        "Period": 300,
        "MetricName": "CPUUsage",
        "DataPoints": [
            {
                "Dimensions": [
                    {
                        "Name": "InstanceId",
                        "Value": "lhins-aglzynfg"
                    }
                ],
                "Timestamps": [
                    1586448000,
                    1586448300,
                    1586448600
                ],
                "Values": [
                    0.816,
                    0.883,
                    0.883
                ]
            }
        ],
        "RequestId": "0cbdd8e1-0d0a-45a6-a957-f74acfbe91d9"
    }
}
```

**Example 2: 拉取某个硬盘某段时间内统计周期为 60 秒的 IO 繁忙比率监控数据**



Input: 

```
tccli lighthouse GetMonitorData --cli-unfold-argument  \
    --Namespace QCE/BLOCK_STORAGE \
    --MetricName DiskUtil \
    --Period 300 \
    --StartTime 2020-05-16T20:00:00+08:00 \
    --EndTime 2020-05-16T20:30:00+08:00 \
    --Instances.0.Dimensions.0.Name diskId \
    --Instances.0.Dimensions.0.Value lhdisk-f71kc5bh
```

Output: 
```
{
    "Response": {
        "StartTime": "2020-05-16 20:00:00",
        "EndTime": "2020-05-16 20:30:00",
        "Period": 300,
        "MetricName": "DiskUtil",
        "DataPoints": [
            {
                "Dimensions": [
                    {
                        "Name": "diskId",
                        "Value": "lhdisk-f71kc5bh"
                    }
                ],
                "Timestamps": [
                    1589630400,
                    1589630700,
                    1589631000,
                    1589631300,
                    1589631600,
                    1589631900,
                    1589632200
                ],
                "Values": [
                    0.15,
                    0.148,
                    0.169,
                    0.16,
                    0.11,
                    0.133,
                    0.134
                ]
            }
        ],
        "RequestId": "004714bd-f37b-4a0e-81d5-26d9e0a89281"
    }
}
```

**Example 3: 拉取多个实例某段时间内统计周期为 300 秒的磁盘分区使用率监控数据**



Input: 

```
tccli lighthouse GetMonitorData --cli-unfold-argument  \
    --Namespace QCE/BLOCK_STORAGE \
    --MetricName DiskReadIops \
    --Period 300 \
    --StartTime 2020-04-03T00:00:00+08:00 \
    --EndTime 2020-04-03T00:10:00+08:00 \
    --Instances.0.Dimensions.0.Name InstanceId \
    --Instances.0.Dimensions.0.Value lhins-6ufhphs3 \
    --Instances.1.Dimensions.0.Name InstanceId \
    --Instances.1.Dimensions.0.Value lhins-aglzynfg
```

Output: 
```
{
    "Response": {
        "StartTime": "2020-04-03 00:00:00",
        "EndTime": "2020-04-03 00:10:00",
        "Period": 300,
        "MetricName": "DiskUsage",
        "DataPoints": [
            {
                "Dimensions": [
                    {
                        "Name": "InstanceId",
                        "Value": "lhins-6ufhphs3"
                    },
                    {
                        "Name": "vmUuid",
                        "Value": "b57c4319-f96d-4fc7-9c7a-712478956767"
                    },
                    {
                        "Name": "ProjectId",
                        "Value": "1153379"
                    },
                    {
                        "Name": "DiskName",
                        "Value": "vda1"
                    }
                ],
                "Timestamps": [
                    1585843200,
                    1585843500,
                    1585843800
                ],
                "Values": [
                    38.299,
                    38.28,
                    38.28
                ]
            },
            {
                "Dimensions": [
                    {
                        "Name": "InstanceId",
                        "Value": "lhins-aglzynfg"
                    },
                    {
                        "Name": "vmUuid",
                        "Value": "d83faaa9-8efb-42a0-b0c4-25a8e892858e"
                    },
                    {
                        "Name": "ProjectId",
                        "Value": "1153379"
                    },
                    {
                        "Name": "DiskName",
                        "Value": "vda1"
                    }
                ],
                "Timestamps": [
                    1585843200,
                    1585843500,
                    1585843800
                ],
                "Values": [
                    25.649,
                    25.649,
                    25.559
                ]
            }
        ],
        "RequestId": "33b70a1d-1176-47e9-b764-ed530c5706fe"
    }
}
```


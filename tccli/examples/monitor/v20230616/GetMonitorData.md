**Example 1: 拉取单台云服务器监控数据**

拉取某台云服务器某段时间内统计周期为5分钟的CPU利用率监控数据

Input: 

```
tccli monitor GetMonitorData --cli-unfold-argument  \
    --Namespace QCE/CVM \
    --MetricName CPUUsage \
    --Period 300 \
    --Instances.0.Dimensions.0.Name InstanceId \
    --Instances.0.Dimensions.0.Value ins-j0hk02zo \
    --StartTime 2019-03-24T10:51:23+08:00 \
    --EndTime 2019-03-24T20:51:23+08:00
```

Output: 
```
{
    "Response": {
        "StartTime": "2019-03-24T10:50:00+08:00",
        "EndTime": "2019-03-24T20:50:00+08:00",
        "Period": 300,
        "MetricName": "CPUUsage",
        "DataPoints": [
            {
                "Dimensions": [
                    {
                        "Name": "InstanceId",
                        "Value": "ins-j0hk02zo"
                    }
                ],
                "Timestamps": [
                    1535079000,
                    1535079300,
                    1535079600,
                    1535079900,
                    1535080200,
                    1535080500
                ],
                "Values": [
                    2.566,
                    2.283,
                    6.316,
                    2.816,
                    2.7,
                    2.35
                ]
            }
        ],
        "Msg": "",
        "RequestId": "d96ec542-6547-4af2-91ac-fee85c1b8b85"
    }
}
```

**Example 2: 获取带宽包P99数据**



Input: 

```
tccli monitor GetMonitorData --cli-unfold-argument  \
    --Namespace QCE/BWP \
    --MetricName BWPResourceBandwidthOut \
    --Instances.0.Dimensions.0.Name bandwidthPackageId \
    --Instances.0.Dimensions.0.Value bwp-djhptxvq \
    --Instances.0.Dimensions.1.Name resourceId \
    --Instances.0.Dimensions.1.Value eip-abcd \
    --Expr.Function PERCENTILE \
    --Expr.N 99 \
    --Period 60 \
    --StartTime 2024-12-11T10:57:27+08:00 \
    --EndTime 2024-12-11T11:07:27+08:00
```

Output: 
```
{
    "Response": {
        "RequestId": "34e19559-914f-4730-be56-6d53a13e9764",
        "Msg": "Success",
        "StartTime": "2024-12-11T10:57:27+08:00",
        "EndTime": "2024-12-11T11:07:27+08:00",
        "MetricName": "BWPResourceBandwidthOut",
        "Period": 60,
        "DataPoints": [
            {
                "Dimensions": [
                    {
                        "Name": "u_id",
                        "Value": "eip-abcd"
                    },
                    {
                        "Name": "netgroup",
                        "Value": "bwp-djhptxvq"
                    }
                ],
                "Timestamps": [
                    1733886060
                ],
                "Values": [
                    12139179.200000001
                ]
            }
        ]
    }
}
```


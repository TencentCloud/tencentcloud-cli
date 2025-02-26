**Example 1: 拉取BWP带宽Top5的监控数据**

根据某个netgroup实例，查看一段时间范围内带宽Top5的u_id数据。

Input: 

```
tccli monitor GetTopNMonitorData --cli-unfold-argument  \
    --Namespace QCE/BWP \
    --MetricName Bwpresourcebandwidthin \
    --Period 60 \
    --StartTime 2024-09-05T00:27:00+08:00 \
    --EndTime 2024-09-05T23:27:00+08:00 \
    --N 5 \
    --Instances.0.Dimensions.0.Name netgroup \
    --Instances.0.Dimensions.0.Value -1
```

Output: 
```
{
    "Response": {
        "MetricName": "Bwpresourcebandwidthin",
        "Period": 60,
        "N": 5,
        "OrderedDataPoints": [
            {
                "Dimensions": [
                    {
                        "Name": "appid",
                        "Value": "251236571"
                    },
                    {
                        "Name": "netgroup",
                        "Value": "-1"
                    },
                    {
                        "Name": "u_id",
                        "Value": "eip-3xq5lcpb"
                    }
                ],
                "Timestamp": 1725496200,
                "Value": 19411.2,
                "Order": 1
            },
            {
                "Dimensions": [
                    {
                        "Name": "u_id",
                        "Value": "eip-bhhl5d0l"
                    },
                    {
                        "Name": "appid",
                        "Value": "251236571"
                    },
                    {
                        "Name": "netgroup",
                        "Value": "-1"
                    }
                ],
                "Timestamp": 1725495840,
                "Value": 2224,
                "Order": 2
            },
            {
                "Dimensions": [
                    {
                        "Name": "appid",
                        "Value": "251236571"
                    },
                    {
                        "Name": "netgroup",
                        "Value": "-1"
                    },
                    {
                        "Name": "u_id",
                        "Value": "eip-7mg0n41b"
                    }
                ],
                "Timestamp": 1725496200,
                "Value": 2088,
                "Order": 3
            },
            {
                "Dimensions": [
                    {
                        "Name": "netgroup",
                        "Value": "-1"
                    },
                    {
                        "Name": "u_id",
                        "Value": "eip-r2n5fxfr"
                    },
                    {
                        "Name": "appid",
                        "Value": "251195348"
                    }
                ],
                "Timestamp": 1725495840,
                "Value": 1759.2,
                "Order": 4
            },
            {
                "Dimensions": [
                    {
                        "Name": "netgroup",
                        "Value": "-1"
                    },
                    {
                        "Name": "u_id",
                        "Value": "eip-bl7z49yd"
                    },
                    {
                        "Name": "appid",
                        "Value": "251236571"
                    }
                ],
                "Timestamp": 1725496140,
                "Value": 1568,
                "Order": 5
            }
        ],
        "RequestId": "yql-qqqqqqqqq",
        "Msg": "Success"
    }
}
```


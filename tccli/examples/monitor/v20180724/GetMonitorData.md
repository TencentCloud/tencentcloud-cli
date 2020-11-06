**Example 1: Getting the monitoring data of multiple CVM instances**

This example shows you how to get the monitoring data for the CPU utilization of multiple CVM instances using a statistical period of 5 minutes for a specified length of time.

Input: 

```
tccli monitor GetMonitorData --cli-unfold-argument  \
    --Namespace QCE/CVM \
    --MetricName CPUUsage \
    --Period 300 \
    --StartTime 2018-09-22T19:51:23+08:00 \
    --EndTime 2018-09-22T20:51:23+08:00 \
    --Instances.0.Dimensions.0.Name InstanceId \
    --Instances.0.Dimensions.0.Value ins-j0hk02zo \
    --Instances.1.Dimensions.0.Name InstanceId \
    --Instances.1.Dimensions.0.Value ins-o8vv2w10
```

Output: 
```
{
    "Response": {
        "StartTime": "2018-09-22 19:50:00",
        "EndTime": "2018-09-22 20:50:00",
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
                "Timestamps": [],
                "Values": []
            },
            {
                "Dimensions": [
                    {
                        "Name": "InstanceId",
                        "Value": "ins-o8vv2w10"
                    }
                ],
                "Timestamps": [],
                "Values": []
            }
        ],
        "RequestId": "9ac53ccc-fbab-483d-980b-b763bcc2f83f"
    }
}
```

**Example 2: Getting the monitoring data of a TencentDB instance**

This example shows you how to get the monitoring data for the CPU utilization of one TencentDB instance using a statistical period of 5 minutes for a specified length of time.

Input: 

```
tccli monitor GetMonitorData --cli-unfold-argument  \
    --Namespace QCE/CDB \
    --MetricName SlowQueries \
    --Period 300 \
    --StartTime 2018-09-22T19:23:07+08:00 \
    --EndTime 2018-09-22T20:23:07+08:00 \
    --Instances.0.Dimensions.0.Name InstanceId \
    --Instances.0.Dimensions.0.Value cdb-k5d6z7p0 \
    --Instances.0.Dimensions.1.Name InstanceType \
    --Instances.0.Dimensions.1.Value 2
```

Output: 
```
{
    "Response": {
        "StartTime": "2018-09-22 19:20:00",
        "EndTime": "2018-09-22 20:20:00",
        "Period": 300,
        "MetricName": "SlowQueries",
        "DataPoints": [
            {
                "Dimensions": [
                    {
                        "Name": "InstanceType",
                        "Value": "2"
                    },
                    {
                        "Name": "InstanceId",
                        "Value": "cdb-k5d6z7p0"
                    }
                ],
                "Timestamps": [],
                "Values": []
            }
        ],
        "RequestId": "2bcfe8b7-8ea8-4488-9d17-f1aeb106eecd"
    }
}
```

**Example 3: Getting the monitoring data of a CVM Instance**

This example shows you how to get the monitoring data for the CPU utilization of one CVM instance using a statistical period of 5 minutes for a specified length of time.

Input: 

```
tccli monitor GetMonitorData --cli-unfold-argument  \
    --Namespace QCE/CVM \
    --MetricName CPUUsage \
    --Period 300 \
    --StartTime 2019-03-24T10:51:23+08:00 \
    --EndTime 2019-03-24T20:51:23+08:00 \
    --Instances.0.Dimensions.0.Name InstanceId \
    --Instances.0.Dimensions.0.Value ins-j0hk02zo
```

Output: 
```
{
    "Response": {
        "StartTime": "2019-03-24 10:50:00",
        "EndTime": "2019-03-24 20:50:00",
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
        "RequestId": "d96ec542-6547-4af2-91ac-fee85c1b8b85"
    }
}
```


**Example 1: DescribeInstanceMonitorData**



Input: 

```
tccli cvd DescribeInstanceMonitorData --cli-unfold-argument  \
    --NameSpace QCE/CVM \
    --MetricName CpuUsage \
    --Period 300 \
    --Instances.0.Dimensions.0.Name InstanceId \
    --Instances.0.Dimensions.0.Value cdi-xxxx \
    --StartTime 2018-09-22T19:23:07+08:00 \
    --EndTime 2018-09-22T20:23:07+08:00
```

Output: 
```
{
    "Response": {
        "StartTime": "2018-09-22T19:20:00+08:00",
        "EndTime": "2018-09-22T20:20:00+08:00",
        "Period": 300,
        "MetricName": "CpuUseRate",
        "DataPoints": [
            {
                "Dimensions": [
                    {
                        "Name": "InstanceId",
                        "Value": "cdi-xxxx"
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


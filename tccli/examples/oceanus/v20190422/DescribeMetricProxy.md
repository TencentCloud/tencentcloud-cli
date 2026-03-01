**Example 1: setats集群查找指标信息**

setats集群查找指标信息

Input: 

```
tccli oceanus DescribeMetricProxy --cli-unfold-argument  \
    --Namespace QCE/CVM \
    --MetricName CpuUsage \
    --Period 300 \
    --StartTime 2026-01-27 10:00:29 \
    --EndTime 2026-01-27 11:00:29 \
    --ClusterId cluster-25jtjt3p \
    --MetricType setats \
    --Filters.0.Name InstanceId  \
    --Filters.0.Values ins-09oy8c32
```

Output: 
```
{
    "Response": {
        "AdditionalInfo": "eyJJbnN0YW5jZU1hcCI6eyJpbnMtMDlveThjMzIiOiJzZXRhdHMtd29ya2VyIiwiaW5zLTM2cThlNjlzIjoic2V0YXRzLXdvcmtlciIsImlucy1pb2ZrcDEyZSI6InNldGF0cy1tYW5hZ2VyIiwiaW5zLXA5ZjBhaXVjIjoic2V0YXRzLXdvcmtlciJ9fQ==",
        "DataPoints": [
            {
                "Dimensions": [
                    {
                        "Name": "InstanceId",
                        "Value": "ins-09oy8c32"
                    }
                ]
            }
        ],
        "EndTime": "2026-01-27 11:00:00",
        "MetricName": "CpuUsage",
        "Period": 300,
        "StartTime": "2026-01-27 10:00:00",
        "RequestId": "b9439958-f460-4213-9612-03919a895665"
    }
}
```


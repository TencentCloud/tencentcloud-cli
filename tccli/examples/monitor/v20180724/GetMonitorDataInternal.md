**Example 1: CDB查询**

更多示例详情可以查看GetMonitorData接口

Input: 

```
tccli monitor GetMonitorDataInternal --cli-unfold-argument  \
    --Namespace QCE/CDB \
    --MetricName VolumeRate \
    --Period 60 \
    --StartTime 2023-06-27T20:51:23+08:00 \
    --EndTime 2023-06-27T21:51:23+08:00 \
    --Instances.0.Dimensions.0.Name InstanceId \
    --Instances.0.Dimensions.0.Value cdb-e3zzox6t
```

Output: 
```
{
    "Response": {
        "DataPoints": [
            {
                "Dimensions": [
                    {
                        "Name": "InstanceId",
                        "Value": "cdb-e3zzox6t"
                    }
                ],
                "Timestamps": [],
                "Values": []
            }
        ],
        "EndTime": "2023-06-27T21:51:00+08:00",
        "MetricName": "VolumeRate",
        "Msg": "",
        "Period": 60,
        "RequestId": "37d241fc-3c63-4aaf-92a6-f6f920800647",
        "StartTime": "2023-06-27T20:51:00+08:00"
    }
}
```


**Example 1: GetModelServiceMonitorData**



Input: 

```
tccli wedata GetModelServiceMonitorData --cli-unfold-argument  \
    --MetricName CpuUtil \
    --Period 60 \
    --StartTime 2025-03-17T11:45:44+08:00 \
    --EndTime 2025-03-18T11:45:44+08:00 \
    --ServiceId aaabbbcccc
```

Output: 
```
{
    "Response": {
        "Data": {
            "StartTime": "2025-03-17T11:45:00+08:00",
            "EndTime": "2025-03-18T11:45:00+08:00",
            "Period": 60,
            "MetricName": "CpuUtil",
            "DataPoints": [
                {
                    "Dimensions": [
                        {
                            "Name": "ServiceId",
                            "Value": "ms-hpwcpdvr-1"
                        }
                    ],
                    "Timestamps": [
                        "1742183100"
                    ],
                    "Values": [
                        0.16,
                        0.163,
                        0.162,
                        0.159
                    ]
                }
            ],
            "Msg": ""
        },
        "RequestId": "79429668-3a87-41d9-9db4-f353cb12919b"
    }
}
```


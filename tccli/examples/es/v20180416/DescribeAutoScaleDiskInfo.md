**Example 1: demo**



Input: 

```
tccli es DescribeAutoScaleDiskInfo --cli-unfold-argument  \
    --InstanceId es-xxx
```

Output: 
```
{
    "Response": {
        "AutoScaleDiskInfoList": [
            {
                "NodeType": "hotData",
                "ScaleType": 0,
                "Threshold": 80,
                "Duration": 60,
                "PercentSize": 20,
                "FixSize": 0,
                "MaxSize": 500
            },
            {
                "NodeType": "WarmData",
                "ScaleType": 1,
                "Threshold": 0,
                "Duration": 90,
                "PercentSize": 0,
                "FixSize": 100,
                "MaxSize": 1000
            }
        ],
        "Status": 1,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```


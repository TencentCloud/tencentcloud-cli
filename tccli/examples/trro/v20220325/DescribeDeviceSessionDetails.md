**Example 1: 示例1**



Input: 

```
tccli trro DescribeDeviceSessionDetails --cli-unfold-argument  \
    --SessionId abcde-50f7-4c60-9c89-e7076c8529a9-0
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "MemUsed": [
                    0.0
                ],
                "Fps": [
                    0
                ],
                "Lost": [
                    0.0
                ],
                "NetworkLatency": [
                    0
                ],
                "Rate": [
                    0
                ],
                "SessionId": "xx",
                "DeviceType": "xx",
                "StartTime": 1,
                "TimeOffset": [
                    1
                ],
                "SdkMode": "xx",
                "EndTime": 1,
                "CpuUsed": [
                    0.0
                ],
                "VideoLatency": [
                    0
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```


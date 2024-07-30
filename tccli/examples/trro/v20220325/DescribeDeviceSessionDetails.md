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
                "DeviceType": "abc",
                "StartTime": 1,
                "EndTime": 1,
                "SessionId": "abc",
                "Rate": [
                    0
                ],
                "Fps": [
                    0
                ],
                "Lost": [
                    0
                ],
                "NetworkLatency": [
                    0
                ],
                "VideoLatency": [
                    0
                ],
                "CpuUsed": [
                    0
                ],
                "MemUsed": [
                    0
                ],
                "TimeOffset": [
                    1
                ],
                "ProjectId": "abc",
                "DeviceId": "abc",
                "Ver": "abc",
                "SdkMode": "abc",
                "DecodeCost": [
                    0
                ],
                "RenderConst": [
                    0
                ],
                "K100": [
                    0
                ],
                "K150": [
                    0
                ],
                "NACK": [
                    0
                ],
                "BitRateEstimate": [
                    0
                ],
                "Width": 0,
                "Height": 0,
                "EncodeCost": [
                    0
                ],
                "CaptureCost": [
                    0
                ],
                "RenderCost": [
                    0
                ],
                "ConfigWidth": 0,
                "ConfigHeight": 0,
                "FrameDelta": [
                    0
                ],
                "MaxFrameDelta": [
                    0
                ],
                "TotalBitrateEstimate": [
                    0
                ],
                "Lag100Duration": [
                    0
                ],
                "Lag150Duration": [
                    0
                ],
                "MultiMode": 0,
                "MultiNet": [
                    {
                        "NetId": 0,
                        "NetIp": "abc",
                        "Rtt": [
                            0
                        ],
                        "Lost": [
                            0
                        ],
                        "SendBps": [
                            0
                        ],
                        "RecvBps": [
                            0
                        ]
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```


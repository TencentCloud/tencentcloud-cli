**Example 1: 请求示例**



Input: 

```
tccli mps DescribeStreamLinkFlowMediaStatistics --cli-unfold-argument  \
    --FlowId 0175723949ba0956b92d0bf40cfe \
    --StartTime 2020-12-10T11:00:00Z \
    --EndTime 2020-12-10T12:00:00Z \
    --Period 1min \
    --Type input \
    --Pipeline 0 \
    --InputOutputId 0175723949bb0956b92d0bf40cff
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "Network": 1208588,
                "Timestamp": 1607598000,
                "SessionId": "xx",
                "Video": [
                    {
                        "Rate": 1038884,
                        "Pid": 256,
                        "SessionId": "xx",
                        "Fps": 62
                    }
                ],
                "ClientIp": "xx",
                "Audio": [
                    {
                        "Rate": 169704,
                        "Pid": 257,
                        "SessionId": "xx",
                        "Fps": 45
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```


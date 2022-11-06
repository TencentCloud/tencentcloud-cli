**Example 1: 请求示例**



Input: 

```
tccli mps DescribeStreamLinkFlowStatistics --cli-unfold-argument  \
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
                "Timestamp": 1610953200,
                "FlowStatistics": [
                    {
                        "SessionId": "562328572",
                        "ClientIp": "134.175.180.167",
                        "Network": 1748053,
                        "Video": [
                            {
                                "Fps": 17,
                                "Rate": 1458950,
                                "Pid": 256
                            }
                        ],
                        "Audio": [
                            {
                                "Fps": 28,
                                "Rate": 114462,
                                "Pid": 257
                            },
                            {
                                "Fps": 30,
                                "Rate": 116787,
                                "Pid": 258
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "4d9bcf8e-32c5-49ed-b145-875ad65c3d46"
    }
}
```


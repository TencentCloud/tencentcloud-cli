**Example 1: 请求示例**



Input: 

```
tccli mps DescribeStreamLinkFlowRealtimeStatus --cli-unfold-argument  \
    --FlowId 0176ac7f1af20956b92d2aad1e6d \
    --InputIds 0176ac7f1af30956b92d2aad1e6e \
    --OutputIds 0178c3f4bceb0956b92d149e1b5d
```

Output: 
```
{
    "Response": {
        "Timestamp": 1618543864,
        "RequestId": "xx",
        "Datas": [
            {
                "Protocol": "xx",
                "ConnectServerIP": "xx",
                "RTMPStatus": [
                    {}
                ],
                "OutputId": "xx",
                "FlowId": "xx",
                "InputId": "xx",
                "CommonStatus": {
                    "State": "xx",
                    "Reconnections": 0,
                    "Bitrate": 0,
                    "Mode": "xx",
                    "ConnectedTime": 0
                },
                "SRTStatus": [
                    {}
                ],
                "Type": "xx",
                "RTPStatus": {
                    "Packets": 0
                }
            },
            {
                "Protocol": "xx",
                "ConnectServerIP": "xx",
                "RTMPStatus": [
                    {}
                ],
                "OutputId": "xx",
                "FlowId": "xx",
                "InputId": "xx",
                "CommonStatus": {
                    "State": "xx",
                    "Reconnections": 0,
                    "Bitrate": 0,
                    "Mode": "xx",
                    "ConnectedTime": 0
                },
                "SRTStatus": [
                    {}
                ],
                "Type": "xx",
                "RTPStatus": {
                    "Packets": 0
                }
            }
        ]
    }
}
```


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
        "RequestId": "01937702c54509dc0f3269ca341f",
        "Datas": [
            {
                "Protocol": "SRT",
                "Type": "Input",
                "ConnectServerIP": "233.35.69.89",
                "OutputId": "019202e96d9f09dc0f325e7f7a2a",
                "FlowId": "019377034b0709dc0f3269ca3422",
                "InputId": "0193d38d0a4f09dc0f326fd4342c",
                "SRTStatus": {
                    "PacketLossRate": 0.0,
                    "DroppedPackets": 0,
                    "Latency": 120,
                    "Encryption": "Off",
                    "RetransmitRate": 0.0,
                    "Packets": 0,
                    "RTT": 20
                },
                "CommonStatus": {
                    "State": "Connected",
                    "Reconnections": 10,
                    "Bitrate": 0,
                    "Mode": "Listener",
                    "ConnectedTime": 36000
                },
                "RTMPStatus": {
                    "VideoFPS": 0,
                    "AudioFPS": 0
                },
                "RTPStatus": {
                    "Packets": 0
                }
            }
        ]
    }
}
```


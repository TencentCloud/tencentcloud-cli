**Example 1: 请求示例**



Input: 

```
tccli mps ModifyStreamLinkOutputInfo --cli-unfold-argument  \
    --FlowId 019202e96d9f09dc0f325e7f7a2a \
    --Output.OutputId 01937702c54509dc0f3269ca341f \
    --Output.OutputName output_name \
    --Output.OutputType Internet \
    --Output.Description description \
    --Output.Protocol SRT \
    --Output.SRTSettings.Destinations.0.Ip 102.32.56.23 \
    --Output.SRTSettings.Destinations.0.Port 22300 \
    --Output.SRTSettings.StreamId  \
    --Output.SRTSettings.Latency 0 \
    --Output.SRTSettings.RecvLatency 0 \
    --Output.SRTSettings.PeerLatency 0 \
    --Output.SRTSettings.PeerIdleTimeout 0 \
    --Output.SRTSettings.Passphrase  \
    --Output.SRTSettings.PbKeyLen 0 \
    --Output.SRTSettings.Mode Caller \
    --Output.RTPSettings.Destinations.0.Ip 102.32.56.23 \
    --Output.RTPSettings.Destinations.0.Port 22300 \
    --Output.RTPSettings.FEC off \
    --Output.RTPSettings.IdleTimeout 0 \
    --Output.RTMPSettings.ChunkSize 0 \
    --Output.RTMPSettings.Destinations.0.Url rtmp://example.com/live \
    --Output.RTMPSettings.Destinations.0.StreamKey live_test \
    --Output.AllowIpList 0.0.0.0 \
    --Output.MaxConcurrent 1
```

Output: 
```
{
    "Response": {
        "Info": {
            "OutputId": "01937702c54509dc0f3269ca341f",
            "OutputRegion": "ap-shanghai",
            "OutputName": "output_name",
            "OutputType": "Internet",
            "Description": "description",
            "Protocol": "SRT",
            "OutputAddressList": [
                {
                    "Ip": "102.32.56.23"
                }
            ],
            "SRTSettings": {
                "Destinations": [
                    {
                        "Ip": "102.32.56.23",
                        "Port": 22300
                    }
                ],
                "StreamId": "",
                "Latency": 0,
                "RecvLatency": 0,
                "PeerLatency": 0,
                "PeerIdleTimeout": 0,
                "Passphrase": "",
                "PbKeyLen": 0,
                "Mode": "Caller",
                "SourceAddresses": [
                    {
                        "Ip": "102.32.56.23",
                        "Port": 22300
                    }
                ]
            },
            "RTPSettings": {
                "Destinations": [
                    {
                        "Ip": "102.32.56.23",
                        "Port": 22300
                    }
                ],
                "FEC": "off",
                "IdleTimeout": 0
            },
            "RTMPSettings": {
                "IdleTimeout": 0,
                "ChunkSize": 0,
                "Destinations": [
                    {
                        "Url": "rtmp://example.com/live",
                        "StreamKey": "live_test"
                    }
                ]
            },
            "RTMPPullSettings": {
                "ServerUrls": [
                    {
                        "TcUrl": "rtmp://example.com/live",
                        "StreamKey": "live_test"
                    }
                ]
            },
            "AllowIpList": [
                "0.0.0.0"
            ],
            "RTSPPullSettings": {
                "ServerUrls": [
                    {
                        "Url": "rtsp://example.com/live/test"
                    }
                ]
            },
            "HLSPullSettings": {
                "ServerUrls": [
                    {
                        "Url": "http://example.com/live/test.m3u8"
                    }
                ]
            },
            "MaxConcurrent": 1
        },
        "RequestId": "01937702ecc509dc0f3269ca3420"
    }
}
```


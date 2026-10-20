**Example 1: 请求示例**

创建媒体传输的输入配置。

Input: 

```
tccli mps CreateStreamLinkInput --cli-unfold-argument  \
    --FlowId  \
    --InputGroup.0.InputName inputname \
    --InputGroup.0.Description inputnameDescription \
    --InputGroup.0.Protocol RTP \
    --InputGroup.0.AllowIpList 0.0.0.0/0 \
    --InputGroup.0.SRTSettings.StreamId #!::u=johnny,t=file,m=publish,r=results.csv \
    --InputGroup.0.SRTSettings.Latency 1000 \
    --InputGroup.0.SRTSettings.RecvLatency 1000 \
    --InputGroup.0.SRTSettings.PeerLatency 1000 \
    --InputGroup.0.SRTSettings.PeerIdleTimeout 1000 \
    --InputGroup.0.SRTSettings.Passphrase  \
    --InputGroup.0.SRTSettings.PbKeyLen 10 \
    --InputGroup.0.RTPSettings.FEC none \
    --InputGroup.0.RTPSettings.IdleTimeout 1000
```

Output: 
```
{
    "Response": {
        "Info": {
            "FlowId": "01937702ecc509dc0f3269ca3420",
            "FlowName": "live-srt-shanghai",
            "State": "RUNNING",
            "MaxBandwidth": 20000000,
            "InputGroup": [
                {
                    "InputId": "019377034b0709dc0f3269ca3422",
                    "InputName": "srt-input-shanghai",
                    "Description": "上海 SRT 推流输入",
                    "Protocol": "SRT",
                    "InputAddressList": [
                        {
                            "Ip": "1.1.1.1",
                            "Port": 9000
                        }
                    ],
                    "AllowIpList": [
                        "1.1.1.1"
                    ],
                    "SRTSettings": {
                        "Mode": "LISTENER",
                        "StreamId": "#!::r=live/stream1,m=publish",
                        "Latency": 120,
                        "RecvLatency": 120,
                        "PeerLatency": 120,
                        "PeerIdleTimeout": 5000,
                        "Passphrase": "0123456789abcdef",
                        "PbKeyLen": 16,
                        "SourceAddresses": [
                            {
                                "Ip": "1.1.1.1",
                                "Port": 9000
                            }
                        ]
                    },
                    "RTPSettings": {
                        "FEC": "NONE",
                        "IdleTimeout": 5000
                    },
                    "InputRegion": "ap-shanghai",
                    "RTMPSettings": {
                        "AppName": "live",
                        "StreamKey": "stream1"
                    },
                    "FailOver": "ENABLE",
                    "Zones": [
                        "ap-shanghai-2"
                    ],
                    "RTMPPullSettings": {
                        "SourceAddresses": [
                            {
                                "TcUrl": "rtmp://1.1.1.1/live",
                                "StreamKey": "stream1"
                            }
                        ]
                    },
                    "RTSPPullSettings": {
                        "SourceAddresses": [
                            {
                                "Url": "rtsp://1.1.1.1:554/live/stream1"
                            }
                        ]
                    },
                    "HLSPullSettings": {
                        "SourceAddresses": [
                            {
                                "Url": "https://origin.example.com/live/stream1/index.m3u8"
                            }
                        ]
                    },
                    "ResilientStream": {
                        "Enable": true,
                        "BufferTime": 1000
                    },
                    "SecurityGroupIds": [
                        "sg-1a2b3c4d"
                    ]
                }
            ],
            "OutputGroup": [
                {
                    "OutputId": "019377034c0709dc0f3269ca3430",
                    "OutputName": "srt-output-beijing",
                    "OutputType": "SRT",
                    "Description": "北京 SRT 拉流输出",
                    "Protocol": "SRT",
                    "OutputAddressList": [
                        {
                            "Ip": "1.1.1.1"
                        }
                    ],
                    "OutputRegion": "ap-beijing",
                    "SRTSettings": {
                        "Destinations": [
                            {
                                "Ip": "1.1.1.1",
                                "Port": 10080
                            }
                        ],
                        "StreamId": "#!::r=live/stream1,m=request",
                        "Latency": 120,
                        "RecvLatency": 120,
                        "PeerLatency": 120,
                        "PeerIdleTimeout": 5000,
                        "Passphrase": "0123456789abcdef",
                        "PbKeyLen": 16,
                        "Mode": "LISTENER",
                        "SourceAddresses": [
                            {
                                "Ip": "1.1.1.1",
                                "Port": 9000
                            }
                        ]
                    },
                    "RTPSettings": {
                        "Destinations": [
                            {
                                "Ip": "1.1.1.1",
                                "Port": 5004
                            }
                        ],
                        "FEC": "NONE",
                        "IdleTimeout": 5000
                    },
                    "RTMPSettings": {
                        "IdleTimeout": 3000,
                        "ChunkSize": 4096,
                        "Destinations": [
                            {
                                "Url": "rtmp://1.1.1.1/live",
                                "StreamKey": "stream1"
                            }
                        ]
                    },
                    "RTMPPullSettings": {
                        "ServerUrls": [
                            {
                                "TcUrl": "rtmp://1.1.1.1/live",
                                "StreamKey": "stream1"
                            }
                        ]
                    },
                    "AllowIpList": [
                        "1.1.1.1"
                    ],
                    "RTSPPullSettings": {
                        "ServerUrls": [
                            {
                                "Url": "rtsp://1.1.1.1:554/live/stream1"
                            }
                        ]
                    },
                    "HLSPullSettings": {
                        "ServerUrls": [
                            {
                                "Url": "https://origin.example.com/live/stream1/index.m3u8"
                            }
                        ]
                    },
                    "MaxConcurrent": 5,
                    "SecurityGroupIds": [
                        "sg-1a2b3c4d"
                    ],
                    "Zones": [
                        "ap-beijing-1"
                    ]
                }
            ],
            "EventId": "0193770a00009dc0f3269ca3439",
            "Region": "ap-shanghai"
        },
        "RequestId": "3c140219-cfe9-4a60-af06-3ee6e0a1e5f1"
    }
}
```


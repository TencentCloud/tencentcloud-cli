**Example 1: 请求示例**

创建媒体传输流

Input: 

```
tccli mps CreateStreamLinkFlow --cli-unfold-argument  \
    --FlowName flowtest \
    --EventId 01937702ecc509dc0f3269ca3420 \
    --MaxBandwidth 20000000 \
    --InputGroup.0.InputName inputname \
    --InputGroup.0.Description inputnameDescription \
    --InputGroup.0.Protocol RTP \
    --InputGroup.0.AllowIpList 0.0.0.0/0 \
    --InputGroup.0.SRTSettings.StreamId #!::u=johnny,r=resource,h=xxx.com,t=stream,m=play \
    --InputGroup.0.SRTSettings.Latency 1000 \
    --InputGroup.0.SRTSettings.RecvLatency 1000 \
    --InputGroup.0.SRTSettings.PeerLatency 1000 \
    --InputGroup.0.SRTSettings.PeerIdleTimeout 1000 \
    --InputGroup.0.SRTSettings.Passphrase passphrase \
    --InputGroup.0.SRTSettings.PbKeyLen 10 \
    --InputGroup.0.HLSPullSettings.SourceAddresses.0.Url http://example.com:8806/live/streamname.m3u8 \
    --InputGroup.0.RTPSettings.FEC none \
    --InputGroup.0.RTPSettings.IdleTimeout 1000
```

Output: 
```
{
    "Response": {
        "Info": {
            "FlowId": "flowtest",
            "FlowName": "flowtest",
            "State": "IDLE",
            "MaxBandwidth": 0,
            "InputGroup": [
                {
                    "InputId": "inputtest",
                    "InputName": "inputtest",
                    "Description": "inputtest",
                    "Protocol": "SRT",
                    "InputAddressList": [],
                    "AllowIpList": [
                        "0.0.0.0/0"
                    ],
                    "SRTSettings": {
                        "Mode": "LISTENER",
                        "StreamId": "srttest",
                        "Latency": 0,
                        "RecvLatency": 0,
                        "PeerLatency": 0,
                        "PeerIdleTimeout": 0,
                        "Passphrase": "srttest",
                        "PbKeyLen": 0,
                        "SourceAddresses": [
                            {
                                "Ip": "227.0.0.101",
                                "Port": 0
                            }
                        ]
                    },
                    "RTPSettings": {
                        "FEC": "rtptest",
                        "IdleTimeout": 0
                    },
                    "InputRegion": "ap-shanghai",
                    "RTMPSettings": {
                        "AppName": "live",
                        "StreamKey": "live_test"
                    },
                    "FailOver": "on",
                    "RTMPPullSettings": {
                        "SourceAddresses": [
                            {
                                "TcUrl": "rtmp://example.com/live",
                                "StreamKey": "live_test"
                            }
                        ]
                    },
                    "RTSPPullSettings": {
                        "SourceAddresses": [
                            {
                                "Url": "rtsp://120.10.10.10:2355/cam/test"
                            }
                        ]
                    },
                    "ResilientStream": {
                        "Enable": true,
                        "BufferTime": 1
                    },
                    "HLSPullSettings": {
                        "SourceAddresses": [
                            {
                                "Url": "http://example.com/live/index.m3u8"
                            }
                        ]
                    }
                }
            ],
            "OutputGroup": [
                {
                    "OutputId": "outputtest",
                    "OutputName": "outputtest",
                    "OutputType": "outputtest",
                    "Description": "outputtest",
                    "Protocol": "outputtest",
                    "OutputAddressList": [
                        {
                            "Ip": "223.223.223.223"
                        }
                    ],
                    "OutputRegion": "ap-shanghai",
                    "SRTSettings": {
                        "Destinations": [
                            {
                                "Ip": "223.223.223.223",
                                "Port": 0
                            }
                        ],
                        "StreamId": "outputtest",
                        "Latency": 0,
                        "RecvLatency": 0,
                        "PeerLatency": 0,
                        "PeerIdleTimeout": 0,
                        "Passphrase": "outputtest",
                        "PbKeyLen": 0,
                        "Mode": "outputtest",
                        "SourceAddresses": [
                            {
                                "Ip": "202.118.80.23",
                                "Port": 3320
                            }
                        ]
                    },
                    "RTPSettings": {
                        "Destinations": [
                            {
                                "Ip": "202.118.80.23",
                                "Port": 2200
                            }
                        ],
                        "FEC": "outputtest",
                        "IdleTimeout": 0
                    },
                    "RTMPSettings": {
                        "IdleTimeout": 0,
                        "ChunkSize": 0,
                        "Destinations": [
                            {
                                "Url": "outputtest",
                                "StreamKey": "outputtest"
                            }
                        ]
                    },
                    "RTMPPullSettings": {
                        "ServerUrls": [
                            {
                                "TcUrl": "outputtest",
                                "StreamKey": "outputtest"
                            }
                        ]
                    },
                    "AllowIpList": [
                        "223.223.223.223"
                    ],
                    "RTSPPullSettings": {
                        "ServerUrls": [
                            {
                                "Url": "rtsp://120.10.10.10:2355/cam/test"
                            }
                        ]
                    },
                    "HLSPullSettings": {
                        "ServerUrls": [
                            {
                                "Url": "http://example.com/live/index.m3u8"
                            }
                        ]
                    },
                    "MaxConcurrent": 1
                }
            ],
            "EventId": "01937702ecc509dc0f3269ca3420",
            "Region": "ap-shanghai"
        },
        "RequestId": "0186e91bf25809831f1703c66937"
    }
}
```


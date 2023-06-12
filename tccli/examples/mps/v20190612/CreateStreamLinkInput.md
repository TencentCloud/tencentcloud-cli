**Example 1: 请求示例**

创建媒体传输的输入配置。

Input: 

```
tccli mps CreateStreamLinkInput --cli-unfold-argument  \
    --FlowId aaa \
    --InputGroup.0.InputName inputname \
    --InputGroup.0.Description inputnameDescription \
    --InputGroup.0.Protocol RTP \
    --InputGroup.0.AllowIpList 0.0.0.0/0 \
    --InputGroup.0.SRTSettings.StreamId #!::u=johnny,t=file,m=publish,r=results.csv \
    --InputGroup.0.SRTSettings.Latency 1000 \
    --InputGroup.0.SRTSettings.RecvLatency 1000 \
    --InputGroup.0.SRTSettings.PeerLatency 1000 \
    --InputGroup.0.SRTSettings.PeerIdleTimeout 1000 \
    --InputGroup.0.SRTSettings.Passphrase aaa \
    --InputGroup.0.SRTSettings.PbKeyLen 10 \
    --InputGroup.0.RTPSettings.FEC none \
    --InputGroup.0.RTPSettings.IdleTimeout 1000
```

Output: 
```
{
    "Response": {
        "Info": {
            "FlowId": "abc",
            "FlowName": "abc",
            "State": "abc",
            "MaxBandwidth": 0,
            "InputGroup": [
                {
                    "InputId": "abc",
                    "InputName": "abc",
                    "Description": "abc",
                    "Protocol": "abc",
                    "InputAddressList": [
                        {
                            "Ip": "abc",
                            "Port": 0
                        }
                    ],
                    "AllowIpList": [
                        "abc"
                    ],
                    "SRTSettings": {
                        "Mode": "abc",
                        "StreamId": "abc",
                        "Latency": 0,
                        "RecvLatency": 0,
                        "PeerLatency": 0,
                        "PeerIdleTimeout": 0,
                        "Passphrase": "abc",
                        "PbKeyLen": 0,
                        "SourceAddresses": [
                            {
                                "Ip": "abc",
                                "Port": 0
                            }
                        ]
                    },
                    "RTPSettings": {
                        "FEC": "abc",
                        "IdleTimeout": 0
                    },
                    "InputRegion": "abc",
                    "RTMPSettings": {
                        "AppName": "abc",
                        "StreamKey": "abc"
                    },
                    "FailOver": "abc",
                    "RTMPPullSettings": {
                        "SourceAddresses": [
                            {
                                "TcUrl": "abc",
                                "StreamKey": "abc"
                            }
                        ]
                    },
                    "RTSPPullSettings": {
                        "SourceAddresses": [
                            {
                                "Url": "abc"
                            }
                        ]
                    },
                    "HLSPullSettings": {
                        "SourceAddresses": [
                            {
                                "Url": "abc"
                            }
                        ]
                    },
                    "ResilientStream": {
                        "Enable": true,
                        "BufferTime": 1
                    }
                }
            ],
            "OutputGroup": [
                {
                    "OutputId": "abc",
                    "OutputName": "abc",
                    "OutputType": "abc",
                    "Description": "abc",
                    "Protocol": "abc",
                    "OutputAddressList": [
                        {
                            "Ip": "abc"
                        }
                    ],
                    "OutputRegion": "abc",
                    "SRTSettings": {
                        "Destinations": [
                            {
                                "Ip": "abc",
                                "Port": 0
                            }
                        ],
                        "StreamId": "abc",
                        "Latency": 0,
                        "RecvLatency": 0,
                        "PeerLatency": 0,
                        "PeerIdleTimeout": 0,
                        "Passphrase": "abc",
                        "PbKeyLen": 0,
                        "Mode": "abc",
                        "SourceAddresses": [
                            {
                                "Ip": "abc",
                                "Port": 0
                            }
                        ]
                    },
                    "RTPSettings": {
                        "Destinations": [
                            {
                                "Ip": "abc",
                                "Port": 0
                            }
                        ],
                        "FEC": "abc",
                        "IdleTimeout": 0
                    },
                    "RTMPSettings": {
                        "IdleTimeout": 0,
                        "ChunkSize": 0,
                        "Destinations": [
                            {
                                "Url": "abc",
                                "StreamKey": "abc"
                            }
                        ]
                    },
                    "RTMPPullSettings": {
                        "ServerUrls": [
                            {
                                "TcUrl": "abc",
                                "StreamKey": "abc"
                            }
                        ]
                    },
                    "AllowIpList": [
                        "abc"
                    ],
                    "RTSPPullSettings": {
                        "ServerUrls": [
                            {
                                "Url": "abc"
                            }
                        ]
                    },
                    "HLSPullSettings": {
                        "ServerUrls": [
                            {
                                "Url": "abc"
                            }
                        ]
                    },
                    "MaxConcurrent": 1
                }
            ],
            "EventId": "abc",
            "Region": "abc"
        },
        "RequestId": "abc"
    }
}
```


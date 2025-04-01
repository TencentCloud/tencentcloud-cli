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
            "FlowId": "018f09cc50671eb401a6024fcabc",
            "FlowName": "test",
            "State": "",
            "MaxBandwidth": 0,
            "InputGroup": [
                {
                    "InputId": "",
                    "InputName": "",
                    "Description": "",
                    "Protocol": "",
                    "InputAddressList": [
                        {
                            "Ip": "",
                            "Port": 0
                        }
                    ],
                    "AllowIpList": [
                        ""
                    ],
                    "SRTSettings": {
                        "Mode": "",
                        "StreamId": "",
                        "Latency": 0,
                        "RecvLatency": 0,
                        "PeerLatency": 0,
                        "PeerIdleTimeout": 0,
                        "Passphrase": "",
                        "PbKeyLen": 0,
                        "SourceAddresses": [
                            {
                                "Ip": "",
                                "Port": 0
                            }
                        ]
                    },
                    "RTPSettings": {
                        "FEC": "",
                        "IdleTimeout": 0
                    },
                    "InputRegion": "",
                    "RTMPSettings": {
                        "AppName": "",
                        "StreamKey": ""
                    },
                    "FailOver": "",
                    "RTMPPullSettings": {
                        "SourceAddresses": [
                            {
                                "TcUrl": "",
                                "StreamKey": ""
                            }
                        ]
                    },
                    "RTSPPullSettings": {
                        "SourceAddresses": [
                            {
                                "Url": ""
                            }
                        ]
                    },
                    "HLSPullSettings": {
                        "SourceAddresses": [
                            {
                                "Url": ""
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
                    "OutputId": "",
                    "OutputName": "",
                    "OutputType": "",
                    "Description": "",
                    "Protocol": "",
                    "OutputAddressList": [
                        {
                            "Ip": ""
                        }
                    ],
                    "OutputRegion": "",
                    "SRTSettings": {
                        "Destinations": [
                            {
                                "Ip": "",
                                "Port": 0
                            }
                        ],
                        "StreamId": "",
                        "Latency": 0,
                        "RecvLatency": 0,
                        "PeerLatency": 0,
                        "PeerIdleTimeout": 0,
                        "Passphrase": "",
                        "PbKeyLen": 0,
                        "Mode": "",
                        "SourceAddresses": [
                            {
                                "Ip": "",
                                "Port": 0
                            }
                        ]
                    },
                    "RTPSettings": {
                        "Destinations": [
                            {
                                "Ip": "",
                                "Port": 0
                            }
                        ],
                        "FEC": "",
                        "IdleTimeout": 0
                    },
                    "RTMPSettings": {
                        "IdleTimeout": 0,
                        "ChunkSize": 0,
                        "Destinations": [
                            {
                                "Url": "",
                                "StreamKey": ""
                            }
                        ]
                    },
                    "RTMPPullSettings": {
                        "ServerUrls": [
                            {
                                "TcUrl": "",
                                "StreamKey": ""
                            }
                        ]
                    },
                    "AllowIpList": [
                        ""
                    ],
                    "RTSPPullSettings": {
                        "ServerUrls": [
                            {
                                "Url": ""
                            }
                        ]
                    },
                    "HLSPullSettings": {
                        "ServerUrls": [
                            {
                                "Url": ""
                            }
                        ]
                    },
                    "MaxConcurrent": 1
                }
            ],
            "EventId": "",
            "Region": ""
        },
        "RequestId": ""
    }
}
```


**Example 1: 请求示例**



Input: 

```
tccli mps CreateStreamLinkFlow --cli-unfold-argument  \
    --FlowName aaa \
    --EventId 123 \
    --MaxBandwidth 20000000 \
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
            "EventId": "xx",
            "FlowName": "xx",
            "InputGroup": [
                {
                    "AllowIpList": [
                        "0.0.0.0/0"
                    ],
                    "Protocol": "xx",
                    "Description": "xx",
                    "RTPSettings": {
                        "IdleTimeout": 1000,
                        "FEC": "xx"
                    },
                    "InputAddressList": [
                        {
                            "Ip": "xx",
                            "Port": 0
                        }
                    ],
                    "FailOver": "xx",
                    "RTMPPullSettings": {
                        "SourceAddresses": [
                            {
                                "StreamKey": "xx",
                                "TcUrl": "xx"
                            }
                        ]
                    },
                    "InputName": "xx",
                    "SRTSettings": {
                        "Latency": 0,
                        "PeerLatency": 0,
                        "PbKeyLen": 0,
                        "RecvLatency": 0,
                        "Passphrase": "xx",
                        "StreamId": "xx",
                        "PeerIdleTimeout": 0,
                        "SourceAddresses": [
                            {
                                "Ip": "xx",
                                "Port": 0
                            }
                        ],
                        "Mode": "xx"
                    },
                    "HLSPullSettings": {
                        "SourceAddresses": [
                            {
                                "Url": "xx"
                            }
                        ]
                    },
                    "RTSPPullSettings": {
                        "SourceAddresses": [
                            {
                                "Url": "xx"
                            }
                        ]
                    },
                    "InputRegion": "xx",
                    "InputId": "xx",
                    "ResilientStream": {
                        "Enable": true,
                        "BufferTime": 1
                    },
                    "RTMPSettings": {
                        "StreamKey": "xx",
                        "AppName": "xx"
                    }
                }
            ],
            "Region": "xx",
            "FlowId": "xx",
            "State": "xx",
            "OutputGroup": [
                {
                    "OutputName": "xx",
                    "OutputAddressList": [
                        {
                            "Ip": "xx"
                        }
                    ],
                    "AllowIpList": [
                        "xx"
                    ],
                    "Protocol": "xx",
                    "Description": "xx",
                    "RTPSettings": {
                        "IdleTimeout": 0,
                        "FEC": "xx",
                        "Destinations": [
                            {
                                "Ip": "xx",
                                "Port": 0
                            }
                        ]
                    },
                    "RTMPPullSettings": {
                        "ServerUrls": [
                            {
                                "StreamKey": "xx",
                                "TcUrl": "xx"
                            }
                        ]
                    },
                    "OutputType": "xx",
                    "HLSPullSettings": {
                        "ServerUrls": [
                            {
                                "Url": "xx"
                            }
                        ]
                    },
                    "SRTSettings": {
                        "Latency": 0,
                        "PeerLatency": 0,
                        "PbKeyLen": 0,
                        "RecvLatency": 0,
                        "Passphrase": "xx",
                        "StreamId": "xx",
                        "Mode": "xx",
                        "PeerIdleTimeout": 0,
                        "SourceAddresses": [
                            {
                                "Ip": "xx",
                                "Port": 0
                            }
                        ],
                        "Destinations": [
                            {
                                "Ip": "xx",
                                "Port": 0
                            }
                        ]
                    },
                    "OutputId": "xx",
                    "RTSPPullSettings": {
                        "ServerUrls": [
                            {
                                "Url": "xx"
                            }
                        ]
                    },
                    "RTMPSettings": {
                        "IdleTimeout": 0,
                        "ChunkSize": 0,
                        "Destinations": [
                            {
                                "Url": "xx",
                                "StreamKey": "xx"
                            }
                        ]
                    },
                    "OutputRegion": "xx"
                }
            ],
            "MaxBandwidth": 0
        },
        "RequestId": "xx"
    }
}
```


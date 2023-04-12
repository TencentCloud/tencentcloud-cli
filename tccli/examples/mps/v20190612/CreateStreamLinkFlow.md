**Example 1: 请求示例**

创建媒体传输流

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
    --InputGroup.0.SRTSettings.StreamId #!::u=johnny,r=resource,h=xxx.com,t=stream,m=play \
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
                    "InputAddressList": [
                        {
                            "Ip": "inputtest",
                            "Port": 0
                        }
                    ],
                    "AllowIpList": [
                        "127.0.0.1"
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
                                "Ip": "127.0.0.1",
                                "Port": 0
                            }
                        ]
                    },
                    "RTPSettings": {
                        "FEC": "rtptest",
                        "IdleTimeout": 0
                    },
                    "InputRegion": "ap-region",
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
                    "OutputId": "outputtest",
                    "OutputName": "outputtest",
                    "OutputType": "outputtest",
                    "Description": "outputtest",
                    "Protocol": "outputtest",
                    "OutputAddressList": [
                        {
                            "Ip": "127.0.0.1"
                        }
                    ],
                    "OutputRegion": "ap-region",
                    "SRTSettings": {
                        "Destinations": [
                            {
                                "Ip": "127.0.0.1",
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
                                "Ip": "127.0.0.1",
                                "Port": 0
                            }
                        ]
                    },
                    "RTPSettings": {
                        "Destinations": [
                            {
                                "Ip": "127.0.0.1",
                                "Port": 0
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
                        "127.0.0.1"
                    ],
                    "RTSPPullSettings": {
                        "ServerUrls": [
                            {
                                "Url": "outputtest"
                            }
                        ]
                    },
                    "HLSPullSettings": {
                        "ServerUrls": [
                            {
                                "Url": "outputtest"
                            }
                        ]
                    },
                    "MaxConcurrent": 1
                }
            ],
            "EventId": "eventtest",
            "Region": "ap-region"
        },
        "RequestId": "0186e91bf25809831f1703c66937"
    }
}
```


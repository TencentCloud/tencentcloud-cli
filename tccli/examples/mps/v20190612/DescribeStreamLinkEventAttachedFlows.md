**Example 1: 请求示例**

请求示例

Input: 

```
tccli mps DescribeStreamLinkEventAttachedFlows --cli-unfold-argument  \
    --EventId xx \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "FlowName": "xx",
                "InputGroup": [
                    {
                        "AllowIpList": [
                            "xx"
                        ],
                        "Protocol": "xx",
                        "Description": "xx",
                        "RTPSettings": {
                            "IdleTimeout": 0,
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
            }
        ],
        "RequestId": "xx",
        "TotalNum": 0
    }
}
```


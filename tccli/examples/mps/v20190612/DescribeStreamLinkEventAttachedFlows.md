**Example 1: 请求示例**

查询媒体传输事件关联的所有媒体输入流的配置信息。

Input: 

```
tccli mps DescribeStreamLinkEventAttachedFlows --cli-unfold-argument  \
    --EventId test \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
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
            }
        ],
        "TotalNum": 0,
        "RequestId": "abc"
    }
}
```


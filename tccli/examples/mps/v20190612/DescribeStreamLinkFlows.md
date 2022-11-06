**Example 1: 请求示例**



Input: 

```
tccli mps DescribeStreamLinkFlows --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "TotalPage": 1,
        "PageNum": 1,
        "PageSize": 10,
        "RequestId": "aaaaa",
        "Infos": [
            {
                "FlowName": "sacdsad",
                "InputGroup": [
                    {
                        "AllowIpList": [
                            "0.0.0.0/0"
                        ],
                        "Protocol": "SRT",
                        "Description": "asda",
                        "RTPSettings": {
                            "IdleTimeout": 1000,
                            "FEC": "none"
                        },
                        "InputName": "123sadsasada2",
                        "SRTSettings": {
                            "Latency": 1000,
                            "PeerLatency": 1000,
                            "PbKeyLen": 1000,
                            "RecvLatency": 1000,
                            "Passphrase": "aaaa",
                            "StreamId": "1111",
                            "PeerIdleTimeout": 1000
                        },
                        "RTMPSettings": {
                            "StreamKey": "streamid?a=b",
                            "AppName": "live_appid"
                        },
                        "RTSPPullSettings": {},
                        "FailOver": "xx",
                        "RTMPPullSettings": {},
                        "InputRegion": "ap-mumbai",
                        "InputId": "1213",
                        "InputAddressList": [
                            {
                                "Ip": "0.0.0.0",
                                "Port": 0
                            }
                        ]
                    }
                ],
                "FlowId": "123ds12",
                "State": "IDLE",
                "OutputGroup": [
                    {
                        "OutputName": "sad231edqsq",
                        "OutputAddressList": [
                            {
                                "Ip": "2.2.2.2"
                            }
                        ],
                        "Protocol": "RTP",
                        "Description": "aaaaasss",
                        "RTPSettings": {
                            "IdleTimeout": 1000,
                            "FEC": "none",
                            "Destinations": [
                                {
                                    "Ip": "3.3.3.3",
                                    "Port": 0
                                }
                            ]
                        },
                        "OutputType": "Internet",
                        "SRTSettings": {
                            "Latency": 10000,
                            "PeerLatency": 20000,
                            "PbKeyLen": 10000,
                            "RecvLatency": 30000,
                            "Passphrase": "aaaa",
                            "StreamId": "aaaa",
                            "PeerIdleTimeout": 40000,
                            "Destinations": [
                                {
                                    "Ip": "4.4.4.4",
                                    "Port": 0
                                }
                            ]
                        },
                        "OutputId": "asd21dsa",
                        "RTMPSettings": {
                            "IdleTimeout": 1000,
                            "ChunkSize": 4096,
                            "Destinations": [
                                {
                                    "Url": "rtmp://domain/live",
                                    "StreamKey": "streamid?a=b"
                                }
                            ]
                        },
                        "RTSPPullSettings": {
                            "ServerUrls": [
                                {
                                    "Url": "test"
                                }
                            ]
                        },
                        "RTMPPullSettings": {
                            "ServerUrls": [
                                {
                                    "StreamKey": "test",
                                    "TcUrl": "test"
                                }
                            ]
                        },
                        "OutputRegion": "xx"
                    }
                ],
                "MaxBandwidth": 10000000
            }
        ],
        "TotalNum": 1
    }
}
```


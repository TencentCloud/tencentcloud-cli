**Example 1: 请求示例**



Input: 

```
tccli mps DescribeStreamLinkFlow --cli-unfold-argument  \
    --FlowId aaa
```

Output: 
```
{
    "Response": {
        "Info": {
            "FlowName": "sacdsad",
            "InputGroup": [
                {
                    "AllowIpList": [
                        "0.0.0.0/0"
                    ],
                    "FailOver": "test",
                    "Protocol": "SRT",
                    "Description": "description",
                    "RTPSettings": {
                        "IdleTimeout": 1000,
                        "FEC": "none"
                    },
                    "InputName": "sadsa",
                    "SRTSettings": {
                        "Latency": 1000,
                        "PeerLatency": 1000,
                        "PbKeyLen": 1000,
                        "RecvLatency": 1000,
                        "Passphrase": "aaaa",
                        "StreamId": "",
                        "PeerIdleTimeout": 1000
                    },
                    "RTSPPullSettings": {},
                    "RTMPPullSettings": {},
                    "RTMPSettings": {
                        "StreamKey": "stream?a=b",
                        "AppName": "live"
                    },
                    "InputRegion": "ap-hongkong",
                    "InputId": "id",
                    "InputAddressList": [
                        {
                            "Ip": "2.2.2.2",
                            "Port": 2
                        }
                    ]
                }
            ],
            "FlowId": "",
            "State": "IDLE",
            "OutputGroup": [
                {
                    "OutputName": "sad231edqsq",
                    "OutputAddressList": [
                        {
                            "Ip": "1.1.1.1"
                        }
                    ],
                    "Protocol": "RTP",
                    "Description": "description",
                    "RTPSettings": {
                        "IdleTimeout": 1000,
                        "FEC": "none",
                        "Destinations": [
                            {
                                "Ip": "3.3.3.3",
                                "Port": 3
                            }
                        ]
                    },
                    "OutputType": "Internet",
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
                    "SRTSettings": {
                        "Latency": 1000,
                        "PeerLatency": 1000,
                        "PbKeyLen": 1000,
                        "RecvLatency": 1000,
                        "Passphrase": "aaaa",
                        "StreamId": "aaaa",
                        "PeerIdleTimeout": 1000,
                        "Destinations": [
                            {
                                "Ip": "4.4.4.4",
                                "Port": 4
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
                    "OutputRegion": "ap-mumbai"
                }
            ],
            "MaxBandwidth": 10000000
        },
        "RequestId": "fsaasd"
    }
}
```


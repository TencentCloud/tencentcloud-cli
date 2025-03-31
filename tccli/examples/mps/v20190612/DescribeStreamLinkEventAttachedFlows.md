**Example 1: 请求示例**

查询媒体传输事件关联的所有媒体输入流的配置信息。

Input: 

```
tccli mps DescribeStreamLinkEventAttachedFlows --cli-unfold-argument  \
    --EventId 019202e96d9f09dc0f325e7f7a2a \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "FlowId": "019202e96d9f09dc0f325e7f7a2a",
                "FlowName": "flow_name",
                "State": "IDLE",
                "MaxBandwidth": 0,
                "InputGroup": [
                    {
                        "InputId": "019202e96d9f09dc0f325e7f7a2a",
                        "InputName": "input_name",
                        "Description": "description",
                        "Protocol": "SRT",
                        "InputAddressList": [
                            {
                                "Ip": "102.102.2.3",
                                "Port": 23600
                            }
                        ],
                        "AllowIpList": [
                            "0.0.0.0"
                        ],
                        "SRTSettings": {
                            "Mode": "Listener",
                            "StreamId": "",
                            "Latency": 0,
                            "RecvLatency": 0,
                            "PeerLatency": 0,
                            "PeerIdleTimeout": 0,
                            "Passphrase": "",
                            "PbKeyLen": 0,
                            "SourceAddresses": [
                                {
                                    "Ip": "120.120.23.32",
                                    "Port": 23600
                                }
                            ]
                        },
                        "RTPSettings": {
                            "FEC": "off",
                            "IdleTimeout": 0
                        },
                        "InputRegion": "ap-shanghai",
                        "RTMPSettings": {
                            "AppName": "live",
                            "StreamKey": "live"
                        },
                        "FailOver": "off",
                        "RTMPPullSettings": {
                            "SourceAddresses": [
                                {
                                    "TcUrl": "rtmp://example.com/live",
                                    "StreamKey": "test_live"
                                }
                            ]
                        },
                        "RTSPPullSettings": {
                            "SourceAddresses": [
                                {
                                    "Url": "rtsp://example.com/live/test"
                                }
                            ]
                        },
                        "HLSPullSettings": {
                            "SourceAddresses": [
                                {
                                    "Url": "http://example.com/live/test.m3u8"
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
                        "OutputId": "01937702c54509dc0f3269ca341f",
                        "OutputName": "output_name",
                        "OutputType": "Internet",
                        "Description": "description",
                        "Protocol": "SRT",
                        "OutputAddressList": [
                            {
                                "Ip": "102.32.56.23"
                            }
                        ],
                        "OutputRegion": "ap-shanghai",
                        "SRTSettings": {
                            "Destinations": [
                                {
                                    "Ip": "102.32.56.23",
                                    "Port": 22300
                                }
                            ],
                            "StreamId": "",
                            "Latency": 0,
                            "RecvLatency": 0,
                            "PeerLatency": 0,
                            "PeerIdleTimeout": 0,
                            "Passphrase": "",
                            "PbKeyLen": 0,
                            "Mode": "Caller",
                            "SourceAddresses": [
                                {
                                    "Ip": "102.32.56.23",
                                    "Port": 22300
                                }
                            ]
                        },
                        "RTPSettings": {
                            "Destinations": [
                                {
                                    "Ip": "102.32.56.23",
                                    "Port": 22300
                                }
                            ],
                            "FEC": "off",
                            "IdleTimeout": 0
                        },
                        "RTMPSettings": {
                            "IdleTimeout": 0,
                            "ChunkSize": 0,
                            "Destinations": [
                                {
                                    "Url": "rtmp://example.com/live",
                                    "StreamKey": "live_test"
                                }
                            ]
                        },
                        "RTMPPullSettings": {
                            "ServerUrls": [
                                {
                                    "TcUrl": "rtmp://example.com/live",
                                    "StreamKey": "live_test"
                                }
                            ]
                        },
                        "AllowIpList": [
                            "0.0.0.0"
                        ],
                        "RTSPPullSettings": {
                            "ServerUrls": [
                                {
                                    "Url": "rtsp://example.com/live/test"
                                }
                            ]
                        },
                        "HLSPullSettings": {
                            "ServerUrls": [
                                {
                                    "Url": "http://example.com/live/test.m3u8"
                                }
                            ]
                        },
                        "MaxConcurrent": 1
                    }
                ],
                "EventId": "01937702ecc509dc0f3269ca3420",
                "Region": "ap-shanghai"
            }
        ],
        "TotalNum": 0,
        "RequestId": "01937702c54509dc0f3269ca341f"
    }
}
```


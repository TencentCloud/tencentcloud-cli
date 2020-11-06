**Example 1: Sample request**



Input: 

```
tccli mdc DescribeMediaConnectFlows --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "Uin": "12312",
                "AppId": 123123,
                "ProductName": "MEDIACONNECT",
                "Region": "ap-mumbai",
                "FlowId": "123ds12",
                "FlowName": "sacdsad",
                "ExpireTime": 12312313,
                "State": "IDLE",
                "MaxBandwidth": 10000000,
                "InputGroup": [
                    {
                        "InputId": "123sada2",
                        "InputName": "sadsa",
                        "Description": "2esda",
                        "Protocol": "SRT",
                        "InputIP": "1.1.1.1",
                        "InputPort": 65535,
                        "IpWhitelist": [
                            "0.0.0.0/0"
                        ],
                        "SRTSettings": {
                            "StreamId": "1111",
                            "Latency": 1000,
                            "RecvLatency": 1000,
                            "PeerLatency": 1000,
                            "PeerIdleTimeout": 1000,
                            "Passphrase": "aaaa",
                            "Pbkeylen": 1000
                        },
                        "RTPSettings": {
                            "FEC": "none",
                            "IdleTimeout": 1000
                        },
                        "RTMPSettings": {
                            "IdleTimeout": 1000,
                            "ChunkSize": 4096,
                            "Url": "rtmp://domain/live",
                            "StreamKey": "streamid?a=b"
                        }
                    }
                ],
                "OutputGroup": [
                    {
                        "OutputId": "asd21dsa",
                        "OutputName": "sad231edqsq",
                        "OutputType": "Internet",
                        "Description": "sdajidhj2d'",
                        "Protocol": "RTP",
                        "DestIP": "1.1.1.1",
                        "DestPort": 234,
                        "OutputIp": "2.2.2.2",
                        "SRTSettings": {
                            "StreamId": "aaaa",
                            "Latency": 10000,
                            "RecvLatency": 20000,
                            "PeerLatency": 30000,
                            "PeerIdleTimeout": 40000
                        },
                        "RTPSettings": {
                            "FEC": "none",
                            "IdleTimeout": 1000
                        },
                        "RTMPSettings": {
                            "IdleTimeout": 1000,
                            "ChunkSize": 4096,
                            "Url": "rtmp://domain/live",
                            "StreamKey": "streamid?a=b"
                        }
                    }
                ]
            }
        ],
        "PageNum": 1,
        "PageSize": 10,
        "TotalNum": 1,
        "TotalPage": 1,
        "RequestId": "aaaaa"
    }
}
```


**Example 1: Sample request**



Input: 

```
tccli mdc DescribeMediaConnectFlow --cli-unfold-argument  \
    --FlowId aaa
```

Output: 
```
{
    "Response": {
        "Info": {
            "FlowId": "",
            "FlowName": "sacdsad",
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
                        "StreamId": "",
                        "Latency": 1000,
                        "RecvLatency": 1000,
                        "PeerLatency": 0,
                        "PeerIdleTimeout": 1000,
                        "Passphrase": "aaaa",
                        "Pbkeylen": 1000
                    },
                    "RTPSettings": {
                        "FEC": "none",
                        "IdleTimeout": 1000
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
                    "OutputIp": "1.1.1.1",
                    "SRTSettings": {
                        "DestIP": "",
                        "DestPort": 1223,
                        "StreamId": "aaaa",
                        "Latency": 10000,
                        "RecvLatency": 20000,
                        "PeerLatency": 30000,
                        "PeerIdleTimeout": 40000
                    },
                    "RTPSettings": {
                        "DestIP": "",
                        "Port": 12334,
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
        },
        "RequestId": "aaaaa"
    }
}
```


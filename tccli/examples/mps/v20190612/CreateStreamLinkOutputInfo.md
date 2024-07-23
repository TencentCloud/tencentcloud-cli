**Example 1: 请求示例**



Input: 

```
tccli mps CreateStreamLinkOutputInfo --cli-unfold-argument  \
    --FlowId abc \
    --Output.OutputName abc \
    --Output.Protocol abc \
    --Output.Description abc \
    --Output.RTPSettings.IdleTimeout 1000 \
    --Output.RTPSettings.FEC abc \
    --Output.RTPSettings.Destinations.0.Ip abc \
    --Output.RTPSettings.Destinations.0.Port 0 \
    --Output.SRTSettings.Latency 1000 \
    --Output.SRTSettings.PeerLatency 1000 \
    --Output.SRTSettings.PbKeyLen 0 \
    --Output.SRTSettings.RecvLatency 1000 \
    --Output.SRTSettings.Passphrase abc \
    --Output.SRTSettings.StreamId abc \
    --Output.SRTSettings.PeerIdleTimeout 1000 \
    --Output.SRTSettings.Destinations.0.Ip abc \
    --Output.SRTSettings.Destinations.0.Port 10000 \
    --Output.SRTSettings.Destinations.1.Ip abc \
    --Output.SRTSettings.Destinations.1.Port 10000 \
    --Output.RTMPSettings.ChunkSize 4096 \
    --Output.RTMPSettings.Destinations.0.Url abc \
    --Output.RTMPSettings.Destinations.0.StreamKey abc \
    --Output.RTMPSettings.Destinations.1.Url abc \
    --Output.RTMPSettings.Destinations.1.StreamKey abc \
    --Output.OutputRegion abc
```

Output: 
```
{
    "Response": {
        "Info": {
            "OutputId": "01746d03dd8c0956b92d34d30447",
            "OutputName": "bbbbaaa",
            "OutputType": "Internet",
            "Description": "description",
            "Protocol": "SRT",
            "OutputAddressList": [
                {
                    "Ip": "1.1.1.1"
                },
                {
                    "Ip": "2.2.2.2"
                }
            ],
            "OutputRegion": "ap-mumbai",
            "SRTSettings": {
                "Destinations": [
                    {
                        "Ip": "1.1.1.1",
                        "Port": 10000
                    },
                    {
                        "Ip": "1.1.1.1",
                        "Port": 10000
                    }
                ],
                "StreamId": "#!::u=johnny,t=file,m=publish,r=results.csv",
                "Latency": 1000,
                "RecvLatency": 1000,
                "PeerLatency": 1000,
                "PeerIdleTimeout": 1000,
                "Passphrase": "",
                "PbKeyLen": 0,
                "Mode": "abc",
                "SourceAddresses": [
                    {
                        "Ip": "abc",
                        "Port": 0
                    }
                ]
            },
            "AllowIpList": [
                "test"
            ],
            "RTPSettings": {
                "Destinations": [],
                "FEC": "",
                "IdleTimeout": 0
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
            "RTMPSettings": {
                "Destinations": [],
                "IdleTimeout": 0,
                "ChunkSize": 0
            },
            "HLSPullSettings": {
                "ServerUrls": [
                    {
                        "Url": "abc"
                    }
                ]
            },
            "MaxConcurrent": 1,
            "SecurityGroupIds": [
                "abc"
            ],
            "Zones": [
                "abc"
            ]
        },
        "RequestId": "aaaaa"
    }
}
```


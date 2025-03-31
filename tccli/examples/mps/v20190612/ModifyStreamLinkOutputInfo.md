**Example 1: 请求示例**



Input: 

```
tccli mps ModifyStreamLinkOutputInfo --cli-unfold-argument  \
    --FlowId  \
    --Output.OutputName  \
    --Output.Protocol  \
    --Output.Description  \
    --Output.RTPSettings.IdleTimeout 1000 \
    --Output.RTPSettings.FEC  \
    --Output.RTPSettings.Destinations.0.Ip  \
    --Output.RTPSettings.Destinations.0.Port 0 \
    --Output.SRTSettings.Latency 1000 \
    --Output.SRTSettings.PeerLatency 1000 \
    --Output.SRTSettings.PbKeyLen 0 \
    --Output.SRTSettings.RecvLatency 1000 \
    --Output.SRTSettings.Passphrase  \
    --Output.SRTSettings.StreamId  \
    --Output.SRTSettings.PeerIdleTimeout 1000 \
    --Output.SRTSettings.Destinations.0.Ip  \
    --Output.SRTSettings.Destinations.0.Port 10000 \
    --Output.SRTSettings.Destinations.1.Ip  \
    --Output.SRTSettings.Destinations.1.Port 10000 \
    --Output.OutputId  \
    --Output.RTMPSettings.ChunkSize 4096 \
    --Output.RTMPSettings.Destinations.0.Url  \
    --Output.RTMPSettings.Destinations.0.StreamKey  \
    --Output.RTMPSettings.Destinations.1.Url  \
    --Output.RTMPSettings.Destinations.1.StreamKey 
```

Output: 
```
{
    "Response": {
        "Info": {
            "OutputId": "01746d03dd8c0956b92d34d30447",
            "OutputName": "bbbb",
            "OutputType": "Internet",
            "Description": "description",
            "Protocol": "SRT",
            "MaxConcurrent": 1,
            "OutputAddressList": [
                {
                    "Ip": "1.1.1.1"
                },
                {
                    "Ip": "2.2.2.2"
                }
            ],
            "OutputRegion": "ap-mumbai",
            "RTSPPullSettings": {
                "ServerUrls": [
                    {
                        "Url": ""
                    }
                ]
            },
            "RTMPPullSettings": {
                "ServerUrls": [
                    {
                        "StreamKey": "",
                        "TcUrl": ""
                    }
                ]
            },
            "AllowIpList": [
                ""
            ],
            "SRTSettings": {
                "Mode": "",
                "SourceAddresses": [
                    {
                        "Ip": "",
                        "Port": 1
                    }
                ],
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
                "PbKeyLen": 0
            },
            "HLSPullSettings": {
                "ServerUrls": []
            },
            "RTPSettings": {
                "Destinations": [],
                "FEC": "",
                "IdleTimeout": 0
            },
            "RTMPSettings": {
                "Destinations": [],
                "IdleTimeout": 0,
                "ChunkSize": 0
            }
        },
        "RequestId": "aaaaa"
    }
}
```


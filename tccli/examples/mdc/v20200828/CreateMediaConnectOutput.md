**Example 1: Sample request**



Input: 

```
tccli mdc CreateMediaConnectOutput --cli-unfold-argument  \
    --FlowId 01746cfeda560956b92d34d30445 \
    --Output.OutputName bbbbaaa \
    --Output.Description description \
    --Output.Protocol SRT \
    --Output.OutputRegion ap-mumbai \
    --Output.SRTSettings.Destinations.0.Ip 1.1.1.1 \
    --Output.SRTSettings.Destinations.0.Port 10000 \
    --Output.SRTSettings.Destinations.1.Ip 1.1.1.1 \
    --Output.SRTSettings.Destinations.1.Port 10000 \
    --Output.SRTSettings.StreamId #!::u=johnny,t=file,m=publish,r=results.csv \
    --Output.SRTSettings.Latency 1000 \
    --Output.SRTSettings.RecvLatency 1000 \
    --Output.SRTSettings.PeerLatency 1000 \
    --Output.SRTSettings.PeerIdleTimeout 1000 \
    --Output.RTPSettings.Destinations.0.Ip 1.1.1.1 \
    --Output.RTPSettings.Destinations.0.Port 10000 \
    --Output.RTPSettings.Destinations.1.Ip 1.1.1.1 \
    --Output.RTPSettings.Destinations.1.Port 10000 \
    --Output.RTPSettings.FEC none \
    --Output.RTPSettings.IdleTimeout 1000 \
    --Output.RTMPSettings.Destinations.0.Url rtmp://domain/live \
    --Output.RTMPSettings.Destinations.0.StreamKey streamid?a=b \
    --Output.RTMPSettings.Destinations.1.Url rtmp://domain/live \
    --Output.RTMPSettings.Destinations.1.StreamKey streamid?a=b \
    --Output.RTMPSettings.ChunkSize 4096 \
    --Output.RTMPSettings.Url rtmp://domain/live \
    --Output.RTMPSettings.StreamKey streamid?a=b
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
                "PbKeyLen": 0
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


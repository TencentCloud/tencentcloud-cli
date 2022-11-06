**Example 1: 请求示例**



Input: 

```
tccli mps ModifyStreamLinkInput --cli-unfold-argument  \
    --FlowId 01746cfeda560956b92d34d30445 \
    --Input.InputId 01746cfeda570956b92d34d30446 \
    --Input.InputName inputname \
    --Input.Description inputnameDescription \
    --Input.AllowIpList 0.0.0.0/0 \
    --Input.SRTSettings.Latency 1000 \
    --Input.SRTSettings.RecvLatency 1000 \
    --Input.SRTSettings.PeerLatency 0 \
    --Input.SRTSettings.PeerIdleTimeout 1000 \
    --Input.SRTSettings.Passphrase aaaaaaaaaa \
    --Input.SRTSettings.PbKeyLen 32 \
    --Input.RTPSettings.FEC  \
    --Input.RTPSettings.IdleTimeout 0
```

Output: 
```
{
    "Response": {
        "Info": {
            "AllowIpList": [
                "0.0.0.0/0"
            ],
            "Protocol": "xx",
            "Description": "xx",
            "RTPSettings": {
                "IdleTimeout": 0,
                "FEC": "xx"
            },
            "InputName": "xx",
            "SRTSettings": {
                "Latency": 1000,
                "PeerLatency": 0,
                "PbKeyLen": 32,
                "RecvLatency": 1000,
                "Passphrase": "xx",
                "StreamId": "xx",
                "PeerIdleTimeout": 1000
            },
            "RTMPSettings": {
                "StreamKey": "xx",
                "AppName": "xx"
            },
            "RTSPPullSettings": {
                "SourceAddresses": [
                    {
                        "Url": "xx"
                    }
                ]
            },
            "RTMPPullSettings": {
                "SourceAddresses": [
                    {
                        "StreamKey": "xx",
                        "TcUrl": "xx"
                    }
                ]
            },
            "FailOver": "xx",
            "InputRegion": "xx",
            "InputId": "xx",
            "InputAddressList": [
                {
                    "Ip": "xx",
                    "Port": 1
                },
                {
                    "Ip": "xx",
                    "Port": 1
                }
            ]
        },
        "RequestId": "xx"
    }
}
```


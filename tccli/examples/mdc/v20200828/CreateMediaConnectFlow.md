**Example 1: Sample request**



Input: 

```
tccli mdc CreateMediaConnectFlow --cli-unfold-argument  \
    --FlowName aaa \
    --MaxBandwidth 20000000 \
    --InputGroup.0.InputName inputname \
    --InputGroup.0.Description inputnameDescription \
    --InputGroup.0.Protocol RTP \
    --InputGroup.0.AllowIpList 0.0.0.0/0 \
    --InputGroup.0.SRTSettings.StreamId #!::u=johnny,t=file,m=publish,r=results.csv \
    --InputGroup.0.SRTSettings.Latency 1000 \
    --InputGroup.0.SRTSettings.RecvLatency 1000 \
    --InputGroup.0.SRTSettings.PeerLatency 1000 \
    --InputGroup.0.SRTSettings.PeerIdleTimeout 1000 \
    --InputGroup.0.SRTSettings.Passphrase aaa \
    --InputGroup.0.SRTSettings.Pbkeylen 10 \
    --InputGroup.0.RTPSettings.FEC none \
    --InputGroup.0.RTPSettings.IdleTimeout 1000
```

Output: 
```
{
    "Response": {
        "Info": {
            "FlowId": "01742ac4e2b90956b92d573b0443",
            "FlowName": "aaa",
            "State": "IDLE",
            "InputGroup": [
                {
                    "InputId": "01742ac4e2b90956b92d573b0444",
                    "InputName": "inputname",
                    "InputType": "",
                    "Description": "inputname Description",
                    "Protocol": "RTP",
                    "InputIP": "",
                    "InputPort": 0,
                    "IpWhitelist": [
                        "0.0.0.0/0"
                    ],
                    "SRTSettings": {
                        "Latency": 0,
                        "RecvLatency": 0,
                        "PeerLatency": 0,
                        "PeerIdleTimeout": 0,
                        "Passphrase": "",
                        "Pbkeylen": 0
                    },
                    "RTPSettings": {
                        "FEC": "none",
                        "IdleTimeout": 1000
                    },
                    "RTMPSettings": {
                        "IdleTimeout": 0,
                        "ChunkSize": 0,
                        "Url": "",
                        "StreamKey": ""
                    }
                }
            ],
            "OutputGroup": []
        },
        "RequestId": "aaaaa"
    }
}
```


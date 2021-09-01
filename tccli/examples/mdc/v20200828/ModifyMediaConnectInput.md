**Example 1: Sample request**



Input: 

```
tccli mdc ModifyMediaConnectInput --cli-unfold-argument  \
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
            "InputId": "01746cfeda570956b92d34d30446",
            "InputName": "inputname",
            "Description": "inputname Description",
            "Protocol": "SRT",
            "InputAddressList": [
                {
                    "Ip": "1.1.1.1",
                    "Port": 1
                },
                {
                    "Ip": "1.1.1.1",
                    "Port": 1
                }
            ],
            "AllowIpList": [
                "0.0.0.0/0"
            ],
            "SRTSettings": {
                "Latency": 1000,
                "RecvLatency": 1000,
                "PeerLatency": 0,
                "PeerIdleTimeout": 1000,
                "Passphrase": "aaaaaaaaaa",
                "PbKeyLen": 32
            },
            "RTPSettings": {
                "FEC": "",
                "IdleTimeout": 0
            }
        },
        "RequestId": "aaaaa"
    }
}
```


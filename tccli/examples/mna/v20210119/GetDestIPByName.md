**Example 1: 根据DeviceName（testdev）查询目标IP列表**



Input: 

```
tccli mna GetDestIPByName --cli-unfold-argument  \
    --DeviceName testdev \
    --BeginTime 1758544656 \
    --EndTime 1758544716 \
    --GatewayType 0
```

Output: 
```
{
    "Response": {
        "AccessRegion": "MC",
        "DestIpInfo": [
            {
                "GatewayIp": "",
                "GatewaySite": "",
                "IpCount": 0,
                "IpList": [],
                "Time": "1758544620"
            },
            {
                "GatewayIp": "",
                "GatewaySite": "",
                "IpCount": 0,
                "IpList": [],
                "Time": "1758544680"
            }
        ],
        "RequestId": "33ef661c-3d47-4b67-96a1-d4852daeace6"
    }
}
```


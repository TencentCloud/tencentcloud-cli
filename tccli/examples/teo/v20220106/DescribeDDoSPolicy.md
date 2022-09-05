**Example 1: 查询DDoS防护配置**



Input: 

```
tccli teo DescribeDDoSPolicy --cli-unfold-argument  \
    --PolicyId 1456 \
    --ZoneId zone-285thql0vdhi
```

Output: 
```
{
    "Response": {
        "RequestId": "2a814004-5cb4-4776-bd4e-c34a85688754",
        "DdosRule": {
            "DdosAcl": {
                "Acl": [
                    {
                        "Action": "forward",
                        "Default": 0,
                        "DportEnd": 80,
                        "DportStart": 80,
                        "Protocol": "all",
                        "SportEnd": 65535,
                        "SportStart": 1
                    }
                ],
                "Switch": "on"
            },
            "DdosAllowBlock": {
                "Switch": "on",
                "UserAllowBlockIp": []
            },
            "DdosAntiPly": {
                "AbnormalConnectNum": 0,
                "AbnormalSynNum": 0,
                "AbnormalSynRatio": 0,
                "ConnectTimeout": 0,
                "DestinationConnectLimit": 0,
                "DestinationCreateLimit": 0,
                "DropIcmp": "off",
                "DropOther": "off",
                "DropTcp": "off",
                "DropUdp": "off",
                "EmptyConnectProtect": "off",
                "SourceConnectLimit": 0,
                "SourceCreateLimit": 0,
                "UdpShard": "off"
            },
            "DdosGeoIp": {
                "RegionId": [
                    1818209
                ],
                "Switch": "on"
            },
            "DdosPacketFilter": {
                "PacketFilter": [],
                "Switch": "on"
            },
            "DdosSpeedLimit": {
                "FluxLimit": "0 bps",
                "PackageLimit": "0 pps"
            },
            "DdosStatusInfo": {
                "AiStatus": "off",
                "Appid": "1300054968",
                "PlyLevel": "middle"
            },
            "Switch": "on"
        }
    }
}
```


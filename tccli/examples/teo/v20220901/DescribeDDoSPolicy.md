**Example 1: 查询Ddos防护详细配置**



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
        "RequestId": "7d20dbda-d747-4946-9ada-30ca22449d69",
        "DDoSRule": {
            "DDoSAcl": {
                "DDoSAclRules": [
                    {
                        "Action": "forward",
                        "DportEnd": 80,
                        "DportStart": 80,
                        "Protocol": "all",
                        "SportEnd": 65535,
                        "SportStart": 1
                    }
                ],
                "Switch": "on"
            },
            "DDoSAllowBlock": {
                "DDoSAllowBlockRules": [
                    {
                        "Ip": "2.2.2.2",
                        "Type": "allow",
                        "UpdateTime": 1661828230
                    }
                ],
                "Switch": "on"
            },
            "DDoSAntiPly": {
                "AbnormalConnectNum": 0,
                "AbnormalSynNum": 0,
                "AbnormalSynRatio": 0,
                "ConnectTimeout": 0,
                "DestinationConnectLimit": 0,
                "DestinationCreateLimit": 0,
                "DropIcmp": "on",
                "DropOther": "off",
                "DropTcp": "off",
                "DropUdp": "off",
                "EmptyConnectProtect": "off",
                "SourceConnectLimit": 0,
                "SourceCreateLimit": 0,
                "UdpShard": "off"
            },
            "DDoSGeoIp": {
                "RegionIds": [],
                "Switch": "on"
            },
            "DDoSPacketFilter": {
                "DDoSFeaturesFilters": [
                    {
                        "Action": "forward",
                        "Depth": 123,
                        "Depth2": 1500,
                        "DportEnd": 0,
                        "DportStart": 0,
                        "IsNot": 0,
                        "IsNot2": 0,
                        "MatchBegin": "begin_l3",
                        "MatchBegin2": "no_match",
                        "MatchLogic": "none",
                        "MatchType": "sunday",
                        "MatchType2": "sunday",
                        "Offset": 23,
                        "Offset2": 0,
                        "PacketMax": 0,
                        "PacketMin": 0,
                        "Protocol": "udp",
                        "SportEnd": 0,
                        "SportStart": 0,
                        "Str": "123",
                        "Str2": ""
                    }
                ],
                "Switch": "on"
            },
            "DDoSSpeedLimit": {
                "FluxLimit": "0 bps",
                "PackageLimit": "0 pps"
            },
            "DDoSStatusInfo": {
                "PlyLevel": "middle"
            },
            "Switch": "on"
        }
    }
}
```


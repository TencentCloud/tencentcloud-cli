**Example 1: 获取DDoS高级策略**



Input: 

```
tccli dayu DescribeDDoSPolicy --cli-unfold-argument  \
    --Business bgp \
    --Id bgpip-000000xe
```

Output: 
```
{
    "Response": {
        "DDosPolicyList": [
            {
                "PolicyId": "policy-000003h6",
                "PolicyName": "name2",
                "DropOptions": {
                    "DropTcp": 1,
                    "DropUdp": 1,
                    "DropIcmp": 1,
                    "DropOther": 1,
                    "DropAbroad": 1,
                    "CheckSyncConn": 1
                },
                "PortLimits": [
                    {
                        "Protocol": "tcp",
                        "DPortStart": 0,
                        "DPortEnd": 6000
                    }
                ],
                "IpBlackWhiteLists": [
                    {
                        "Ip": "1.1.1.13",
                        "Type": "white"
                    },
                    {
                        "Ip": "153.45.0.78",
                        "Type": "black"
                    }
                ],
                "PacketFilters": [
                    {
                        "Protocol": "tcp",
                        "SportStart": 0,
                        "SportEnd": 65535,
                        "DportStart": 0,
                        "DportEnd": 65535,
                        "PktlenMin": 520,
                        "PktlenMax": 1024,
                        "MatchBegin": "no_match",
                        "MatchType": "sunday",
                        "Str": "",
                        "Depth": 0,
                        "Offset": 0,
                        "IsNot": 0,
                        "Action": "transmit"
                    }
                ],
                "Resources": [
                    {
                        "Id": "bgpip-000000xe",
                        "IpList": [
                            "123.206.79.197"
                        ]
                    }
                ],
                "WaterPrint": [
                    {
                        "Offset": 0,
                        "RemoveSwitch": 1,
                        "OpenStatus": 1,
                        "TcpPortList": [
                            "1000-2000"
                        ],
                        "UdpPortList": [
                            "1000-2000"
                        ]
                    }
                ],
                "WaterKey": [
                    {
                        "KeyId": 1234,
                        "KeyContent": "abc6b301-a322-493a-8e36-83b295453497",
                        "KeyVersion": "123",
                        "OpenStatus": 1
                    }
                ],
                "CreateTime": "2018-11-07 11:13:14"
            }
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```


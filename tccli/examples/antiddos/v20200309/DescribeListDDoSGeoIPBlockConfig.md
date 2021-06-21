**Example 1: 获取DDoS防护的区域封禁配置列表**



Input: 

```
tccli antiddos DescribeListDDoSGeoIPBlockConfig --cli-unfold-argument  \
    --Offset 0 \
    --Limit 25 \
    --FilterIp 1.1.1.1 \
    --FilterInstanceId bgpip-*
```

Output: 
```
{
    "Response": {
        "RequestId": "bcfa39ae-5b8b-4b5b-9e53-016176e54b59",
        "ConfigList": [
            {
                "GeoIPBlockConfig": {
                    "RegionType": "customized",
                    "AreaList": [
                        100001,
                        100002
                    ],
                    "Action": "drop",
                    "Id": "00000001"
                },
                "InstanceDetailList": [
                    {
                        "EipList": [
                            "1.1.1.1"
                        ],
                        "InstanceId": "bgpip-0000011x"
                    }
                ]
            }
        ],
        "Total": 1
    }
}
```


**Example 1: 获取CC防护的区域封禁配置列表**



Input: 

```
tccli antiddos DescribeCcGeoIPBlockConfigList --cli-unfold-argument  \
    --Domain test.dayu.com \
    --Protocol http \
    --Business bgpip \
    --InstanceId bgpip-111111q1 \
    --Ip 1.1.1.1 \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "CcGeoIpPolicyList": [
            {
                "Domain": "test.dayu.com",
                "Protocol": "http",
                "InstanceId": "bgpip-111111q1",
                "Ip": "1.1.1.1",
                "RegionType": "china",
                "PolicyId": "rule-0000011x",
                "ModifyTime": "2020-09-22 00:00:00",
                "Action": "1",
                "CreateTime": "2020-09-22 00:00:00",
                "AreaList": [
                    1
                ]
            }
        ],
        "Total": 1,
        "RequestId": "c9520936-381c-4c04-b535-c8f4df1f8059"
    }
}
```


**Example 1: 获取CC防护的区域封禁配置列表**



Input: 

```
tccli antiddos DescribeCcGeoIPBlockConfigList --cli-unfold-argument  \
    --Domain xx \
    --Protocol xx \
    --Business xx \
    --InstanceId xx \
    --Ip xx \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "CcGeoIpPolicyList": [
            {
                "Domain": "xx",
                "Protocol": "xx",
                "InstanceId": "xx",
                "Ip": "xx",
                "RegionType": "xx",
                "PolicyId": "xx",
                "ModifyTime": "2020-09-22 00:00:00",
                "Action": "xx",
                "CreateTime": "2020-09-22 00:00:00",
                "AreaList": [
                    1
                ]
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```


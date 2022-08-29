**Example 1: 查询域名解析记录列表**



Input: 

```
tccli gaap DescribeGlobalDomainDns --cli-unfold-argument  \
    --DomainId test.com
```

Output: 
```
{
    "Response": {
        "RequestId": "51828ffb-75f5-4378-921b-212a8a07574c",
        "GlobalDnsList": [
            {
                "Status": 0,
                "AccessList": [],
                "CountryAreaList": [
                    {
                        "Remark": "1",
                        "NationCountryName": "韩国",
                        "GeographicalZoneInnerCode": "101000",
                        "ContinentName": "亚洲",
                        "ContinentInnerCode": "100000",
                        "NationCountryInnerCode": "101007",
                        "GeographicalZoneName": "东亚"
                    },
                    {
                        "Remark": "1",
                        "NationCountryName": "中国大陆-华西",
                        "GeographicalZoneInnerCode": "101000",
                        "ContinentName": "亚洲",
                        "ContinentInnerCode": "100000",
                        "NationCountryInnerCode": "101004",
                        "GeographicalZoneName": "东亚"
                    }
                ],
                "DnsRecordId": 258
            }
        ]
    }
}
```

**Example 2: 查询统一域名的域名解析**



Input: 

```
tccli gaap DescribeGlobalDomainDns --cli-unfold-argument  \
    --DomainId dm-fgsymu39
```

Output: 
```
{
    "Response": {
        "RequestId": "fa0f3927-406e-4a45-bced-590b4b0175fe",
        "GlobalDnsList": [
            {
                "DnsRecordId": 12756,
                "CountryAreaList": [
                    {
                        "ContinentInnerCode": "100000",
                        "ContinentName": "亚洲",
                        "GeographicalZoneInnerCode": "101000",
                        "GeographicalZoneName": "东亚",
                        "NationCountryInnerCode": "101001",
                        "NationCountryName": "中国大陆-华北"
                    }
                ],
                "AccessList": [
                    {
                        "ProxyId": "link-4m6fx36h",
                        "Vip": "1.14.225.21",
                        "VipList": [
                            {
                                "IP": "1.14.225.21",
                                "Provider": "BGP",
                                "Bandwidth": 10
                            }
                        ],
                        "RegionId": "Guangzhou",
                        "SourceRegionIdcType": "dc",
                        "RegionName": "广州（原中国大陆-华南大区）"
                    }
                ],
                "Status": 1
            }
        ]
    }
}
```


**Example 1: 获取通道组域名解析配置详情**



Input: 

```
tccli gaap DescribeGroupDomainConfig --cli-unfold-argument  \
    --GroupId lg-b7h4d02f
```

Output: 
```
{
    "Response": {
        "DefaultDnsIp": "lg-na2d00jf",
        "AccessRegionCount": 2,
        "RequestId": "74b5f95c-e976-4f78-b2ee-aad49eb844c4",
        "AccessRegionList": [
            {
                "NationCountryInnerList": [
                    {
                        "NationCountryName": "North China",
                        "NationCountryInnerCode": "101001"
                    },
                    {
                        "NationCountryName": "East China",
                        "NationCountryInnerCode": "101002"
                    },
                    {
                        "NationCountryName": "South China",
                        "NationCountryInnerCode": "101003"
                    },
                    {
                        "NationCountryName": "West China",
                        "NationCountryInnerCode": "101004"
                    }
                ],
                "ContinentInnerCode": "100000",
                "RegionId": "EastChina",
                "GeographicalZoneInnerCode": "101000",
                "ProxyList": [
                    {
                        "ProxyId": "link-4lzfc73l"
                    }
                ],
                "RegionName": "East China"
            },
            {
                "NationCountryInnerList": [
                    {
                        "NationCountryName": "Australia",
                        "NationCountryInnerCode": "401000"
                    },
                    {
                        "NationCountryName": "New Zealand",
                        "NationCountryInnerCode": "401001"
                    }
                ],
                "ContinentInnerCode": "400000",
                "RegionId": "SL_Australia",
                "GeographicalZoneInnerCode": "401000",
                "ProxyList": [
                    {
                        "ProxyId": "link-ozvhjhp1"
                    }
                ],
                "RegionName": "Australia (Sydney)"
            }
        ],
        "GroupId": "lg-na2d00jf"
    }
}
```


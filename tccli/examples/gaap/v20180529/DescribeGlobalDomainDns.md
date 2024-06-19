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


**Example 1: 查看地域列表**

查看地域列表

Input: 

```
tccli ecm DescribeNode --cli-unfold-argument  \
    --Filters.0.Name InstanceFamily \
    --Filters.0.Values SN3ne
```

Output: 
```
{
    "Response": {
        "RequestId": "187c16d5-1f53-4e88-b684-077f0c7123b2",
        "NodeSet": [
            {
                "ZoneInfo": {
                    "ZoneId": 10110001,
                    "ZoneName": "杭州一区",
                    "Zone": "ap-hangzhou-ecm-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-east",
                    "AreaName": "华东"
                },
                "Province": {
                    "ProvinceId": "china-east-zhejiang",
                    "ProvinceName": "浙江"
                },
                "City": {
                    "CityId": "china-east-zhejiang-hangzhou",
                    "CityName": "杭州"
                },
                "RegionInfo": {
                    "RegionId": 1011,
                    "Region": "ap-hangzhou-ecm",
                    "RegionName": "杭州"
                },
                "ISPSet": [
                    {
                        "ISPId": "CMCC",
                        "ISPName": "移动"
                    },
                    {
                        "ISPId": "CUCC",
                        "ISPName": "联通"
                    },
                    {
                        "ISPId": "CTCC",
                        "ISPName": "电信"
                    },
                    {
                        "ISPId": "CTCC;CUCC;CMCC",
                        "ISPName": "三网"
                    }
                ],
                "ISPNum": 3
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10510001,
                    "ZoneName": "深圳五区（电信）",
                    "Zone": "ap-shenzhen-ecm-ct2"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-south",
                    "AreaName": "华南"
                },
                "Province": {
                    "ProvinceId": "china-south-guangdong",
                    "ProvinceName": "广东"
                },
                "City": {
                    "CityId": "china-south-guangdong-shenzhen",
                    "CityName": "深圳"
                },
                "RegionInfo": {
                    "RegionId": 1051,
                    "Region": "ap-shenzhen-ecm-ct2",
                    "RegionName": "深圳"
                },
                "ISPSet": [
                    {
                        "ISPId": "CTCC",
                        "ISPName": "电信"
                    }
                ],
                "ISPNum": 1
            }
        ],
        "TotalCount": 2
    }
}
```


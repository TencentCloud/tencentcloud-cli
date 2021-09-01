**Example 1: 获取指定区域人流各年龄占比**



Input: 

```
tccli youmall DescribeZoneFlowAgeInfoByZoneId --cli-unfold-argument  \
    --CompanyId testCompany1 \
    --ShopId 1 \
    --ZoneId 1 \
    --StartDate 2016-10-10 \
    --EndDate 2017-06-01
```

Output: 
```
{
    "Response": {
        "RequestId": "803ce68a-1bf4-4cbc-89da-6e3a6c7710ea",
        "CompanyId": "tencent",
        "ShopId": 12345,
        "ZoneId": 1,
        "ZoneName": "餐饮区",
        "Data": [
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ]
    }
}
```


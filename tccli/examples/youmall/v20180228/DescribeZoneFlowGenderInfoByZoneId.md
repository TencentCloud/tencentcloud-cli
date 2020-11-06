**Example 1: 获取指定区域性别占比**



Input: 

```
tccli youmall DescribeZoneFlowGenderInfoByZoneId --cli-unfold-argument  \
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
        "RequestId": "16719a3d-4826-43e7-b726-dce6062a59e4",
        "CompanyId": "tencent",
        "ShopId": 12345,
        "ZoneId": 1,
        "ZoneName": "餐饮区",
        "MalePercent": 0,
        "FemalePercent": 0
    }
}
```


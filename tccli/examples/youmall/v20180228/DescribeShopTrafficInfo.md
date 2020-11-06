**Example 1: 获取每日客流人数接口-成功实例**



Input: 

```
tccli youmall DescribeShopTrafficInfo --cli-unfold-argument  \
    --CompanyId testCompany1 \
    --ShopId 123 \
    --StartDate 2018-06-01 \
    --EndDate 2018-06-15 \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "CompanyId": "testCompany1",
        "TotalCount": 2,
        "ShopDayTrafficInfoSet": [
            {
                "Date": "2018-06-01",
                "DayTrafficCount": 1000,
                "GenderAgeTrafficDetailSet": [
                    {
                        "AgeGap": "12-10",
                        "Gender": 1,
                        "TrafficCount": 123
                    },
                    {
                        "AgeGap": "12-10",
                        "Gender": 0,
                        "TrafficCount": 123
                    }
                ]
            },
            {
                "Date": "2018-06-02",
                "DayTrafficCount": 1000,
                "GenderAgeTrafficDetailSet": [
                    {
                        "AgeGap": "12-10",
                        "Gender": 1,
                        "TrafficCount": 123
                    },
                    {
                        "AgeGap": "12-10",
                        "Gender": 0,
                        "TrafficCount": 123
                    }
                ]
            }
        ],
        "RequestId": "6ec80684-0879-405e-8932-72e7c0c48ef8",
        "ShopId": 123
    }
}
```

**Example 2: 获取每日客流人数接口-失败实例**



Input: 

```
tccli youmall DescribeShopTrafficInfo --cli-unfold-argument  \
    --ShopId 123 \
    --StartDate 2018-06-01 \
    --EndDate 2018-06-15 \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "Parameter CompanyId is missing"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```


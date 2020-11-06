**Example 1: 获取每小时客流人数接口-成功**



Input: 

```
tccli youmall DescribeShopHourTrafficInfo --cli-unfold-argument  \
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
        "ShopHourTrafficInfoSet": [
            {
                "Date": "2018-06-01",
                "HourTrafficInfoDetailSet": [
                    {
                        "Hour": 12,
                        "HourTrafficCount": 1000
                    },
                    {
                        "Hour": 11,
                        "HourTrafficCount": 1000
                    }
                ]
            },
            {
                "Date": "2018-06-02",
                "HourTrafficInfoDetailSet": [
                    {
                        "Hour": 12,
                        "HourTrafficCount": 1000
                    },
                    {
                        "Hour": 11,
                        "HourTrafficCount": 1000
                    }
                ]
            }
        ],
        "RequestId": "6ec80684-0879-405e-8932-72e7c0c48ef8",
        "ShopId": 123
    }
}
```

**Example 2: 获取每小时客流人数接口-失败**



Input: 

```
tccli youmall DescribeShopHourTrafficInfo --cli-unfold-argument  \
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


**Example 1: 获取指定区域不同年龄段男女平均停留时间**



Input: 

```
tccli youmall DescribeZoneFlowGenderAvrStayTimeByZoneId --cli-unfold-argument  \
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
        "RequestId": "17dc5fc2-f482-42ed-b5c1-f92d028dad79",
        "CompanyId": "tencent",
        "ShopId": 12345,
        "ZoneId": 1,
        "ZoneName": "餐饮区",
        "Data": [
            {
                "MaleAvrStayTime": 0,
                "FemaleAvrStayTime": 0
            },
            {
                "MaleAvrStayTime": 0,
                "FemaleAvrStayTime": 0
            },
            {
                "MaleAvrStayTime": 0,
                "FemaleAvrStayTime": 0
            },
            {
                "MaleAvrStayTime": 0,
                "FemaleAvrStayTime": 0
            },
            {
                "MaleAvrStayTime": 0,
                "FemaleAvrStayTime": 0
            },
            {
                "MaleAvrStayTime": 0,
                "FemaleAvrStayTime": 0
            },
            {
                "MaleAvrStayTime": 0,
                "FemaleAvrStayTime": 0
            }
        ]
    }
}
```


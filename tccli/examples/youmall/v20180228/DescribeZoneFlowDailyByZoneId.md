**Example 1: 获取指定区域每日客流量**



Input: 

```
tccli youmall DescribeZoneFlowDailyByZoneId --cli-unfold-argument  \
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
        "RequestId": "9bf7fde2-a9dc-4ad0-a04c-35d30e01c605",
        "CompanyId": "tencent",
        "ShopId": 12345,
        "ZoneId": 1,
        "ZoneName": "餐饮区",
        "Data": [
            {
                "Day": "2018-09-21",
                "FlowCount": 0
            },
            {
                "Day": "2018-09-22",
                "FlowCount": 0
            },
            {
                "Day": "2018-09-23",
                "FlowCount": 0
            },
            {
                "Day": "2018-09-24",
                "FlowCount": 0
            },
            {
                "Day": "2018-09-25",
                "FlowCount": 0
            },
            {
                "Day": "2018-09-26",
                "FlowCount": 0
            },
            {
                "Day": "2018-09-27",
                "FlowCount": 0
            },
            {
                "Day": "2018-09-28",
                "FlowCount": 0
            }
        ]
    }
}
```


**Example 1: 获取区域人流和停留时间**



Input: 

```
tccli youmall DescribeZoneFlowAndStayTime --cli-unfold-argument  \
    --CompanyId testCompany1 \
    --ShopId 1 \
    --StartDate 2016-10-10 \
    --EndDate 2017-06-01
```

Output: 
```
{
    "Response": {
        "RequestId": "111a6cae-3bae-45ee-a8bd-9b2ec6f028e7",
        "CompanyId": "tencent",
        "ShopId": 12345,
        "Data": [
            {
                "ZoneId": 2,
                "ZoneName": "方便面区",
                "FlowCount": 0,
                "AvrStayTime": 0
            },
            {
                "ZoneId": 3,
                "ZoneName": "收银区",
                "FlowCount": 0,
                "AvrStayTime": 0
            },
            {
                "ZoneId": 4,
                "ZoneName": "麦子工坊",
                "FlowCount": 0,
                "AvrStayTime": 0
            },
            {
                "ZoneId": 5,
                "ZoneName": "水果区",
                "FlowCount": 0,
                "AvrStayTime": 0
            },
            {
                "ZoneId": 6,
                "ZoneName": "出入口",
                "FlowCount": 0,
                "AvrStayTime": 0
            },
            {
                "ZoneId": 7,
                "ZoneName": "冷饮区",
                "FlowCount": 0,
                "AvrStayTime": 0
            },
            {
                "ZoneId": 8,
                "ZoneName": "干百区",
                "FlowCount": 0,
                "AvrStayTime": 0
            },
            {
                "ZoneId": 9,
                "ZoneName": "吧台区",
                "FlowCount": 0,
                "AvrStayTime": 0
            },
            {
                "ZoneId": 10,
                "ZoneName": "冷冻区",
                "FlowCount": 0,
                "AvrStayTime": 0
            },
            {
                "ZoneId": 11,
                "ZoneName": "生活区",
                "FlowCount": 0,
                "AvrStayTime": 0
            },
            {
                "ZoneId": 12,
                "ZoneName": "酒类区",
                "FlowCount": 0,
                "AvrStayTime": 0
            }
        ]
    }
}
```


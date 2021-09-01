**Example 1: 获取指定区域分时客流量**



Input: 

```
tccli youmall DescribeZoneFlowHourlyByZoneId --cli-unfold-argument  \
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
        "RequestId": "78cd194f-459f-4b65-8b0a-fd3b69abb768",
        "CompanyId": "tencent",
        "ShopId": 10086,
        "ZoneId": 1,
        "ZoneName": "西北出口",
        "Data": [
            {
                "Hour": 0,
                "FlowCount": 0
            },
            {
                "Hour": 1,
                "FlowCount": 0
            },
            {
                "Hour": 2,
                "FlowCount": 0
            },
            {
                "Hour": 3,
                "FlowCount": 0
            },
            {
                "Hour": 4,
                "FlowCount": 0
            },
            {
                "Hour": 5,
                "FlowCount": 0
            },
            {
                "Hour": 6,
                "FlowCount": 0
            },
            {
                "Hour": 7,
                "FlowCount": 0
            },
            {
                "Hour": 8,
                "FlowCount": 0
            },
            {
                "Hour": 9,
                "FlowCount": 0
            },
            {
                "Hour": 10,
                "FlowCount": 0
            },
            {
                "Hour": 11,
                "FlowCount": 0
            },
            {
                "Hour": 12,
                "FlowCount": 0
            },
            {
                "Hour": 13,
                "FlowCount": 0
            },
            {
                "Hour": 14,
                "FlowCount": 0
            },
            {
                "Hour": 15,
                "FlowCount": 0
            },
            {
                "Hour": 16,
                "FlowCount": 0
            },
            {
                "Hour": 17,
                "FlowCount": 0
            },
            {
                "Hour": 18,
                "FlowCount": 0
            },
            {
                "Hour": 19,
                "FlowCount": 0
            },
            {
                "Hour": 20,
                "FlowCount": 0
            },
            {
                "Hour": 21,
                "FlowCount": 0
            },
            {
                "Hour": 22,
                "FlowCount": 0
            },
            {
                "Hour": 23,
                "FlowCount": 0
            }
        ]
    }
}
```


**Example 1: 域名解析量统计**

 

Input: 

```
tccli dnspod DescribeDomainAnalytics --cli-unfold-argument  \
    --Domain example.com \
    --StartDate 2022-06-14 \
    --EndDate 2022-06-14
```

Output: 
```
{
    "Response": {
        "AliasData": [],
        "Data": [
            {
                "DateKey": "20221201",
                "HourKey": 0,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 1,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 2,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 3,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 4,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 5,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 6,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 7,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 8,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 9,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 10,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 11,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 12,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 13,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 14,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 15,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 16,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 17,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 18,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 19,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 20,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 21,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 22,
                "Num": 0
            },
            {
                "DateKey": "20221201",
                "HourKey": 23,
                "Num": 0
            }
        ],
        "Info": {
            "DnsFormat": "HOUR",
            "DnsTotal": 8358,
            "Domain": "zhaodapian.com",
            "EndDate": "2022-12-01",
            "StartDate": "2022-12-01"
        },
        "RequestId": "e0815831-4978-445e-b524-746df0069d39"
    }
}
```


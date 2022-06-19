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
        "RequestId": "xx",
        "AliasData": [
            {
                "Data": [
                    {
                        "DateKey": "20220614",
                        "HourKey": 0,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 1,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 2,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 3,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 4,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 5,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 6,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 7,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 8,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 9,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 10,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 11,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 12,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 13,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 14,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 15,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 16,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 17,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 18,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 19,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 20,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 21,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 22,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": 23,
                        "Num": 0
                    }
                ],
                "Info": {
                    "DnsFormat": "HOUR",
                    "DnsTotal": 0,
                    "Domain": "example.comalias.com",
                    "EndDate": "2022-06-14",
                    "StartDate": "2022-06-14"
                }
            }
        ],
        "Data": [
            {
                "DateKey": "20220614",
                "HourKey": 0,
                "Num": 140
            },
            {
                "DateKey": "20220614",
                "HourKey": 1,
                "Num": 136
            },
            {
                "DateKey": "20220614",
                "HourKey": 2,
                "Num": 134
            },
            {
                "DateKey": "20220614",
                "HourKey": 3,
                "Num": 126
            },
            {
                "DateKey": "20220614",
                "HourKey": 4,
                "Num": 147
            },
            {
                "DateKey": "20220614",
                "HourKey": 5,
                "Num": 125
            },
            {
                "DateKey": "20220614",
                "HourKey": 6,
                "Num": 121
            },
            {
                "DateKey": "20220614",
                "HourKey": 7,
                "Num": 120
            },
            {
                "DateKey": "20220614",
                "HourKey": 8,
                "Num": 133
            },
            {
                "DateKey": "20220614",
                "HourKey": 9,
                "Num": 100
            },
            {
                "DateKey": "20220614",
                "HourKey": 10,
                "Num": 114
            },
            {
                "DateKey": "20220614",
                "HourKey": 11,
                "Num": 139
            },
            {
                "DateKey": "20220614",
                "HourKey": 12,
                "Num": 114
            },
            {
                "DateKey": "20220614",
                "HourKey": 13,
                "Num": 114
            },
            {
                "DateKey": "20220614",
                "HourKey": 14,
                "Num": 141
            },
            {
                "DateKey": "20220614",
                "HourKey": 15,
                "Num": 115
            },
            {
                "DateKey": "20220614",
                "HourKey": 16,
                "Num": 116
            },
            {
                "DateKey": "20220614",
                "HourKey": 17,
                "Num": 103
            },
            {
                "DateKey": "20220614",
                "HourKey": 18,
                "Num": 107
            },
            {
                "DateKey": "20220614",
                "HourKey": 19,
                "Num": 107
            },
            {
                "DateKey": "20220614",
                "HourKey": 20,
                "Num": 106
            },
            {
                "DateKey": "20220614",
                "HourKey": 21,
                "Num": 131
            },
            {
                "DateKey": "20220614",
                "HourKey": 22,
                "Num": 120
            },
            {
                "DateKey": "20220614",
                "HourKey": 23,
                "Num": 131
            }
        ],
        "Info": {
            "DnsFormat": "HOUR",
            "DnsTotal": 2940,
            "Domain": "example.com",
            "EndDate": "2022-06-14",
            "StartDate": "2022-06-14"
        }
    }
}
```


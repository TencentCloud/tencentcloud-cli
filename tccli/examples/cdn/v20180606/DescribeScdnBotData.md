**Example 1: 获取bot统计曲线图( Bot流量统计)**



Input: 

```
tccli cdn DescribeScdnBotData --cli-unfold-argument  \
    --Domains zc-test-a.qcloudwaf.com \
    --StartTime '2020-04-20 00:00:00' \
    --EndTime '2020-04-20 23:59:59' \
    --Interval 2min \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Metric": "bot",
                "DetailData": [
                    {
                        "Time": "2020-04-24 00:00:00",
                        "Value": 735
                    },
                    {
                        "Time": "2020-04-24 01:00:00",
                        "Value": 1124
                    }
                ]
            },
            {
                "Metric": "total",
                "DetailData": [
                    {
                        "Time": "2020-04-24 00:00:00",
                        "Value": 735
                    },
                    {
                        "Time": "2020-04-24 01:00:00",
                        "Value": 1124
                    }
                ]
            },
            {
                "Metric": "qps",
                "DetailData": [
                    {
                        "Time": "2020-04-24 00:00:00",
                        "Value": 735
                    },
                    {
                        "Time": "2020-04-24 01:00:00",
                        "Value": 1124
                    }
                ]
            }
        ],
        "Interval": "2min",
        "RequestId": "8d492352-67f4-4fac-a752-331b973b3dcc"
    }
}
```


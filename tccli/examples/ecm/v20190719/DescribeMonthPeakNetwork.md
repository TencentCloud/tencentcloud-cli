**Example 1: 获取客户指定月份的带宽信息**

获取客户指定月份的带宽信息

Input: 

```
tccli ecm DescribeMonthPeakNetwork --cli-unfold-argument  \
    --Month 2020-09 \
    --Filters.0.Name region \
    --Filters.0.Values ap-zhengzhou-ecm
```

Output: 
```
{
    "Response": {
        "RequestId": "ee2849f2-facd-4f84-a0ab-bec49edda5fc",
        "MonthNetWorkData": [
            {
                "ZoneInfo": {
                    "ZoneId": "490001",
                    "ZoneName": "南京",
                    "Zone": "ap-nanjing-ecm-1"
                },
                "Month": "202001",
                "BandwidthPkgId": "bwp-mm9aw7jq",
                "Isp": "CMCC",
                "TrafficMaxIn": 12.345,
                "TrafficMaxOut": 12.345,
                "FeeTraffic": 12.345,
                "StartTime": "2021-03-01 00:00:00",
                "EndTime": "2021-03-29 23:59:59",
                "EffectiveDays": 2,
                "MonthDays": 30,
                "EffectiveDaysRate": 12.34
            }
        ]
    }
}
```


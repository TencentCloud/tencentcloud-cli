**Example 1: 获取DDoS攻击指标数据**



Input: 

```
tccli antiddos DescribeDDoSTrend --cli-unfold-argument  \
    --Business xx \
    --Ip xx \
    --Period 0 \
    --StartTime 2020-09-22 00:00:00 \
    --EndTime 2020-09-22 00:00:00 \
    --Id xx \
    --MetricName xx
```

Output: 
```
{
    "Response": {
        "Business": "bgp",
        "Count": 1,
        "Data": [
            1234
        ],
        "EndTime": "2018-08-27 16:05:10",
        "Id": "bgp-00000010",
        "Ip": "3.3.3.3",
        "MetricName": "bps",
        "Period": 3600,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "StartTime": "2018-08-27 15:05:10"
    }
}
```


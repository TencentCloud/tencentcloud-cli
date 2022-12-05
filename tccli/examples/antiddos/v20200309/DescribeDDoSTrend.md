**Example 1: 获取DDoS攻击指标数据**



Input: 

```
tccli antiddos DescribeDDoSTrend --cli-unfold-argument  \
    --Business bgpip \
    --Ip 1.1.1.1 \
    --Period 330 \
    --StartTime 2022-10-10 01:08:00 \
    --EndTime 2022-10-10 01:13:00 \
    --Id bgpip-00000xxx \
    --MetricName pps
```

Output: 
```
{
    "Response": {
        "Business": "bgpip",
        "Count": 2,
        "Data": [
            30,
            20
        ],
        "EndTime": "2022-10-10 01:13:00",
        "Id": "bgpip-00000xxx",
        "Ip": "1.1.1.1",
        "MetricName": "pps",
        "Period": 300,
        "RequestId": "2f44a9d8-2b6f-4a9a-b1da-9d05d9e6ad83",
        "StartTime": "2022-10-10 01:05:00"
    }
}
```


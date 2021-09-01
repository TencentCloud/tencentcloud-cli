**Example 1: 获取DDoS攻击占比分析**



Input: 

```
tccli dayu DescribeDDoSCount --cli-unfold-argument  \
    --Business bgp \
    --Id bgp-00000010 \
    --Ip 3.3.3.3 \
    --StartTime '2018-08-27 15:05:10' \
    --EndTime '2018-08-27 16:05:10' \
    --MetricName pkg
```

Output: 
```
{
    "Response": {
        "Business": "bgpip",
        "Data": [],
        "EndTime": "2019-03-07 14:50:00",
        "Id": "bgpip-000000y0",
        "Ip": "3.3.3.3",
        "RequestId": "69b1692b-4b6e-47c0-a7d6-0ff0da286874",
        "StartTime": "2019-03-07 00:00:00"
    }
}
```

